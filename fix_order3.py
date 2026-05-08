#!/usr/bin/env python3
import re

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Day2 南京大学 - 图片在描述之前，需要调整
old = '''<div class="day-images-grid">
                    <img src="images/南京大学鼓楼校区1.jpg" alt="南京大学北大楼" class="day-image" loading="lazy" onclick="openModal('day2', 4)">
                    <img src="images/南京大学鼓楼校区2.jpg" alt="南京大学校园秋色" class="day-image" loading="lazy" onclick="openModal('day2', 5)">
                    <div class="image-caption">🎓 南京大学鼓楼校区 · 北大楼爬藤墙与校园秋色（可选）</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🎓</span> 南京大学鼓楼校区 · 先锋书店</div>'''

new = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🎓</span> 南京大学鼓楼校区 · 先锋书店</div>'''

c = c.replace(old, new)

# 在南京大学描述后添加图片
old2 = '''</div>
            </div>
        </section>

        <!-- ==========================================
             Day3'''

new2 = '''</div>

                <div class="day-images-grid">
                    <img src="images/南京大学鼓楼校区1.jpg" alt="南京大学北大楼" class="day-image" loading="lazy" onclick="openModal('day2', 4)">
                    <img src="images/南京大学鼓楼校区2.jpg" alt="南京大学校园秋色" class="day-image" loading="lazy" onclick="openModal('day2', 5)">
                    <div class="image-caption">🎓 南京大学鼓楼校区 · 北大楼爬藤墙与校园秋色（可选）</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day3'''

c = c.replace(old2, new2)

# Day3: 鸡鸣寺 -> 台城城墙 -> 玄武湖 (城墙方案)
# 检查并修复

# 鸡鸣寺 - 当前是图片在描述之前
old3 = '''<img src="images/day3-jimingsi.jpg" alt="鸡鸣寺南朝四百八十寺" class="day-image" loading="lazy" onclick="openModal('day3', 1)">
                <div class="image-caption">🏯 鸡鸣寺 · 南朝四百八十寺之首</div>

                <img src="images/台城城墙1.jpg" alt="台城城墙俯瞰玄武湖" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 俯瞰玄武湖全景</div>

                <img src="images/台城城墙2.jpg" alt="台城城墙视角" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 城墙步道</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏰</span> 台城城墙 <span class="warning-tag">需门票</span></div>'''

new3 = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏯</span> 鸡鸣寺</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市玄武区鸡鸣寺路1号</p>
                        <p><span class="info-label">⏰ 开放时间：</span>7:00-17:30</p>
                        <p><span class="info-label">🎫 门票：</span>10元/人</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>1-1.5小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>最佳拍照点：药师佛塔拍紫峰大厦同框</li>
                            <li>傍晚时分光线极美，可拍日落</li>
                        </ul>
                    </div>
                </div>

                <img src="images/day3-jimingsi.jpg" alt="鸡鸣寺南朝四百八十寺" class="day-image" loading="lazy" onclick="openModal('day3', 1)">
                <div class="image-caption">🏯 鸡鸣寺 · 南朝四百八十寺之首</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏰</span> 台城城墙 <span class="warning-tag">需门票</span></div>'''

c = c.replace(old3, new3)

# 台城城墙后添加图片
old4 = '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>防晒</li><li>相机</li></ul>
                    </div>
                </div>

                <img src="images/台城城墙1.jpg" alt="台城城墙俯瞰玄武湖" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 俯瞰玄武湖全景</div>

                <img src="images/台城城墙2.jpg" alt="台城城墙视角" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 城墙步道</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌅</span> 玄武湖</div>'''

new4 = '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>防晒</li><li>相机</li></ul>
                    </div>
                </div>

                <img src="images/台城城墙1.jpg" alt="台城城墙俯瞰玄武湖" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 俯瞰玄武湖全景</div>

                <img src="images/台城城墙2.jpg" alt="台城城墙视角" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🏰 台城城墙 · 城墙步道</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌅</span> 玄武湖</div>'''

c = c.replace(old4, new4)

# 玄武湖后添加图片
old5 = '''</div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>推荐路线：从解放门进入 → 沿环湖路散步或骑行</li>
                            <li>💪 精力旺盛者可选夜骑：19:30从解放门出发，顺时针环湖约9km</li>
                            <li>最佳拍照点：环湖路看日落，樱洲看花海</li>
                        </ul>
                    </div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏯</span> 鸡鸣寺 → 台城城墙 → 玄武湖</div>'''

new5 = '''</div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>推荐路线：从解放门进入 → 沿环湖路散步或骑行</li>
                            <li>💪 精力旺盛者可选夜骑：19:30从解放门出发，顺时针环湖约9km</li>
                            <li>最佳拍照点：环湖路看日落，樱洲看花海</li>
                        </ul>
                    </div>
                </div>

                <img src="images/玄武湖1.jpg" alt="玄武湖夕阳" class="day-image" loading="lazy" onclick="openModal('day3', 3)">
                <div class="image-caption">🌅 玄武湖 · 金陵明珠，散步或骑行皆宜</div>

                <img src="images/玄武湖2.jpg" alt="玄武湖夜景" class="day-image" loading="lazy" onclick="openModal('day3', 3)">
                <div class="image-caption">🌙 玄武湖夜景 · 解放门段灯光最美</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏯</span> 鸡鸣寺 → 台城城墙 → 玄武湖</div>'''

c = c.replace(old5, new5)

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Day2 和 Day3 已修复")