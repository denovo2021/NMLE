import json
import openai
import os
import time
import re

# setting of OpenAI API
openai.api_key = 'API_key'

def create_prompts(question_file, i):
    # Read the questions
    with open(question_file, 'r') as qf:
        questions = json.load(qf)

    answers = []

    question = questions[i]
    number = question["number"]
    prompt_text = f"医師国家試験問題{number}に関する深い知識を持っている。この問題の内容と選択肢を慎重に検討し、最も正しいと思われる答えを選び、解答のみを出力する。問題: {question['text']} 選択肢は以下の通り: {', '.join(question['choices'])}。# 以下の条件を必ず守ること：選択肢を選ぶ個数に注意する。正しい選択肢のアルファベットのみを半角の大文字で返す。余計な文字は付け加えずに答える。例えば解答が(a, c)の場合は(AC)と答える"

    messages = [
        {"role": "system", "content": "あなたは、医師国家試験問題の専門家である。試験問題に関して深い理解を持ち、正しい答えを選び出す際の解説もできる。"},
        {"role": "user", "content": prompt_text}
    ]

    temperature = 0

    # Call OpenAI API
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages, max_tokens = 10)

    # Output of answers
    answer = response['choices'][0]['message']['content'].strip().split("\n")
    answers.extend(answer)

    return i+1, answers

def safe_api_call(question_file, i):
    while True:
        try:
            _, answers = create_prompts(question_file, i)
            return answers
        except openai.error.OpenAIError as e:
            match = re.search(r"Please try again in (\d+)ms", str(e))
            if match:
                wait_time = int(match.group(1)) / 1000 + 1  # Convert milliseconds to seconds and add a small buffer
                print(f"Rate limit reached, waiting for {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e

def process_questions_without_image(question_file):
    with open(question_file, 'r') as qf:
        questions = json.load(qf)

    results = {}
    for i in range(len(questions)):  # Processing questions from 1 to end
        question = questions[i]
        key = partCap + str(i+1).zfill(3)  # Create a key like "A001", "A002", ...

        if "image" not in question:  # Check if the "image" field is not present
            answers = safe_api_call(question_file, i)
            results[key] = ''.join(answers)  # Join list of answers to form a string
        else:
            results[key] = "*"

    return results

def write_results_to_json(results, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, ensure_ascii=False, indent=4)

# Change this part in succession
directory = "117"
part = "a"
partCap = "F"
question_file = "/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}.json".format(directory, part)

results = process_questions_without_image(question_file)
output_file = "/Users/Documents/TMDU/MedicalExaminationGPT/{0}/results_{1}_refined.json".format(directory, part)  # Update with desired output path
write_results_to_json(results, output_file)
