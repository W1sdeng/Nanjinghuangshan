#!/usr/bin/env python3
# 从v15-final重新构建v16，不改变任何图片路径

with open(r'D:\nanjing\nanjing-v15-final.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 标题改为v16
content = content.replace('v15（完整优化版）', 'v16（动画增强版）')

# 2. 副标题添加精简行程
content = content.replace(
    '✨ v15版：精确时间安排 + 交通互斥 + 无障碍优化 + 平滑交互',
    '南京5天（秦淮→钟山→红山→博物院→铭记）+ 黄山3天（赴黄山→登顶→返程）\n                ✨ v16版：动画增强 + 滚动渐显'
)

# 3. 结语改为祝旅途愉快
old_conclusion = '''<div class="conclusion">
            <h2>旅行攻略总结</h2>
            <p>
                <strong>南京5天：</strong>Day1秦淮初探→Day2钟山+🌳梧桐大道→Day3红山/城墙二选一→Day4南博+总统府→Day5铭记历史+新城治愈<br><br>
                <strong>黄山3天：</strong>Day6赴黄山→Day7黄山一日游→Day8返程<br><br>
                ✨ v15版：精确时间安排 + 交通互斥 + 无障碍优化 + 平滑交互！
            </p>
        </div>'''

new_conclusion = '''<div class="conclusion">
            <h2>祝旅途愉快</h2>
            <p>愿你在南京的梧桐树下、黄山的云海中，找到属于自己的旅行节奏。</p>
        </div>'''

content = content.replace(old_conclusion, new_conclusion)

# 4. 页脚改为v16
content = content.replace('v15（完整优化版）', 'v16（动画增强版）')

# 5. 图片CSS改为原始比例显示
old_img_css = '''.day-image {
            width: 100%;
            height: 350px;
            object-fit: cover;'''

new_img_css = '''.day-image {
            width: 100%;
            height: auto;
            max-height: 500px;
            object-fit: contain;
            background: #f5f5f5;'''

content = content.replace(old_img_css, new_img_css)

# 6. 添加动画CSS
animation_css = '''
        /* v16 动画效果 */
        #home h1 { animation: fadeInUp 0.8s ease forwards; }
        #home h1 .stamp { animation: fadeInUp 0.8s ease 0.3s forwards; opacity: 0; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .day-label { background: linear-gradient(135deg, var(--main-purple), var(--accent-warm)); animation: gradientShift 3s ease infinite; background-size: 200% 200%; }
        @keyframes gradientShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        .day-image:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(122,134,193,0.3); }
        .back-to-top.visible { animation: bounceIn 0.5s ease; }
        @keyframes bounceIn { 0% { transform: scale(0.3); opacity: 0; } 50% { transform: scale(1.1); } 70% { transform: scale(0.9); } 100% { transform: scale(1); opacity: 1; } }
        .day-image.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s ease; }
        .day-image.reveal.visible { opacity: 1; transform: translateY(0); }
'''

style_end = content.find('</style>')
if style_end > 0:
    content = content[:style_end] + animation_css + content[style_end:]

# 7. 添加Intersection Observer
io_script = '''
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        imageObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            document.querySelectorAll('.day-image').forEach(img => {
                img.classList.add('reveal');
                imageObserver.observe(img);
            });
        });
    </script>
'''

body_end = content.rfind('</body>')
if body_end > 0:
    content = content[:body_end] + io_script + content[body_end:]

# 8. Day5改为上午自然醒，下午纪念馆
old_day5 = '''<li><strong>8:00-9:00</strong> 起床、洗漱</li>
                        <li><strong>9:00-9:45</strong> 早餐 + 前往纪念馆（地铁约30分钟）</li>
                        <li><strong>9:45-12:30</strong> 纪念馆（2.5h，保持肃穆）</li>
                        <li><strong>12:30-13:30</strong> 建邺万达午餐（调整情绪）</li>
                        <li><strong>13:30-14:00</strong> 前往新城区（地铁约15分钟）</li>
                        <li><strong>14:00-17:30</strong> 下午治愈三选一（3.5h）</li>'''

new_day5 = '''<li><strong>8:00-10:00</strong> 自然醒、懒散早餐</li>
                        <li><strong>10:00-12:00</strong> 上午自由活动（补觉/逛店/拍照）</li>
                        <li><strong>12:00-13:00</strong> 午餐</li>
                        <li><strong>13:00-13:30</strong> 前往纪念馆（地铁约30分钟）</li>
                        <li><strong>13:30-16:00</strong> 纪念馆（2.5h，保持肃穆）</li>
                        <li><strong>16:00-17:00</strong> 建邺万达晚餐（调整情绪）</li>'''

content = content.replace(old_day5, new_day5)

with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(content)

import os
print(f"v16重新构建完成! 文件大小: {os.path.getsize(r'D:\nanjing\nanjing-v16-complete.html')} bytes")