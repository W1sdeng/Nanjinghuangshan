#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\nanjing\nanjing-v16-complete.html', 'rb') as f:
    content = f.read()

# 解码为utf-8
content = content.decode('utf-8')

# 替换
content = content.replace('day1-laomentong.jpg', '南京老门东.jpg')
content = content.replace('day3-hongshan.jpg', '明孝陵2.jpg')  # 用现有图片
content = content.replace('day3-jimingsi.jpg', '明孝陵3.jpg')  # 用现有图片
content = content.replace('day4-zongtong1.jpg', '南京总统府1.jpg')
content = content.replace('day4-zongtong2.jpg', '南京总统府2.jpg')

# 写回
with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')