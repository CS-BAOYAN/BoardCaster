import json

# 读取现有的 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建一个字典，以 name 为键，存储相应的条目
schools_dict = {}
for entry in data['schools']:
    name = entry['name']
    if name not in schools_dict:
        schools_dict[name] = []
    schools_dict[name].append(entry)

# 生成 Markdown 内容
markdown_lines = []
for name, entries in schools_dict.items():
    markdown_lines.append(f"## {name}\n")
    for entry in entries:
        line = f"【截止日期：{entry['deadline'][0:10]} {entry['deadline'][11:19]}】[{entry['institute']}]({entry['website']}) {entry['description']}"
        markdown_lines.append(line)
    markdown_lines.append("")  # 空一行
    markdown_lines.append("")  # 空一行

# 将 Markdown 内容写入文件
with open('output.md', 'w', encoding='utf-8') as file:
    file.write("\n".join(markdown_lines))
