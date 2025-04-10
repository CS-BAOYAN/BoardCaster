import json
import os
import csv
import re

def extract_field(text, header):
    pattern = rf"### {header}\s+(.*?)(?:\n###|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


with open(os.environ['GITHUB_EVENT_PATH'], 'r', encoding='utf-8') as f:
    event = json.load(f)
    body = event["issue"]["body"]

name = extract_field(body, "学校名称")
institute = extract_field(body, "举办单位或学院")
description = extract_field(body, "简要描述（可选）")
deadline = extract_field(body, "报名截止日期")
website = extract_field(body, "官网链接")
tags = [tag.strip() for tag in extract_field(body, "标签（可多选）").replace("，", ",").split(",") if tag.strip()]
if tags[0] == "_No response_":
    tags = []
target = extract_field(body, "面向年级")


# 新条目拼接
new_entry = {
    "name": name,
    "institute": institute,
    "description": description,
    "deadline": deadline,
    "website": website,
    "tags": tags
}

# 标签补全逻辑
if not new_entry["tags"]:
    csv_file_path = '92.csv'
    found = False

    # 第一列查找
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                new_entry["tags"].extend(["985", "211"])
                found = True
                break

    # 第二列查找
    if not found:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[1] == name:
                    new_entry["tags"].append("211")
                    found = True
                    break

    # 第三列查找
    if not found:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[2] == name:
                    new_entry["tags"].append("双非")
                    found = True
                    break

    # 如果还没找到
    if not found:
        new_entry["tags"].append("四非")

    # 附加类标签查找
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3] == name:
                new_entry["tags"].append("TOP2")
                break

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[4] == name:
                new_entry["tags"].append("华五")
                break

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[5] == name:
                new_entry["tags"].append("C9")
                break

# 读取已有 JSON 数据
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 替换或追加
if target not in data:
    data[target] = []

found = False
for i, entry in enumerate(data[target]):
    if entry['name'] == new_entry['name'] and entry['institute'] == new_entry['institute']:
        data[target][i] = new_entry
        found = True
        break

if not found:
    data[target].append(new_entry)

# 写入文件
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
