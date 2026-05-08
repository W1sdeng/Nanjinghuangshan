c = open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8').read()
print('quote class:', c.count('class="quote"'))
print('conclusion class:', c.count('class="conclusion"'))