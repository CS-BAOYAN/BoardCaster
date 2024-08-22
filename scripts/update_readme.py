import datetime

def update_third_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    utc_now = datetime.datetime.now()
    beijing_time = utc_now + datetime.timedelta(hours=8)
    current_time = beijing_time.strftime("%Y-%m-%d %H:%M:%S")

    if len(lines) >= 5:
        lines[4] = f"最后修改日期为：{current_time}\n"
    else:
        print("文件少于 5 行，无法替换第 5 行。")

    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


file_path = 'README.md'
update_third_line(file_path)