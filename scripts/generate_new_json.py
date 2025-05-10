import json
from collections import defaultdict

province_map = {
    "清华大学": "北京市",
    "北京大学": "北京市",
    "中国科学院": "北京市",
    "香港中文大学（深圳）": "广东省",
    "香港科技大学（广州）": "广东省",
    "南方科技大学": "广东省",
    "香港科技大学": "香港特别行政区",
    "香港中文大学": "香港特别行政区",
    "上海创智学院": "上海市",
    "上海交通大学": "上海市",
    "上海科技大学": "上海市",
    "上海AILAB": "上海市",
    "西湖大学": "浙江省",
    "南京大学": "江苏省",
    "哈尔滨工业大学": "黑龙江省",
}

with open("data.json", "r", encoding="utf-8") as f:
    camp2025 = json.load(f)["camp2025"]

by_province = defaultdict(list)
for item in camp2025:
    province = item.get("province")
    if not province:
        province = province_map.get(item["name"], "未知地区")
        item["province"] = province
    by_province[province].append(item)

statistics = []
for province, entries in by_province.items():
    stats = {
        "province": province,
        "count": len(entries),
        "schools": [entry["name"] for entry in entries],
    }
    statistics.append(stats)

result = {
    "byProvince": dict(by_province),
    "statistics": statistics
}

with open("camp2025-by-province.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

