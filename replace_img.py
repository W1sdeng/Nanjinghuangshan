#!/usr/bin/env python3
import os
import re

# 读取HTML
with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 获取images目录中所有文件
img_dir = r'D:\nanjing\images'
files = os.listdir(img_dir)

# 找到中文名文件
chinese_files = {}
for f in files:
    if not f.startswith('day'):
        # 这个文件是中文名
        # 尝试提取关键词
        if '老门东' in f:
            chinese_files['laomentong'] = f
        elif '秦淮' in f:
            chinese_files['qinhuai'] = f
        elif '大学' in f and '鼓楼' in f:
            chinese_files['nanda'] = f
        elif '纪念馆' in f or '大屠杀' in f:
            chinese_files['jinianguan'] = f
        elif '云海' in f:
            chinese_files['yunhai'] = f
        elif '总统府' in f:
            chinese_files['zongtong'] = f

print("Found Chinese files:", chinese_files)

# 替换
if 'laomentong' in chinese_files:
    html = html.replace('day1-laomentong.jpg', f"images/{chinese_files['laomentong']}")

# 保存
with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")