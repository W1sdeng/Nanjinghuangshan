import os, base64

html_path = r'D:\nanjing\nanjing-huangshan-zhoucheng-v10.html'
images_dir = r'D:\nanjing\images'
out_path = r'D:\nanjing\nanjing-FINAL.html'

# 读取原HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 遍历images文件夹中的所有图片文件
count = 0
for filename in os.listdir(images_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        filepath = os.path.join(images_dir, filename)
        # 转为base64
        with open(filepath, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        # 判断mime类型
        ext = filename.lower().split('.')[-1]
        mime = 'jpeg' if ext in ['jpg', 'jpeg'] else 'png'
        data_uri = f'data:image/{mime};base64,{b64}'
        # 替换HTML中的图片路径
        old_path1 = f'images/{filename}'
        old_path2 = filename
        if old_path1 in html:
            html = html.replace(old_path1, data_uri)
            count += 1
            print(f'Embedded: {filename}')
        elif old_path2 in html:
            html = html.replace(old_path2, data_uri)
            count += 1
            print(f'Embedded: {filename}')

# 保存新文件
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done! Embedded {count} images. Saved to: {out_path}')
