#!/usr/bin/env python3
import re

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Day4: 总统府
old = '''<div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府民国中枢" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府子超楼" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府 · 民国中枢与江南园林交融</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 总统府 <span class="warning-tag">需预约</span></div>'''

new = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 总统府 <span class="warning-tag">需预约</span></div>'''

c = c.replace(old, new)

# 在总统府描述后添加图片
old2 = '''</div>
            </div>
        </section>

        <!-- ==========================================
             Day5'''

new2 = '''</div>

                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府民国中枢" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府子超楼" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府 · 民国中枢与江南园林交融</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day5'''

c = c.replace(old2, new2)

# Day5: 纪念馆 -> 下午三选一
# 检查纪念馆结构

# Day5下午三选一图片在描述之前
old3 = '''<div class="day-images-grid">
                    <img src="images/梧桐大道3.jpg" alt="梧桐大道" class="day-image" loading="lazy" onclick="openModal('day5', 1)">
                    <img src="images/明孝陵2.jpg" alt="明孝陵秋色" class="day-image" loading="lazy" onclick="openModal('day5', 2)">
                    <div class="image-caption">🏙️ 南京新城/梧桐景色 · 下午三选一</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day6'''

new3 = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏙️</span> 下午治愈三选一</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">① 南京云锦博物馆：</span>免费，室内，安静华美</p>
                        <p><span class="info-label">② 南京眼步行桥+保利大剧院：</span>新城风貌，拍照圣地</p>
                        <p><span class="info-label">③ 河西金鹰世界/华采天地：</span>现代商场+晚餐</p>
                    </div>
                </div>

                <div class="day-images-grid">
                    <img src="images/梧桐大道3.jpg" alt="梧桐大道" class="day-image" loading="lazy" onclick="openModal('day5', 1)">
                    <img src="images/明孝陵2.jpg" alt="明孝陵秋色" class="day-image" loading="lazy" onclick="openModal('day5', 2)">
                    <div class="image-caption">🏙️ 南京新城/梧桐景色 · 下午三选一</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day6'''

c = c.replace(old3, new3)

# Day6: 汤口镇图片在描述之前
old4 = '''<div class="day-images-grid">
                    <img src="images/明孝陵1.jpg" alt="明孝陵秋色" class="day-image" loading="lazy" onclick="openModal('day6', 0)">
                    <img src="images/明孝陵2.jpg" alt="明孝陵石象路" class="day-image" loading="lazy" onclick="openModal('day6', 1)">
                    <div class="image-caption">🏨 汤口镇 · 黄山脚下休整（用南京景点图）</div>
                </div>
                <img src="images/明孝陵3.jpg" alt="明孝陵神道" class="day-image" loading="lazy" onclick="openModal('day6', 2)">
                <div class="image-caption">🏨 汤口镇 · 酒店周边（用南京景点图）</div>
            </div>
        </section>

        <!-- ==========================================
             Day7'''

new4 = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏨</span> 入住汤口镇</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📝 活动：</span>黄山脚下休整，晚上吃徽菜</p>
                    </div>
                </div>

                <div class="day-images-grid">
                    <img src="images/明孝陵1.jpg" alt="明孝陵秋色" class="day-image" loading="lazy" onclick="openModal('day6', 0)">
                    <img src="images/明孝陵2.jpg" alt="明孝陵石象路" class="day-image" loading="lazy" onclick="openModal('day6', 1)">
                    <div class="image-caption">🏨 汤口镇 · 黄山脚下休整（用南京景点图）</div>
                </div>
                <img src="images/明孝陵3.jpg" alt="明孝陵神道" class="day-image" loading="lazy" onclick="openModal('day6', 2)">
                <div class="image-caption">🏨 汤口镇 · 酒店周边（用南京景点图）</div>
            </div>
        </section>

        <!-- ==========================================
             Day7'''

c = c.replace(old4, new4)

# Day7: 光明顶、始信峰、迎客松 - 需要检查顺序

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Day4-6 已修复")