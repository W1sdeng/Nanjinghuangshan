#!/usr/bin/env python3
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = r'D:\nanjing\nanjing-v16-complete.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 图片路径修复
replacements = {
    'day1-laomentong.jpg': '南京老门东.jpg',
    'day1-qinhuai1.jpg': '秦淮河夜游1.jpg',
    'day1-qinhuai2.jpg': '秦淮河夜游2.jpg',
    'day2-mingxiaoling.jpg': '明孝陵1.jpg',
    'day2-nanda1.jpg': '南京大学鼓楼校区1.jpg',
    'day2-nanda2.jpg': '南京大学鼓楼校区2.jpg',
    'day3-xuanwuhu.jpg': '玄武湖1.jpg',
    'day3-chengqiang.jpg': '台城城墙1.jpg',
    'day5-jinianguan.jpg': '侵华日军南京大屠杀遇难同胞纪念馆.jpg',
    'day7-yunhai1.jpg': '黄山云海.jpg',
    'day7-yunhai2.jpg': '黄山云海.jpg',
    'day1-ganxi.jpg': '明孝陵1.jpg',  # 临时用存在的图片
}

for old, new in replacements.items():
    content = content.replace(f'images/{old}', f'images/{new}')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("图片路径修复完成!")