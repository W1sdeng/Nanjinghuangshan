import os, base64, shutil

images_dir = r'D:\nanjing\images'
html_path = r'D:\nanjing\nanjing-huangshan-zhoucheng-v10.html'
out_path = r'D:\nanjing\nanjing-FINAL.html'

# 1. 重命名文件为英文（对应景点）
rename_map = {
    '甘熙宅第.jpg': 'day1-ganxi.jpg',
    '老门东.jpg': 'day1-laomendong.jpg',
    '秦淮河1.jpg': 'day1-qinhuai1.jpg',
    '秦淮河2.jpg': 'day1-qinhuai2.jpg',
    '明孝陵.jpg': 'day2-mingxiaoling.jpg',
    '中山陵.jpg': 'day2-zhongshanling.jpg',
    '梧桐大道1.jpg': 'day2-wutong1.jpg',
    '梧桐大道2.jpg': 'day2-wutong2.jpg',
    '南京大学鼓楼校1.jpg': 'day2-nanda1.jpg',
    '南京大学鼓楼校2.jpg': 'day2-nanda2.jpg',
    '红山森林动物园.jpg': 'day3-hongshan.jpg',
    '鸡鸣寺.jpg': 'day3-jimingsi.jpg',
    '玄武湖.jpg': 'day3-xuanwuhu.jpg',
    '夜骑玄武湖.jpg': 'day3-nightride.jpg',
    '南京博物院.jpg': 'day4-bowuyuan.jpg',
    '总统府1.jpg': 'day4-zongtong1.jpg',
    '总统府2.jpg': 'day4-zongtong2.jpg',
    '纪念馆.jpg': 'day5-jinianguan.jpg',
    '雨花台1.jpg': 'day5-yuhuatai1.jpg',
    '雨花台2.jpg': 'day5-yuhuatai2.jpg',
    '汤口1.jpg': 'day6-tangkou1.jpg',
    '汤口2.jpg': 'day6-tangkou2.jpg',
    '汤口3.jpg': 'day6-tangkou3.jpg',
    '黄山云海1.jpg': 'day7-yunhai1.jpg',
    '黄山云海2.jpg': 'day7-yunhai2.jpg',
    '始信峰.jpg': 'day7-shixinfeng.jpg',
    '光明顶.jpg': 'day7-guangmingding.jpg',
    '迎客松.jpg': 'day7-yingkesong.jpg',
    '汤口周边.jpg': 'day8-tangkou-around.jpg'
}

print('Step 1: Renaming files...')
for old, new in rename_map.items():
    old_path = os.path.join(images_dir, old)
    new_path = os.path.join(images_dir, new)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        shutil.move(old_path, new_path)
        print(f'  {old} -> {new}')

# 2. 读取HTML并嵌入图片
print('Step 2: Embedding images into HTML...')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for old, new in rename_map.items():
    filepath = os.path.join(images_dir, new)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        mime = 'jpeg' if new.lower().endswith(('.jpg', '.jpeg')) else 'png'
        data_uri = f'data:image/{mime};base64,{b64}'
        html = html.replace(f'images/{old}', data_uri)
        count += 1
        print(f'  Embedded: {new}')

# 3. 保存
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done! {count} images embedded. Saved to: {out_path}')
