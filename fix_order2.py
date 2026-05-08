#!/usr/bin/env python3
import re

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Day1: 甘熙宅第
# 当前: 描述 -> 图片 -> 描述 -> 图片 -> 描述
# 目标: 描述 -> 图片 -> 描述 -> 图片 -> 描述 (但当前第一张图片在描述之前)

# 找甘熙宅第的描述末尾和图片开始
# 甘熙宅第描述结尾 </div></div> 后紧跟图片
# 这需要更复杂的处理

# 简化方法：直接搜索替换模式
# 模式1: attraction-card 后面紧跟 img 的情况
# 模式2: img 后面紧跟 attraction-card 的情况，需要交换

# 具体处理 Day1 的甘熙宅第：
# 当前: </div></div> (甘熙宅第描述结束) -> img -> caption -> 老门东描述
# 改为: </div></div> -> 老门东描述 -> img -> caption

# 由于这太复杂，让我用另一种方式 - 找到所有 img+attraction-card 对，插入描述到中间

# 先处理老门东 - 当前是 img 在描述之前
old = '''<img src="images/南京老门东.jpg" alt="老门东青石板路" class="day-image" loading="lazy" onclick="openModal('day1', 1)">
                <div class="image-caption">🏮 老门东 · 青石板路里的金陵味</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏮</span> 老门东</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市秦淮区箍桶巷</p>
                        <p><span class="info-label">⏰ 开放时间：</span>全天，商铺10:00-22:00</p>
                        <p><span class="info-label">🎫 门票：</span>免费</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>1.5-2小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：从明城墙步行10分钟到老门东，先逛主街再钻小巷</li>
                            <li>最佳拍照点：三条营巷子，青石板路+爬藤墙出片</li>
                            <li>避坑：入口排队小吃比巷子里贵30%，往里走</li>
                        </ul>
                    </div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>空肚子</li><li>手机支付</li><li>湿纸巾</li></ul>
                    </div>
                </div>

                <div class="day-images-grid">'''

new = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏮</span> 老门东</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市秦淮区箍桶巷</p>
                        <p><span class="info-label">⏰ 开放时间：</span>全天，商铺10:00-22:00</p>
                        <p><span class="info-label">🎫 门票：</span>免费</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>1.5-2小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：从明城墙步行10分钟到老门东，先逛主街再钻小巷</li>
                            <li>最佳拍照点：三条营巷子，青石板路+爬藤墙出片</li>
                            <li>避坑：入口排队小吃比巷子里贵30%，往里走</li>
                        </ul>
                    </div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>空肚子</li><li>手机支付</li><li>湿纸巾</li></ul>
                    </div>
                </div>

                <img src="images/南京老门东.jpg" alt="老门东青石板路" class="day-image" loading="lazy" onclick="openModal('day1', 1)">
                <div class="image-caption">🏮 老门东 · 青石板路里的金陵味</div>

                <div class="day-images-grid">'''

c = c.replace(old, new)

# 处理秦淮河
old2 = '''<div class="day-images-grid">
                    <img src="images/秦淮河夜游1.jpg" alt="秦淮河夜色桨声灯影" class="day-image" loading="lazy" onclick="openModal('day1', 2)">
                    <img src="images/秦淮河夜游2.jpg" alt="秦淮河灯火阑珊" class="day-image" loading="lazy" onclick="openModal('day1', 3)">
                    <div class="image-caption">🌙 秦淮河夜色 · 桨声灯影里的金陵梦</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌙</span> 夫子庙 · 秦淮河夜游</div>'''

new2 = '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌙</span> 夫子庙 · 秦淮河夜游</div>'''

c = c.replace(old2, new2)

# 在夫子庙描述后添加秦淮河图片
old3 = '''</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day2'''

new3 = '''</div>
                </div>

                <div class="day-images-grid">
                    <img src="images/秦淮河夜游1.jpg" alt="秦淮河夜色桨声灯影" class="day-image" loading="lazy" onclick="openModal('day1', 2)">
                    <img src="images/秦淮河夜游2.jpg" alt="秦淮河灯火阑珊" class="day-image" loading="lazy" onclick="openModal('day1', 3)">
                    <div class="image-caption">🌙 秦淮河夜色 · 桨声灯影里的金陵梦</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day2'''

c = c.replace(old3, new3)

# Day2: 明孝陵 -> 中山陵 -> 音乐台 -> 梧桐大道 -> 南京大学
# 当前是: 描述 -> 图片 -> 描述 -> 图片 -> 描述 -> 图片...

# 检查Day2的结构并修复

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Day1 已修复")