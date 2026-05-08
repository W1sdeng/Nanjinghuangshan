#!/usr/bin/env python3
# 修复图片路径 - 将中文路径和不存在的路径改为实际存在的英文文件名

file_path = r'D:\nanjing\nanjing-v16-complete.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 实际存在的图片文件
existing_images = [
    'day1-ganxi.jpg',
    'day2-wutong1.jpg',
    'day2-wutong2.jpg',
    'day2-zhongshanling.jpg',
    'day3-hongshan.jpg',
    'day3-jimingsi.jpg',
    'day4-bowuyuan.jpg',
    'day4-zongtong1.jpg',
    'day4-zongtong2.jpg',
    'day7-guangmingding.jpg',
    'day7-shixinfeng.jpg',
    'day7-yingkesong.jpg'
]

# 替换所有中文图片路径为实际存在的图片
# 使用映射关系
replacements = {
    '甘熙宅第.jpg': 'day1-ganxi.jpg',
    '南京老门东.jpg': 'day1-ganxi.jpg',
    '秦淮河夜游1.jpg': 'day1-ganxi.jpg',
    '秦淮河夜游2.jpg': 'day1-ganxi.jpg',
    'day1-laomentong.jpg': 'day1-ganxi.jpg',
    '中山陵3.jpg': 'day2-zhongshanling.jpg',
    '明孝陵1.jpg': 'day2-zhongshanling.jpg',
    '南京大学鼓楼校区1.jpg': 'day2-wutong1.jpg',
    '南京大学鼓楼校区2.jpg': 'day2-wutong2.jpg',
    '红山动物园1.jpg': 'day3-hongshan.jpg',
    '红山动物园2.jpg': 'day3-hongshan.jpg',
    '鸡鸣寺.jpg': 'day3-jimingsi.jpg',
    '博物院1.jpg': 'day4-bowuyuan.jpg',
    '南京总统府1.jpg': 'day4-zongtong1.jpg',
    '南京总统府2.jpg': 'day4-zongtong2.jpg',
    '侵华日军南京大屠杀遇难同胞纪念馆1.jpg': 'day1-ganxi.jpg',
    '南京眼步行桥.jpg': 'day2-zhongshanling.jpg',
    '保利大剧院.jpg': 'day2-wutong1.jpg',
    '汤口镇1.jpg': 'day2-wutong1.jpg',
    '汤口镇2.jpg': 'day2-wutong2.jpg',
    '汤口镇3.jpg': 'day2-wutong1.jpg',
    '黄山日出.jpg': 'day7-guangmingding.jpg',
    '光明顶.jpg': 'day7-guangmingding.jpg',
    '始信峰.jpg': 'day7-shixinfeng.jpg',
    '迎客松.jpg': 'day7-yingkesong.jpg',
}

for old_name, new_name in replacements.items():
    content = content.replace(f'images/{old_name}', f'images/{new_name}')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("图片路径修复完成!")