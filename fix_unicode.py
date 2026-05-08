#!/usr/bin/env python3
c = open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8').read()

# 硬编码替换 - 使用UTF-8字符串
c = c.replace('day1-laomentong', '南京老门东')
c = c.replace('day1-qinhuai1', '秦淮河夜游1')
c = c.replace('day1-qinhuai2', '秦淮河夜游2')
c = c.replace('day2-nanda1', '南京大学鼓楼校区1')
c = c.replace('day2-nanda2', '南京大学鼓楼校区2')
c = c.replace('day5-jinianguan', '侵华日军南京大屠杀遇难同胞纪念馆')
c = c.replace('day7-yunhai1', '黄山云海')
c = c.replace('day7-yunhai2', '黄山云海')
c = c.replace('day4-zongtong1', '南京总统府1')
c = c.replace('day4-zongtong2', '南京总统府2')

open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8').write(c)
print('Done')