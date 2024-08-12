import json
import os
import csv

target = os.getenv('INPUT_TARGET')

# 读取现有的 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 从环境变量中获取新条目
new_entry = {
    "name": os.getenv('INPUT_NAME'),
    "institute": os.getenv('INPUT_INSTITUTE'),
    "description": os.getenv('INPUT_DESCRIPTION'),
    "deadline": os.getenv('INPUT_DEADLINE'),
    "website": os.getenv('INPUT_WEBSITE'),
    "tags": json.loads(os.getenv('INPUT_TAGS', '[]'))
}

if not new_entry["tags"]:
    csv_file_path = '92.csv'
    found = False
    name = new_entry["name"]

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

    # 如果没有找到
    if not found:
        new_entry["tags"].append("四非")
    
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3] == name:
                new_entry["tags"].append(["TOP2"])
                break
            
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[4] == name:
                new_entry["tags"].append(["华五"])
                break
            
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[5] == name:
                new_entry["tags"].append(["C9"])
                break

# 检查是否存在完全一致的条目
found = False
for i, entry in enumerate(data[target]):
    if entry['name'] == new_entry['name'] and entry['institute'] == new_entry['institute']:
        data[target][i] = new_entry
        found = True
        break

# 如果没有找到完全一致的条目，则添加新条目
if not found:
    data[target].append(new_entry)

# 将更新后的数据写回 JSON 文件
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
