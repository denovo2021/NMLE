import pdfplumber
import re
import json

def extract_text_from_pdf(pdf_path, skip_first_page=True):
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = ""

        start_page = 6 if skip_first_page else 0
        for page in pdf.pages[start_page:]:
            extracted_text += page.extract_text()

    return extracted_text

pdf_path = "/Users/Documents/TMDU/MedicalExaminationGPT/117/a.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

def remove_page_info(text):
    pattern = r"DDKKIIXX0011AAHH..iinndddd \d{2,4} 22002222//1122//2200 1155::1133::(1177|1188|1199)"
    cleaned_text = re.sub(pattern, r'', text)
    return cleaned_text

def replace_cid_numbers(text):
    def replace_cid(match):
        cid_number = int(match.group(1))
        if cid_number == 139:
            return "("
        elif cid_number == 140:
            return ")"
        elif cid_number == 7705:
            return "梢"
        else:
            return str(cid_number)

    pattern = r'\(cid:(\d+)\)'
    replaced_text = re.sub(pattern, replace_cid, text)
    return replaced_text

def replace_text_with_parentheses(text):
    def replace_parentheses(match):
        if match.group(1).isalpha():
            return f"{match.group(1)}({match.group(2)})"
        else:
            return match.group(0)

    pattern = r'(\w)0(.*?)2'
    replaced_text = re.sub(pattern, replace_parentheses, text)
    return replaced_text

def insert_underscore(text):
    def replace_ch(match):
        return f"{match.group(1)} CH_{match.group(2)} {match.group(3)}"

    pattern = r'(\d+)(\s+CH\s+)(\d+)(が高値を示す疾患はどれか。)'
    replaced_text = re.sub(pattern, replace_ch, text)
    return replaced_text

def remove_dkix_lines(text):
    lines = text.split("\n")
    filtered_lines = [line for line in lines if "DKIX" not in line]
    return "\n".join(filtered_lines)

def remove_single_number(text):
    pattern = r"^\d+$\n?"
    replaced_text = re.sub(pattern, "", text, flags = re.MULTILINE)
    return replaced_text

def clean_others(text):
    # Remove lines that start with "別 冊" or "No."
    cleaned_text = re.sub(r"^(別 冊|No\.).*?$\n?", "", text, flags=re.MULTILINE)
    return cleaned_text.strip()

def process_text(text):
    text_without_page_info = remove_page_info(text)
    text_replaced_cid = replace_cid_numbers(text_without_page_info)
    text_replaced_parentheses = replace_text_with_parentheses(text_replaced_cid)
    text_without_dkix_lines = remove_dkix_lines(text_replaced_parentheses)
    text_without_single_number = remove_single_number(text_without_dkix_lines)
    text_without_underscore = insert_underscore(text_without_single_number)
    final_text = clean_others(text_without_underscore)
    return final_text

processed_text = process_text(extracted_text)

print(processed_text)

def parse_questions(text):
    lines = text.strip().split("\n")
    cases = []
    current_case = {}
    is_reading_text = False

    for line in lines:
        match = re.match(r"(\d+)\s", line)

        if match:
            # Save the previous case if it exists
            if current_case:
                cases.append(current_case)

            # Initialize a new case
            current_case = {"number": int(match.group(1)), "text": "", "choices": []}
            is_reading_text = True
            current_case['text'] = re.sub(r"^\d+\s", "", line).strip()
        elif is_reading_text:
            if re.match(r"[ａ-ｚ]\s", line):  # If the line starts with a choice identifier
                is_reading_text = False

            if is_reading_text:
                current_case['text'] += "" + line.strip()  # Append to the problem text
            else:
                current_case["choices"].append(line.strip())  # Add a choice
        else:
            current_case["choices"].append(line.strip())  # Add a choice

    # Add the last case if it exists
    if current_case:
        cases.append(current_case)

    return cases

json_data = parse_questions(processed_text)
print(json_data)
with open("/Users/Documents/TMDU/MedicalExaminationGPT/questions_117_a.json", "w", encoding="utf-8") as outfile:
    json.dump(json_data, outfile, indent=2, ensure_ascii=False)
