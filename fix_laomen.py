#!/usr/bin/env python3
c = open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8').read()
c = c.replace('day1-laomentong', '南京老门东')
open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8').write(c)
print('Done')