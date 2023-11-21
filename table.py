import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pylab as plt
import seaborn as sns
sns.set(font = "IPAexGothic")
import datetime
import os
import math
import json

# for Table 1
# 112
general_list_a_112 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A015"]
general_list_b_112 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024"]
general_list_c_112 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024"]
general_list_d_112 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D015"]
general_list_e_112 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025", "E026"]
general_list_f_112 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F035","F036", "F037", "F038", "F039", "F040", "F041", "F042", "F043", "F044", "F084"]
general_lists_112 = {
    "a": general_list_a_112,
    "b": general_list_b_112,
    "c": general_list_c_112,
    "d": general_list_d_112,
    "e": general_list_e_112,
    "f": general_list_f_112
}
year = 112

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_112[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# 113
general_list_a_113 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A075"]
general_list_b_113 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024"]
general_list_c_113 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024", "C066"]
general_list_d_113 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D015"]
general_list_e_113 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025", "E026"]
general_list_f_113 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F035","F036", "F037", "F038", "F039", "F040", "F041", "F042", "F043", "F083", "F084"]
general_lists_113 = {
    "a": general_list_a_113,
    "b": general_list_b_113,
    "c": general_list_c_113,
    "d": general_list_d_113,
    "e": general_list_e_113,
    "f": general_list_f_113
}
year = 113

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_113[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# 114
general_list_a_114 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A015"]
general_list_b_114 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024", "B025"]
general_list_c_114 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024", "C025", "C026", "C027", "C028", "C029", "C030", "C031", "C032",
            "C033", "C034", "C075"]
general_list_d_114 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D075"]
general_list_e_114 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025"]
general_list_f_114 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F075"]
general_lists_114 = {
    "a": general_list_a_114,
    "b": general_list_b_114,
    "c": general_list_c_114,
    "d": general_list_d_114,
    "e": general_list_e_114,
    "f": general_list_f_114
}
year = 114

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_114[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# 115
general_list_a_115 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A015"]
general_list_b_115 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024", "B025"]
general_list_c_115 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024", "C025", "C026", "C027", "C028", "C029", "C030", "C031", "C032",
            "C033", "C034", "C035"]
general_list_d_115 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D015"]
general_list_e_115 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025"]
general_list_f_115 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F075"]
general_lists_115 = {
    "a": general_list_a_115,
    "b": general_list_b_115,
    "c": general_list_c_115,
    "d": general_list_d_115,
    "e": general_list_e_115,
    "f": general_list_f_115
}
year = 115

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_115[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# 116
general_list_a_116 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A015"]
general_list_b_116 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024", "B050"]
general_list_c_116 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024", "C025", "C026", "C027", "C028", "C029", "C030", "C031", "C032",
            "C033", "C034", "C035"]
general_list_d_116 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D015"]
general_list_e_116 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025"]
general_list_f_116 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F075"]
general_lists_116 = {
    "a": general_list_a_116,
    "b": general_list_b_116,
    "c": general_list_c_116,
    "d": general_list_d_116,
    "e": general_list_e_116,
    "f": general_list_f_116
}
year = 116

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_116[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# 117
general_list_a_117 = ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A011", "A012", "A013", "A014", "A075"]
general_list_b_117 = ["B001", "B002", "B003", "B004", "B005", "B006", "B007", "B008", "B009", "B010", "B011", "B012", "B013", "B014", "B015",
            "B016", "B017", "B018", "B019", "B020", "B021", "B022", "B023", "B024", "B025"]
general_list_c_117 = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014", "C015",
            "C016", "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024", "C025", "C026", "C027", "C028", "C029", "C030", "C031", "C032",
            "C033", "C034", "C035"]
general_list_d_117 = ["D001", "D002", "D003", "D004", "D005", "D006", "D007", "D008", "D009", "D010", "D011", "D012", "D013", "D014", "D015"]
general_list_e_117 = ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015",
            "E016", "E017", "E018", "E019", "E020", "E021", "E022", "E023", "E024", "E025"]
general_list_f_117 = ["F001", "F002", "F003", "F004", "F005", "F006", "F007", "F008", "F009", "F010", "F011", "F012", "F013", "F014", "F015",
            "F016", "F017", "F018", "F019", "F020", "F021", "F022", "F023", "F024", "F025", "F026", "F027", "F028", "F029", "F030", "F031",
            "F032", "F033", "F034", "F075"]
general_lists_117 = {
    "a": general_list_a_117,
    "b": general_list_b_117,
    "c": general_list_c_117,
    "d": general_list_d_117,
    "e": general_list_e_117,
    "f": general_list_f_117
}
year = 117

for part in ["a", "b", "c", "d", "e", "f"]:
    qti = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
    gene_num_qti, clin_num_qti = 0, 0
    for i in range(len(qti)):
        if part.upper() +  "{0}".format(qti[i]["number"]).zfill(3) in general_lists_117[part]:
            gene_num_qti += 1
        else:
            clin_num_qti += 1
    print(year, part, gene_num_qti, clin_num_qti)

# for Table 2
general_lists = {
    112: general_lists_112,
    113: general_lists_113,
    114: general_lists_114,
    115: general_lists_115,
    116: general_lists_116,
    117: general_lists_117,
}

length_list = {
    112: {"b": (24, 26), "e": (26-1, 24), "a": (15, 60-1), "c": (25, 50), "d": (15, 60), "f": (45, 39)},
    113: {"b": (24, 26), "e": (26, 24), "a": (15-1, 60), "c": (35, 50-1), "d": (15, 60), "f": (45-1, 45-1)},
    114: {"b": (25, 25), "e": (25, 24-1), "a": (15, 60), "c": (35, 40), "d": (15, 60), "f": (35, 45-1)},
    115: {"b": (25, 25), "e": (25, 25), "a": (15, 60), "c": (35, 40), "d": (15, 60), "f": (35, 45)},
    116: {"b": (25, 25-1), "e": (25-1, 25), "a": (15, 60), "c": (35, 40-1), "d": (15, 60-1), "f": (35, 45)},
    117: {"b": (25, 25), "e": (25, 25), "a": (15, 60), "c": (35-1, 40-1), "d": (15, 60-2), "f": (35, 45-1)},
}
# 採点除外
# 112 A-43（臨床）, B-30（臨床、複数正解）, E-6（一般、正解した受験者は採点対照、不正解は採点対象から除外→不正解）
# 113 A-5（一般）, C-34（臨床）, F-42（一般）, F-81（臨床）
# 114 E-29（臨床）, F-63（臨床）
# 116 A-34（臨床）, A-71（臨床、複数正解→resultを修正）, B-6（一般、正解した受験者は採点対象、不正解は採点対象から除外→正解）, B-43（臨床）,C-36（臨床）, D-64（臨床）, E-16（一般、正解した受験者は採点対象、不正解は採点対象から除外→不正解）
# 117 C-15（一般）, C-60（臨床）, D-38（臨床）, D-53（臨床）, F-42（臨床）

for year in [112, 113, 114, 115, 116, 117]:
    for part in ["b", "e", "a", "c", "d", "f"]:
        ans = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/ans_{0}.json".format(year)))
        rt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/results_{1}_refined_image.json".format(year, part)))
        correct_num_basic, correct_num_clinical = 0, 0
        for k, v in rt.items():
            if k in general_lists[year][part]:
                if ans[k] == v:
                    correct_num_basic += 1
            else:
                if ans[k] == v:
                    correct_num_clinical += 1
        print(year, part, correct_num_basic, length_list[year][part][0],  "{:.1f}".format(correct_num_basic/length_list[year][part][0]*100), correct_num_clinical, length_list[year][part][1], "{:.1f}".format(correct_num_clinical/length_list[year][part][1]*100))


# for Supplementary Table 2
year = 113 # change here in sequence
ans = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/ans_{0}.json".format(year)))

for part in ["a", "b", "c", "d", "e", "f"]:
    rt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/results_{1}_refined_image.json".format(year, part)))
    qt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}.json".format(year, part)))

    for k, v in rt.items():
        if ans[k] != v:
            if k in general_lists[year][part]:
                if "image" in next((item for item in qt if item.get("number") == int(k[1:])), None):
                    print("Checking for number:", k, "Basic", "Image")
                else:
                    print("Checking for number:", k, "Basic")
            else:
                if "image" in next((item for item in qt if item.get("number") == int(k[1:])), None):
                    print("Cheking for number", k, "Clinical", "Image")
                else:
                    print("Cheking for number", k, "Clinical")
            #matching_text = next((item["text"] for item in qt if item["number"] == int(k[1:])), "No match found")
            #print(matching_text)

# for Table 3

for year in range(112, 118):
    length_img = 0
    for part in ["a", "b", "c", "d", "e", "f"]:
        qt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}_filtered.json".format(year, part)))
        length_img += len(qt)
    print(year, length_img)

year = 113 # change here in sequence
ans = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/ans_{0}.json".format(year)))

num_fail = 0
for part in ["a", "b", "c", "d", "e", "f"]:
    rt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/results_{1}_refined_image.json".format(year, part)))
    qt = json.load(open("/Users/Documents/TMDU/MedicalExaminationGPT/{0}/questions_{0}_{1}.json".format(year, part)))
    for k, v in rt.items():
        if ans[k] != v:
            if "image" in next((item for item in qt if item.get("number") == int(k[1:])), None):
                    num_fail += 1
print(num_fail)
