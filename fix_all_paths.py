#!/usr/bin/env python3
# 正确修复所有图片路径

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# ========== 英文名保持不变 ==========
# day1-ganxi.jpg (甘熙宅第) - 保持
# day2-wutong1.jpg, day2-wutong2.jpg (梧桐大道) - 保持
# day2-zhongshanling.jpg (中山陵) - 保持
# day3-hongshan.jpg (红山动物园) - 保持
# day3-jimingsi.jpg (鸡鸣寺) - 保持
# day4-bowuyuan.jpg (南京博物院) - 保持
# day4-zongtong1.jpg, day4-zongtong2.jpg (总统府) - 保持
# day7-guangmingding.jpg (光明顶) - 保持
# day7-shixinfeng.jpg (始信峰) - 保持
# day7-yingkesong.jpg (迎客松) - 保持

# ========== 中文名需要更新 ==========
# 黄山云海
c = c.replace('day7-yunhai1.jpg', '黄山云海.jpg')
c = c.replace('day7-yunhai2.jpg', '黄山云海.jpg')

# 明孝陵
c = c.replace('明孝陵1.jpg', '明孝陵1.jpg')  # 已经是
c = c.replace('明孝陵2.jpg', '明孝陵2.jpg')  # 已经是
c = c.replace('明孝陵3.jpg', '明孝陵3.jpg')  # 已经是

# 南京大学鼓楼校区
c = c.replace('day2-nanda1.jpg', '南京大学鼓楼校区1.jpg')
c = c.replace('day2-nanda2.jpg', '南京大学鼓楼校区2.jpg')

# 南京老门东
c = c.replace('day1-laomentong.jpg', '南京老门东.jpg')
c = c.replace('day1-laomentong', '南京老门东')

# 侵华日军南京大屠杀遇难同胞纪念馆
c = c.replace('day5-jinianguan.jpg', '侵华日军南京大屠杀遇难同胞纪念馆.jpg')
c = c.replace('day5-jinianguan', '侵华日军南京大屠杀遇难同胞纪念馆')

# 秦淮河夜游
c = c.replace('day1-qinhuai1.jpg', '秦淮河夜游1.jpg')
c = c.replace('day1-qinhuai2.jpg', '秦淮河夜游2.jpg')

# 台城城墙
c = c.replace('day3-chengqiang.jpg', '台城城墙1.jpg')

# 梧桐大道3
c = c.replace('day2-wutong1.jpg', '梧桐大道3.jpg')  # 实际上需要检查是否已有

# 先锋书店 - 可能需要用day2-nanda路径

# 玄武湖
c = c.replace('day3-xuanwuhu.jpg', '玄武湖1.jpg')
c = c.replace('day3-nightride.jpg', '玄武湖2.jpg')

# 音乐台 - 可能需要用day2-zhongshanling

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("图片路径已修复!")