#!/usr/bin/env python3
# 全面修复所有Day的图片和描述顺序

with open(r'D:\nanjing\nanjing-v16-complete.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Day1 甘熙宅第 - 交换顺序
c = c.replace(
    '''<img src="images/day1-ganxi.jpg" alt="甘熙宅第（九十九间半）" class="day-image" loading="lazy" onclick="openModal('day1', 0)">
                <div class="image-caption">🏛️ 甘熙宅第（九十九间半）· 金陵民居瑰宝</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 甘熙宅第（九十九间半）</div>''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 甘熙宅第（九十九间半）</div>'''
)

# 在甘熙宅第描述结束后添加图片
c = c.replace(
    '''</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏮</span> 老门东</div>''',
    '''</div>
                </div>

                <img src="images/day1-ganxi.jpg" alt="甘熙宅第（九十九间半）" class="day-image" loading="lazy" onclick="openModal('day1', 0)">
                <div class="image-caption">🏛️ 甘熙宅第（九十九间半）· 金陵民居瑰宝</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏮</span> 老门东</div>'''
)

# 夫子庙 - 在描述后添加秦淮河图片
c = c.replace(
    '''</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day2''',
    '''</div>
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
)

# Day2 明孝陵 - 交换顺序
c = c.replace(
    '''<div class="quote">"钟山龙蟠，石头虎踞，此帝王之宅也。"<div class="quote-author">—— 《太平御览》</div></div>
                
                <img src="images/明孝陵1.jpg" alt="明孝陵神道石像生" class="day-image" loading="lazy" onclick="openModal('day2', 0)">
                <div class="image-caption">🍂 明孝陵神道 · 六百年石像生</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🍂</span> 明孝陵 <span class="warning-tag">需预约</span></div>''',
    '''<div class="quote">"钟山龙蟠，石头虎踞，此帝王之宅也。"<div class="quote-author">—— 《太平御览》</div></div>
                
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🍂</span> 明孝陵 <span class="warning-tag">需预约</span></div>'''
)

# 明孝陵描述后添加图片
c = c.replace(
    '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>舒适步行鞋</li><li>相机</li><li>防晒</li></ul>
                    </div>
                </div>

                <img src="images/day2-zhongshanling.jpg" alt="中山陵祭堂"''',
    '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>舒适步行鞋</li><li>相机</li><li>防晒</li></ul>
                    </div>
                </div>

                <img src="images/明孝陵1.jpg" alt="明孝陵神道石像生" class="day-image" loading="lazy" onclick="openModal('day2', 0)">
                <div class="image-caption">🍂 明孝陵神道 · 六百年石像生</div>

                <img src="images/day2-zhongshanling.jpg" alt="中山陵祭堂"'''
)

# Day2 南京大学 - 交换顺序
c = c.replace(
    '''<div class="day-images-grid">
                    <img src="images/南京大学鼓楼校区1.jpg" alt="南京大学北大楼" class="day-image" loading="lazy" onclick="openModal('day2', 4)">
                    <img src="images/南京大学鼓楼校区2.jpg" alt="南京大学校园秋色" class="day-image" loading="lazy" onclick="openModal('day2', 5)">
                    <div class="image-caption">🎓 南京大学鼓楼校区 · 北大楼爬藤墙与校园秋色（可选）</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🎓</span> 南京大学鼓楼校区 · 先锋书店</div>''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🎓</span> 南京大学鼓楼校区 · 先锋书店</div>'''
)

# Day2 南京大学描述后添加图片
c = c.replace(
    '''</div>
            </div>
        </section>

        <!-- ==========================================
             Day3''',
    '''</div>

                <div class="day-images-grid">
                    <img src="images/南京大学鼓楼校区1.jpg" alt="南京大学北大楼" class="day-image" loading="lazy" onclick="openModal('day2', 4)">
                    <img src="images/南京大学鼓楼校区2.jpg" alt="南京大学校园秋色" class="day-image" loading="lazy" onclick="openModal('day2', 5)">
                    <div class="image-caption">🎓 南京大学鼓楼校区 · 北大楼爬藤墙与校园秋色（可选）</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day3'''
)

# Day3 - 鸡鸣寺需要添加完整描述
c = c.replace(
    '''<img src="images/day3-jimingsi.jpg" alt="鸡鸣寺南朝四百八十寺"''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
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

                <img src="images/day3-jimingsi.jpg" alt="鸡鸣寺南朝四百八十寺"'''
)

# Day4 博物院和总统府 - 检查并修复
c = c.replace(
    '''<img src="images/day4-bowuyuan.jpg" alt="南京博物院历史馆" class="day-image" loading="lazy" onclick="openModal('day4', 0)">
                <div class="image-caption">🏛️ 南京博物院 · 四大镇馆之宝</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 南京博物院 <span class="warning-tag">最难约</span></div>''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 南京博物院 <span class="warning-tag">最难约</span></div>'''
)

c = c.replace(
    '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>身份证</li><li>充电宝</li></ul>
                    </div>
                </div>

                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg"''',
    '''</div>
                    <div class="prepare-box">
                        <h4>🎒 准备物品</h4>
                        <ul><li>身份证</li><li>充电宝</li></ul>
                    </div>
                </div>

                <img src="images/day4-bowuyuan.jpg" alt="南京博物院历史馆" class="day-image" loading="lazy" onclick="openModal('day4', 0)">
                <div class="image-caption">🏛️ 南京博物院 · 四大镇馆之宝</div>

                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg"'''
)

# Day4 总统府 - 交换顺序
c = c.replace(
    '''<div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府民国中枢" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府子超楼" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府 · 民国中枢与江南园林交融</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 总统府 <span class="warning-tag">需预约</span></div>''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 总统府 <span class="warning-tag">需预约</span></div>'''
)

c = c.replace(
    '''</div>
            </div>
        </section>

        <!-- ==========================================
             Day5''',
    '''</div>

                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府民国中枢" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府子超楼" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府 · 民国中枢与江南园林交融</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day5'''
)

# Day5 纪念馆 - 已经有正确顺序，但需要添加图片
c = c.replace(
    '''<img src="images/侵华日军南京大屠杀遇难同胞纪念馆.jpg" alt="纪念馆以史为鉴" class="day-image" loading="lazy" onclick="openModal('day5', 0)">
                <div class="image-caption">🕊️ 侵华日军南京大屠杀遇难同胞纪念馆 · 以史为鉴 <span class="warning-tag">最难约TOP2</span></div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🕊️</span> 纪念馆 <span class="warning-tag">提前7天0点蹲守</span></div>''',
    '''<div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🕊️</span> 纪念馆 <span class="warning-tag">提前7天0点蹲守</span></div>'''
)

c = c.replace(
    '''</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏙️</span> 下午治愈三选一</div>''',
    '''</div>
                </div>

                <img src="images/侵华日军南京大屠杀遇难同胞纪念馆.jpg" alt="纪念馆以史为鉴" class="day-image" loading="lazy" onclick="openModal('day5', 0)">
                <div class="image-caption">🕊️ 侵华日军南京大屠杀遇难同胞纪念馆 · 以史为鉴 <span class="warning-tag">最难约TOP2</span></div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏙️</span> 下午治愈三选一</div>'''
)

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("全面修复完成!")