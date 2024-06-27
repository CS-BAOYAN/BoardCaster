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
