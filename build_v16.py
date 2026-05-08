#!/usr/bin/env python3
# 构建v16版本 - 基于v15-final添加所有修改

import re
import os

# 读取v15-final
with open(r'D:\nanjing\nanjing-v15-final.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改标题为v16
content = content.replace('v15（完整优化版）', 'v16（动画增强版）')

# 2. 图片路径映射表 (英文 -> 中文)
image_map = {
    'day1-ganxi.jpg': '甘熙宅第.jpg',
    'day1-laomentong.jpg': '南京老门东.jpg',
    'day1-qinhuai1.jpg': '秦淮河夜游1.jpg',
    'day1-qinhuai2.jpg': '秦淮河夜游2.jpg',
    'day2-wutong1.jpg': '中山陵3.jpg',
    'day2-wutong2.jpg': '中山陵3.jpg',
    'day2-nanda1.jpg': '南京大学鼓楼校区1.jpg',
    'day2-nanda2.jpg': '南京大学鼓楼校区2.jpg',
    'day2-zhongshanling.jpg': '中山陵3.jpg',
    'day3-hongshan.jpg': '红山动物园1.jpg',
    'day3-jimingsi.jpg': '鸡鸣寺.jpg',
    'day4-bowuyuan.jpg': '博物院1.jpg',
    'day4-zongtong1.jpg': '南京总统府1.jpg',
    'day4-zongtong2.jpg': '南京总统府2.jpg',
    'day5-nanjing-eye1.jpg': '南京眼步行桥.jpg',
    'day5-baoli-theatre.jpg': '保利大剧院.jpg',
    'day6-tangkou1.jpg': '汤口镇1.jpg',
    'day6-tangkou2.jpg': '汤口镇2.jpg',
    'day6-tangkou3.jpg': '汤口镇3.jpg',
    'day7-guangmingding.jpg': '光明顶.jpg',
    'day7-shixinfeng.jpg': '始信峰.jpg',
    'day7-yingkesong.jpg': '迎客松.jpg',
}

# 应用图片路径替换
for old_name, new_name in image_map.items():
    content = content.replace(f'images/{old_name}', f'images/{new_name}')

# 3. 纪念馆重命名
content = content.replace('纪念馆1.jpg', '侵华日军南京大屠杀遇难同胞纪念馆1.jpg')
content = content.replace('纪念馆2.jpg', '侵华日军南京大屠杀遇难同胞纪念馆2.jpg')
content = content.replace('>纪念馆<', '>侵华日军南京大屠杀遇难同胞纪念馆<')

# 4. 在</style>之前添加动画CSS
animation_css = '''
        /* ==========================================
           v16 新增动画效果
           ========================================== */
        
        /* 封面水墨背景 */
        #home {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
            position: relative;
            overflow: hidden;
        }
        #home::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at 30% 70%, rgba(122,134,193,0.08) 0%, transparent 50%),
                        radial-gradient(circle at 70% 30%, rgba(107,159,143,0.08) 0%, transparent 50%);
            animation: inkFlow 20s ease-in-out infinite;
        }
        @keyframes inkFlow {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            50% { transform: translate(-5%, -5%) rotate(5deg); }
        }
        
        /* 标题淡入动画 */
        #home h1 {
            animation: titleFadeIn 1.2s ease-out forwards;
            opacity: 0;
        }
        @keyframes titleFadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        /* 印章弹跳动画 */
        #home h1 .stamp {
            animation: stampBounce 0.6s ease-out 0.8s forwards;
            opacity: 0;
            transform: rotate(-5deg) scale(0.5);
        }
        @keyframes stampBounce {
            0% { opacity: 0; transform: rotate(-5deg) scale(0.5); }
            50% { transform: rotate(-5deg) scale(1.1); }
            100% { opacity: 1; transform: rotate(-5deg) scale(1); }
        }
        
        /* 诗句引号装饰 */
        .quote::before, .quote::after {
            font-family: 'Times New Roman', serif;
            font-size: 2em;
            color: var(--main-purple);
            opacity: 0.3;
            position: absolute;
        }
        .quote::before {
            content: '"';
            left: -5px;
            top: -5px;
        }
        .quote::after {
            content: '"';
            right: -5px;
            bottom: -15px;
        }
        .quote {
            position: relative;
            padding: 15px 25px;
        }
        
        /* 图片hover发光效果 */
        .day-image {
            transition: all 0.4s ease;
        }
        .day-image:hover {
            box-shadow: 0 0 25px rgba(122,134,193,0.5), 0 8px 20px rgba(0,0,0,0.15);
            transform: scale(1.02);
        }
        
        /* Day标签渐变动画 */
        .day-label {
            background: linear-gradient(135deg, var(--main-purple), var(--accent-warm));
            animation: labelGradient 3s ease infinite;
            background-size: 200% 200%;
        }
        @keyframes labelGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* 按钮波纹效果 */
        .enter-btn, .nav-btn, .tab-item, .category-btn {
            position: relative;
            overflow: hidden;
        }
        .enter-btn::after, .nav-btn::after, .tab-item::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.3s, height 0.3s;
        }
        .enter-btn:active::after, .nav-btn:active::after {
            width: 200px;
            height: 200px;
        }
        
        /* 交通卡片箭头滑动 */
        .transport-card::after {
            content: '›';
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.5em;
            color: var(--transport-orange);
            transition: transform 0.3s ease;
        }
        .transport-card:not(.collapsed)::after {
            transform: translateY(-50%) rotate(90deg);
        }
        
        /* 回到顶部弹跳 */
        .back-to-top {
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        .back-to-top:hover {
            transform: scale(1.1);
        }
        .back-to-top.visible {
            animation: bounceIn 0.5s ease;
        }
        @keyframes bounceIn {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.1); }
            70% { transform: scale(0.9); }
            100% { transform: scale(1); opacity: 1; }
        }
        
        /* 图片滚动渐变显示 - 初始状态 */
        .day-image.reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }
        .day-image.reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

'''

# 找到</style>位置插入动画CSS
style_end = content.find('</style>')
if style_end > 0:
    content = content[:style_end] + animation_css + content[style_end:]

# 5. 在</body>之前添加Intersection Observer JavaScript
io_js = '''
    <!-- v16 新增: 图片滚动渐变效果 -->
    <script>
        // Intersection Observer for image reveal
        document.addEventListener('DOMContentLoaded', function() {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                root: null,
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });
            
            // 为所有day-image添加reveal类并观察
            document.querySelectorAll('.day-image').forEach(img => {
                img.classList.add('reveal');
                imageObserver.observe(img);
            });
            
            // 为day-card添加渐入效果
            const cardObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            
            document.querySelectorAll('.day-card, .public-section').forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                cardObserver.observe(card);
            });
        });
    </script>
'''

body_end = content.rfind('</body>')
if body_end > 0:
    content = content[:body_end] + io_js + content[body_end:]

# 写入v16文件
with open(r'D:\nanjing\nanjing-v16-complete.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("v16构建完成!")
print(f"文件大小: {os.path.getsize(r'D:\nanjing\nanjing-v16-complete.html')} bytes")