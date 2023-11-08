import json
import openai
import base64
import requests
import re
import time

# OpenAI API Key
api_key = "API_key"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to create prompts and send API requests
def create_prompts(question_file, i, base64_image):
    # Extract the question and choices
    question = question_file[i]["text"]
    choices = ",".join(question_file[i]["choices"])

    # Prepare the messages for the payload
    messages = [
      {
        "role": "system", "content": "あなたは、医師国家試験問題の専門家である。試験問題に関して深い理解を持ち、正しい答えを選び出す際の解説もできる。"
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": f"医師国家試験問題に関する深い知識を持っている。この問題の内容と選択肢を慎重に検討し、最も正しいと思われる答えを選び、解答のみを出力する。問題: {question} 選択肢は以下の通り: {choices}。# 以下の条件を必ず守ること：選択肢を選ぶ個数に注意する。正しい選択肢のアルファベットのみを半角の大文字で返す。余計な文字は付け加えずに答える。例えば解答がa, cの場合はACと答える。解答を出力できないときは、nullを出力せず、空白を出力すること。"
          },
          {
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{base64_image}"
          }
        ]
      }
    ]

    # Prepare the payload
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": messages,
        "max_tokens": 10,
        "temperature": 0
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send the API request
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

# Function to handle rate limits and other API errors
def safe_api_call(question_file, i, base64_image):
    while True:
        try:
            return create_prompts(question_file, i, base64_image)
        except openai.error.OpenAIError as e:
            match = re.search(r"Please try again in (\d+)ms", str(e))
            if match:
                wait_time = int(match.group(1)) / 1000 + 1  # Convert milliseconds to seconds and add a small buffer
                print(f"Rate limit reached, waiting for {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e

# Function to format question number as specified
def format_question_number(part, number):
    return f"{part.upper()}{number:03d}"

# Function to process all image problems and save the answers to a JSON file
def process_image_problems(year, part):
    # Load the image problem data
    question_file_path = f"/Users/Documents/TMDU/MedicalExaminationGPT/{year}/questions_{year}_{part}_filtered.json"
    with open(question_file_path, 'r') as f:
        question_file = json.load(f)

    # Initialize an empty dictionary to store the answers
    answers_dict = {}

    # Iterate over the image_problem
    for i, problem in enumerate(question_file):
        formatted_number = format_question_number(part, int(problem["number"]))
        print(f"Processing question number {formatted_number} with image {problem['image']}...")

        # Get the base64 string of the image
        image_path = f"/Users/Documents/TMDU/MedicalExaminationGPT/{year}/{part}/{problem['image']}"
        base64_image = encode_image(image_path)

        # Get the answers using the safe API call
        response_json = safe_api_call(question_file, i, base64_image)

        # Extract the answer and add to the dictionary
        answer = response_json["choices"][0]["message"]["content"] if "choices" in response_json else None
        answers_dict[formatted_number] = answer

    # Save the answers to a JSON file
    with open(f'/Users/Documents/TMDU/MedicalExaminationGPT/{year}/Image_answers_{year}_{part}.json', 'w') as outfile:
        json.dump(answers_dict, outfile, ensure_ascii=False, indent=4)

    print(f"Finished processing and saving answers for year {year}, part {part}.")

# Replace 'year' and 'part' with the actual values you want to process
year = 117
part = "a"
process_image_problems(year, part)

# Paths to the JSON files
path_a = f"/Users/Documents/TMDU/MedicalExaminationGPT/{year}/results_{part}_refined.json"
path_b = f"/Users/Documents/TMDU/MedicalExaminationGPT/{year}/Image_answers_{year}_{part}.json"

# Read content of A.json
with open(path_a, 'r') as file:
    data_a = json.load(file)

# Read content of B.json
with open(path_b, 'r') as file:
    data_b = json.load(file)

# Update data_a with data_b
data_a.update(data_b)

# Write the updated dictionary back to a new JSON file
with open(f"/Users/Documents/TMDU/MedicalExaminationGPT/{year}/results_{part}_refined_image.json", 'w') as file:
    json.dump(data_a, file, ensure_ascii=False, indent=4)
