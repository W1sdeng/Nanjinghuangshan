#!/usr/bin/env python3

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Day7 - 云海图片在描述之前
old1 = '''<div class="quote">"五岳归来不看山，黄山归来不看岳。"<div class="quote-author">—— 徐霞客</div></div>
                
                <div class="day-images-grid">
                    <img src="images/黄山云海.jpg" alt="黄山云海翻涌" class="day-image" loading="lazy" onclick="openModal('day7', 0)">
                    <img src="images/黄山云海.jpg" alt="黄山云海松石" class="day-image" loading="lazy" onclick="openModal('day7', 1)">
                    <div class="image-caption">☁️ 黄山云海 · 云海翻涌与松石画廊</div>
                </div>

                <img src="images/day7-shixinfeng.jpg" alt="始信峰黄山小峰" class="day-image" loading="lazy" onclick="openModal('day7', 2)">
                <div class="image-caption">🌲 始信峰 · 黄山三十六小峰之首</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🚡</span> 云谷索道上 → 玉屏索道下 <span class="warning-tag">注意末班</span></div>'''

new1 = '''<div class="quote">"五岳归来不看山，黄山归来不看岳。"<div class="quote-author">—— 徐霞客</div></div>
                
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🚡</span> 云谷索道上 → 玉屏索道下 <span class="warning-tag">注意末班</span></div>'''

c = c.replace(old1, new1)

# 始信峰图片移到描述之后
old2 = '''</div>
                </div>

                <img src="images/day7-shixinfeng.jpg" alt="始信峰黄山小峰" class="day-image" loading="lazy" onclick="openModal('day7', 2)">
                <div class="image-caption">🌲 始信峰 · 黄山三十六小峰之首</div>

                <img src="images/day7-guangmingding.jpg" alt="光明顶观景台" class="day-image" loading="lazy" onclick="openModal('day7', 3)">
                <div class="image-caption">✨ 光明顶 · 黄山第二高峰360度观景台</div>

                <img src="images/day7-yingkesong.jpg" alt="迎客松千年古松" class="day-image" loading="lazy" onclick="openModal('day7', 4)">
                <div class="image-caption">🌲 迎客松 · 千年古松，黄山标志</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏨</span> 下山回汤口酒店躺平</div>'''

new2 = '''</div>
                </div>

                <img src="images/黄山云海.jpg" alt="黄山云海翻涌" class="day-image" loading="lazy" onclick="openModal('day7', 0)">
                <div class="image-caption">☁️ 黄山云海 · 云海翻涌与松石画廊</div>

                <img src="images/黄山云海.jpg" alt="黄山云海松石" class="day-image" loading="lazy" onclick="openModal('day7', 1)">

                <img src="images/day7-shixinfeng.jpg" alt="始信峰黄山小峰" class="day-image" loading="lazy" onclick="openModal('day7', 2)">
                <div class="image-caption">🌲 始信峰 · 黄山三十六小峰之首</div>

                <img src="images/day7-guangmingding.jpg" alt="光明顶观景台" class="day-image" loading="lazy" onclick="openModal('day7', 3)">
                <div class="image-caption">✨ 光明顶 · 黄山第二高峰360度观景台</div>

                <img src="images/day7-yingkesong.jpg" alt="迎客松千年古松" class="day-image" loading="lazy" onclick="openModal('day7', 4)">
                <div class="image-caption">🌲 迎客松 · 千年古松，黄山标志</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏨</span> 下山回汤口酒店躺平</div>'''

c = c.replace(old2, new2)

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Day7 已修复")