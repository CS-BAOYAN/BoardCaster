import json
import os

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

# 添加新条目到 schools 列表
data[target].append(new_entry)

# 将更新后的数据写回 JSON 文件
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
