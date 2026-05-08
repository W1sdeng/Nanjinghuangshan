import os

# 基于v12代码创建完整优化版v15
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>南京黄山之旅｜宁黄八日记 v15（完整优化版）</title>
    <link href="https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
    <style>
        /* ==========================================
           全局变量 - 圆周旅迹低饱和莫兰迪配色
           ========================================== */
        :root {
            --main-purple: #7a86c1;
            --main-green: #6b9f8f;
            --accent-warm: #c9a96e;
            --accent-coral: #d49b8b;
            --transport-orange: #ff9800;
            --tips-blue: #3f51b5;
            --prepare-yellow: #ffc107;
            --info-blue: #2196f3;
            --emergency-red: #f44336;
            --hotel-orange: #e65100;
            --bg-light: #f8f9fa;
            --card-bg: #ffffff;
            --text-main: #333333;
            --text-sub: #666666;
            --text-light: #8c7b6f;
            --shadow-light: 0 4px 12px rgba(0,0,0,0.08);
            --shadow-medium: 0 8px 24px rgba(0,0,0,0.12);
            --radius-large: 20px;
            --radius-medium: 16px;
            --radius-small: 12px;
            --transition-fast: 0.2s ease;
            --transition-normal: 0.3s ease;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            line-height: 1.8; color: var(--text-main);
            background: var(--bg-light); padding-bottom: 80px; overflow-x: hidden;
        }

        /* 打印优化 */
        @media print {
            .top-nav, .bottom-tab, .back-to-top, .enter-btn, .modal, .print-btn { display: none !important; }
            .section { display: block !important; page-break-inside: avoid; }
            .day-card, .public-section { box-shadow: none; border: 1px solid #eee; }
            .transport-card .transport-detail { display: block !important; }
        }
        body.printing .top-nav, body.printing .bottom-tab, body.printing .back-to-top, body.printing .enter-btn { display: none; }

        /* 顶部导航 */
        .top-nav {
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
            padding: 12px 15px; display: flex; gap: 8px; overflow-x: auto;
            box-shadow: var(--shadow-light); scrollbar-width: none;
        }
        .top-nav::-webkit-scrollbar { display: none; }
        .nav-btn {
            flex-shrink: 0; padding: 8px 16px; border: none; border-radius: 20px;
            background: var(--bg-light); color: var(--text-sub); font-size: 0.9em;
            cursor: pointer; transition: var(--transition-normal); white-space: nowrap;
        }
        .nav-btn:hover { background: #e8eaf6; }
        .nav-btn.active { background: var(--main-purple); color: white; box-shadow: 0 4px 12px rgba(122,134,193,0.3); }
        .nav-btn.home-btn { background: var(--main-green); color: white; }
        .nav-btn:active { transform: scale(0.97); }

        /* 底部Tab栏 */
        .bottom-tab {
            position: fixed; bottom: 0; left: 0; right: 0; z-index: 1000;
            background: rgba(255,255,255,0.98); backdrop-filter: blur(10px);
            display: flex; justify-content: flex-start; padding: 10px 5px;
            box-shadow: 0 -4px 12px rgba(0,0,0,0.08); overflow-x: auto;
            scrollbar-width: none; -webkit-overflow-scrolling: touch;
        }
        .bottom-tab::-webkit-scrollbar { display: none; }
        .tab-item {
            display: flex; flex-direction: column; align-items: center; gap: 2px;
            border: none; background: none; color: var(--text-light); font-size: 0.75em;
            cursor: pointer; transition: var(--transition-normal); padding: 5px 10px;
            flex-shrink: 0; position: relative;
        }
        .tab-item.active { color: var(--main-purple); }
        .tab-item.active::after {
            content: ''; position: absolute; bottom: 2px; left: 50%;
            transform: translateX(-50%); width: 6px; height: 6px;
            background: var(--main-purple); border-radius: 50%;
        }
        .tab-icon { font-size: 1.3em; }
        .tab-text { font-size: 0.85em; }
        .tab-item:active { transform: scale(0.95); }
        .tab-item:focus-visible, .nav-btn:focus-visible { outline: 2px solid var(--main-purple); outline-offset: 2px; }

        /* 内容容器 */
        .content-container { max-width: 1100px; margin: 80px auto 0; padding: 0 15px; }
        .section { display: none; animation: fadeIn 0.4s ease; }
        .section.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* 封面页 */
        #home {
            text-align: center; padding: 100px 20px 80px;
            background: var(--card-bg); border-radius: var(--radius-large);
            margin-bottom: 20px; box-shadow: var(--shadow-light); position: relative;
        }
        #home h1 {
            font-family: 'Ma Shan Zheng', 'ZCOOL XiaoWei', 'STKaiti', 'KaiTi', '楷体', serif;
            font-size: 3em; font-weight: 400; color: var(--main-purple);
            letter-spacing: 4px; margin-bottom: 10px; line-height: 1.3;
        }
        #home h1 .stamp {
            display: inline-block; border: 2px solid var(--accent-coral);
            color: var(--accent-coral); padding: 4px 12px; font-size: 0.5em;
            letter-spacing: 2px; transform: rotate(-5deg);
            margin-left: 10px; position: relative; top: -10px; border-radius: 4px;
        }
        #home .subtitle { font-size: 1.1em; color: var(--text-sub); line-height: 1.8; margin-top: 15px; }
        .enter-btn {
            margin-top: 40px; padding: 12px 40px; border: none; border-radius: 25px;
            background: var(--accent-coral); color: white; font-size: 1em; cursor: pointer;
            transition: var(--transition-normal); box-shadow: 0 4px 12px rgba(212,155,139,0.3);
        }
        .enter-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(212,155,139,0.4); }
        .enter-btn:active { transform: scale(0.97); }
        .print-btn {
            position: fixed; top: 20px; right: 20px; z-index: 1001;
            padding: 8px 16px; border: none; border-radius: 20px;
            background: var(--accent-warm); color: white; font-size: 0.9em; cursor: pointer;
            transition: var(--transition-normal);
        }
        .print-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(201,169,110,0.4); }

        /* 每日行程卡片 */
        .day-card {
            background: var(--card-bg); border-radius: var(--radius-large);
            padding: 30px; margin-bottom: 20px; box-shadow: var(--shadow-light);
            transition: var(--transition-normal); position: relative;
        }
        .day-card:hover { transform: translateY(-3px); box-shadow: 0 12px 28px rgba(122,134,193,0.15); }
        .day-header {
            display: flex; align-items: center; margin-bottom: 20px;
            padding-bottom: 15px; border-bottom: 1px solid #eee;
        }
        .day-label {
            background: linear-gradient(135deg, var(--main-purple), var(--accent-warm));
            color: white; padding: 8px 20px; border-radius: 20px;
            font-size: 1em; font-weight: 500; margin-right: 15px;
        }
        .day-date { color: var(--text-sub); font-size: 0.9em; }
        .weather-icon { margin-left: 10px; font-size: 1.2em; }
        .quote {
            font-size: 1.2em; color: var(--text-sub); font-style: italic;
            margin: 20px 0; padding-left: 20px;
            border-left: 3px solid var(--main-purple); line-height: 1.6;
        }
        .quote-author { text-align: right; color: var(--text-light); font-size: 0.9em; margin-top: 8px; font-style: normal; }

        /* 景点图片 */
        .day-image {
            width: 100%; height: 350px; object-fit: cover; border-radius: var(--radius-medium);
            margin: 20px 0; box-shadow: var(--shadow-light); cursor: pointer;
            transition: var(--transition-normal);
        }
        .day-image:hover { transform: scale(1.008); box-shadow: 0 12px 28px rgba(0,0,0,0.18); }
        .image-caption { text-align: center; color: var(--text-light); font-size: 0.85em; margin-top: -15px; margin-bottom: 15px; }

        /* 图片两列布局 */
        @media (min-width: 769px) {
            .day-images-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
            .day-images-grid .day-image { height: 300px; margin: 0; }
            .day-images-grid .image-caption { grid-column: 1 / -1; margin-top: 5px; }
        }

        /* 景点卡片 */
        .attraction-card {
            background: #f8f9fa; border-radius: var(--radius-medium); padding: 20px;
            margin: 15px 0; border-left: 3px solid var(--main-purple); cursor: pointer;
            transition: var(--transition-normal);
        }
        .attraction-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
        .attraction-card.collapsed .attraction-detail { display: none; }
        .attraction-title { font-size: 1.2em; color: var(--text-main); font-weight: 500; display: flex; align-items: center; gap: 8px; }
        .attraction-detail { margin-top: 15px; color: var(--text-sub); line-height: 1.8; }
        .info-label { font-weight: 500; color: var(--main-purple); margin-right: 5px; }

        /* 交通卡片 - 互斥逻辑 */
        .transport-card {
            background: #fff8f0; border-radius: var(--radius-medium); padding: 18px;
            margin: 15px 0; border-left: 3px solid var(--transport-orange); cursor: pointer;
            transition: var(--transition-normal);
        }
        .transport-card:hover { box-shadow: 0 4px 12px rgba(255,152,0,0.1); }
        .transport-card.collapsed .transport-detail { display: none; }
        .transport-detail { margin-top: 12px; color: var(--text-sub); line-height: 1.8; }
        .transport-detail p { padding: 3px 0; }
        .transport-summary {
            margin-top: 10px; padding-top: 10px; border-top: 1px dashed #ddd;
            font-weight: 500; color: var(--transport-orange);
        }

        .warning-tag {
            display: inline-block; background: #fff3e0; color: #e65100;
            padding: 2px 8px; border-radius: 10px; font-size: 0.85em; font-weight: 500; margin-left: 5px;
        }

        /* 老玩家Tips */
        .old-tips {
            background: #f0f4ff; border-left: 3px solid var(--tips-blue); padding: 15px;
            margin: 15px 0; border-radius: var(--radius-small);
        }
        .old-tips h4 { color: var(--tips-blue); margin-bottom: 8px; font-size: 1em; }
        .old-tips ul { list-style: none; padding-left: 0; }
        .old-tips li { padding: 4px 0; font-size: 0.95em; padding-left: 20px; position: relative; }
        .old-tips li:before { content: "🔍"; position: absolute; left: 0; }

        /* 准备/提示卡片 */
        .prepare-box {
            background: #fff8e1; border-left: 3px solid var(--prepare-yellow); padding: 15px;
            margin: 15px 0; border-radius: var(--radius-small);
        }
        .prepare-box h4 { color: #f57c00; margin-bottom: 8px; font-size: 1em; }
        .prepare-box ul { list-style: none; padding-left: 0; }
        .prepare-box li { padding: 4px 0; padding-left: 20px; position: relative; font-size: 0.95em; }
        .prepare-box li:before { content: "✓"; position: absolute; left: 0; color: var(--prepare-yellow); font-weight: bold; }

        .tips-box {
            background: #e3f2fd; border-left: 3px solid var(--info-blue); padding: 15px;
            margin: 15px 0; border-radius: var(--radius-small);
        }
        .tips-box h4 { color: #1976d2; margin-bottom: 8px; font-size: 1em; }
        .tips-box ul { list-style: none; padding-left: 0; }
        .tips-box li { padding: 4px 0; padding-left: 20px; position: relative; font-size: 0.95em; }
        .tips-box li:before { content: "💡"; position: absolute; left: 0; }

        /* 公共板块 */
        .public-section {
            background: var(--card-bg); border-radius: var(--radius-large);
            padding: 30px; margin-bottom: 20px; box-shadow: var(--shadow-light);
            transition: var(--transition-normal);
        }
        .public-section:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
        .public-title {
            font-size: 1.8em; color: var(--main-green); font-weight: 400;
            margin-bottom: 20px; padding-left: 15px; border-left: 3px solid var(--main-green);
        }
        .public-card {
            background: #f8f9fa; border-radius: var(--radius-medium); padding: 20px;
            margin: 15px 0; transition: var(--transition-normal);
        }
        .public-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        .public-card h4 { color: var(--main-purple); margin-bottom: 10px; font-size: 1.1em; }
        .public-card ul { list-style: none; padding-left: 0; }
        .public-card li { padding: 6px 0; color: var(--text-sub); line-height: 1.8; }
        .sub-label {
            font-size: 0.8em; color: var(--accent-warm); font-weight: 500;
            display: inline-block; margin-right: 8px; min-width: 60px;
        }

        /* 行李清单 */
        .category-btns { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
        .category-btn {
            padding: 8px 16px; border: 1px solid #ddd; border-radius: 20px;
            background: white; color: var(--text-sub); cursor: pointer; font-size: 0.9em;
            transition: var(--transition-normal);
        }
        .category-btn.active { background: var(--main-purple); color: white; border-color: var(--main-purple); }
        .category-btn:active { transform: scale(0.96); }
        .category-list { display: none; }
        .category-list.active { display: block; }
        .checklist { list-style: none; padding-left: 0; }
        .checklist li {
            padding: 8px 0; display: flex; align-items: center; gap: 10px;
            border-bottom: 1px solid #eee;
        }
        .checklist input[type="checkbox"] { width: 18px; height: 18px; accent-color: var(--main-purple); cursor: pointer; }

        /* 应急联系卡 */
        .emergency-card {
            background: #ffebee; border-radius: var(--radius-medium); padding: 20px;
            margin: 15px 0; border-left: 3px solid var(--emergency-red);
        }
        .emergency-card h4 { color: #d32f2f; margin-bottom: 10px; }
        .emergency-card ul { list-style: none; padding-left: 0; }
        .emergency-card li { padding: 4px 0; color: var(--text-sub); }

        /* 酒店状态标签 */
        .booking-status {
            display: inline-block; padding: 2px 10px; border-radius: 10px;
            font-size: 0.85em; font-weight: 500; cursor: pointer; transition: var(--transition-fast);
        }
        .booking-status.pending { background: #fff3e0; color: var(--hotel-orange); }
        .booking-status.booked { background: #e8f5e9; color: #2e7d32; }

        /* 图片模态框 */
        .modal {
            display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.9); z-index: 2000;
            justify-content: center; align-items: center; padding: 20px;
        }
        .modal.active { display: flex; }
        .modal-img { max-width: 95%; max-height: 90vh; border-radius: var(--radius-medium); box-shadow: 0 0 0 4px rgba(255,255,255,0.2); transition: transform 0.3s ease; }
        .modal-close {
            position: absolute; top: 20px; right: 20px; color: white; font-size: 2.5em;
            cursor: pointer; border: none; background: rgba(255,255,255,0.2);
            width: 50px; height: 50px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            transition: var(--transition-fast); aria-label: "关闭图片";
        }
        .modal-close:hover { background: rgba(255,255,255,0.4); }
        .modal-arrow {
            position: absolute; top: 50%; transform: translateY(-50%);
            color: white; font-size: 2em; cursor: pointer; border: none; background: none; padding: 10px;
        }
        .modal-arrow.left { left: 20px; }
        .modal-arrow.right { right: 20px; }

        /* 回到顶部按钮 */
        .back-to-top {
            position: fixed; bottom: 90px; right: 20px;
            width: 45px; height: 45px; border-radius: 50%;
            background: var(--main-purple); color: white; border: none;
            font-size: 1.1em; cursor: pointer; box-shadow: var(--shadow-medium);
            transition: opacity 0.3s ease, transform 0.3s ease;
            opacity: 0; visibility: hidden; z-index: 999;
        }
        .back-to-top.visible { opacity: 1; visibility: visible; }
        .back-to-top:hover { transform: scale(1.1); background: var(--accent-coral); }

        /* 结语 */
        .conclusion {
            text-align: center; padding: 60px 30px; background: var(--card-bg);
            border-radius: var(--radius-large); margin-top: 30px; box-shadow: var(--shadow-light);
        }
        .conclusion h2 { font-size: 1.8em; color: var(--text-main); font-weight: 400; margin-bottom: 20px; }
        .conclusion p { color: var(--text-sub); line-height: 2; max-width: 700px; margin: 0 auto; }
        .footer { text-align: center; padding: 30px 15px; color: var(--text-light); font-size: 0.9em; }

        /* 响应式 */
        @media (max-width: 768px) {
            #home h1 { font-size: 2.2em; }
            .day-card { padding: 20px; }
            .day-image { height: 250px; }
            .day-header { flex-direction: column; align-items: flex-start; gap: 10px; }
            .public-section { padding: 20px; }
            .category-btns { justify-content: center; }
        }
        @media (max-width: 480px) {
            #home { padding: 80px 15px 60px; }
            #home h1 { font-size: 1.8em; }
            .day-image { height: 200px; }
            .modal-arrow { font-size: 1.5em; }
            .modal-arrow.left { left: 10px; }
            .modal-arrow.right { right: 10px; }
        }

        /* 暗黑模式 */
        @media (prefers-color-scheme: dark) {
            body { background: #1a1a2e; color: #e0e0e0; }
            .day-card, .public-section, #home { background: #2a2a3e; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
            .attraction-card, .public-card, .transport-card { background: #333350; }
            .old-tips { background: #2a2a40; }
            .prepare-box { background: #2a2a30; }
            .tips-box { background: #2a303a; }
            .transport-card { background: #2a2a20; border-left-color: #ff9800; }
            .transport-detail { color: #ccc; }
            .top-nav, .bottom-tab { background: rgba(30,30,50,0.95); }
            .nav-btn { background: #333350; color: #ccc; }
            .category-btn { background: #333350; color: #ccc; border-color: #555; }
            .checklist li { border-bottom-color: #444; }
            :root { --text-main: #e0e0e0; --text-sub: #bbb; --text-light: #999; }
            .booking-status.pending { background: #3a2a10; color: #ff9800; }
        }
    </style>
</head>
<body>
    <button class="print-btn" onclick="printItinerary()" aria-label="打印行程">打印行程</button>

    <!-- 顶部导航 -->
    <div class="top-nav">
        <button class="nav-btn home-btn active" onclick="showSection('home')" aria-label="首页">首页</button>
        <button class="nav-btn" onclick="showSection('day1')" aria-label="Day1">Day1🚣‍♀️</button>
        <button class="nav-btn" onclick="showSection('day2')" aria-label="Day2">Day2🏛️</button>
        <button class="nav-btn" onclick="showSection('day3')" aria-label="Day3">Day3🦁</button>
        <button class="nav-btn" onclick="showSection('day4')" aria-label="Day4">Day4🏘️</button>
        <button class="nav-btn" onclick="showSection('day5')" aria-label="Day5">Day5🕊️</button>
        <button class="nav-btn" onclick="showSection('day6')" aria-label="Day6">Day6🚄</button>
        <button class="nav-btn" onclick="showSection('day7')" aria-label="Day7">Day7⛰️</button>
        <button class="nav-btn" onclick="showSection('day8')" aria-label="Day8">Day8🌿</button>
    </div>

    <!-- 底部Tab栏 -->
    <div class="bottom-tab">
        <button class="tab-item active" data-tab="itinerary" onclick="switchTab('itinerary')" aria-label="行程">
            <span class="tab-icon">📅</span><span class="tab-text">行程</span>
        </button>
        <button class="tab-item" data-tab="food" onclick="switchTab('food')" aria-label="吃喝逛">
            <span class="tab-icon">🍜</span><span class="tab-text">吃喝逛</span>
        </button>
        <button class="tab-item" data-tab="hotel" onclick="switchTab('hotel')" aria-label="住宿">
            <span class="tab-icon">🏨</span><span class="tab-text">住宿</span>
        </button>
        <button class="tab-item" data-tab="luggage" onclick="switchTab('luggage')" aria-label="清单">
            <span class="tab-icon">🎒</span><span class="tab-text">清单</span>
        </button>
        <button class="tab-item" data-tab="avoid" onclick="switchTab('avoid')" aria-label="须知">
            <span class="tab-icon">⚠️</span><span class="tab-text">须知</span>
        </button>
        <button class="tab-item" data-tab="booking" onclick="switchTab('booking')" aria-label="预约">
            <span class="tab-icon">📝</span><span class="tab-text">预约</span>
        </button>
        <button class="tab-item" data-tab="emergency" onclick="switchTab('emergency')" aria-label="应急">
            <span class="tab-icon">🆘</span><span class="tab-text">应急</span>
        </button>
    </div>

    <div class="content-container">
        <!-- 封面页 -->
        <section id="home" class="section active">
            <h1>南京黄山之旅<span class="stamp">宁黄八记</span></h1>
            <div class="subtitle">
                8天7晚 · 南京5天+黄山3天<br>
                不特种兵 · 无回头路 · 全预约攻略<br>
                ✨ v15版：精确时间安排 + 交通互斥 + 无障碍 + 平滑交互
            </div>
            <button class="enter-btn" onclick="enterItinerary()">进入行程</button>
        </section>

        <!-- Day1 -->
        <section id="day1" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day1</div>
                    <div class="day-date">下午3:00后 · 秦淮初探 <span class="weather-icon">☀️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day1 精确时间安排（抵达日）</h4>
                    <ul>
                        <li><strong>14:00-15:00</strong> 酒店入住、放行李</li>
                        <li><strong>15:00-15:15</strong> 酒店 → 甘熙宅第（步行10分钟）</li>
                        <li><strong>15:15-16:45</strong> 甘熙宅第（1.5h）</li>
                        <li><strong>16:45-17:00</strong> 甘熙宅第 → 老门东（步行10分钟）</li>
                        <li><strong>17:00-19:00</strong> 老门东（逛吃2h）</li>
                        <li><strong>19:00-19:15</strong> 老门东 → 夫子庙（步行15分钟）</li>
                        <li><strong>19:15-21:30</strong> 夫子庙 + 秦淮河夜游（2h）</li>
                        <li><strong>21:30</strong> 返回酒店</li>
                    </ul>
                </div>
                <div class="quote">"烟笼寒水月笼沙，夜泊秦淮近酒家。"<div class="quote-author">—— 杜牧《泊秦淮》</div></div>
                <img src="images/day1-ganxi.jpg" alt="甘熙宅第" class="day-image" loading="lazy" onclick="openModal('day1', 0)">
                <div class="image-caption">🏛️ 甘熙宅第（九十九间半）· 金陵民居瑰宝</div>
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 甘熙宅第（九十九间半）</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市秦淮区南捕厅15号</p>
                        <p><span class="info-label">⏰ 开放时间：</span>9:00-17:00</p>
                        <p><span class="info-label">🎫 门票：</span>25元/人</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：从老门东步行10分钟，重点看南捕厅、津逮楼</li>
                            <li>最佳拍照点：砖雕门楼、后花园假山池塘</li>
                        </ul>
                    </div>
                </div>
                <img src="images/day1-laomendong.jpg" alt="老门东" class="day-image" loading="lazy" onclick="openModal('day1', 1)">
                <div class="image-caption">🏮 老门东 · 青石板路里的金陵味</div>
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏮</span> 老门东</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市秦淮区箍桶巷</p>
                        <p><span class="info-label">⏰ 开放时间：</span>全天，商铺10:00-22:00</p>
                        <p><span class="info-label">🎫 门票：</span>免费</p>
                    </div>
                </div>
                <div class="day-images-grid">
                    <img src="images/day1-qinhuai1.jpg" alt="秦淮河" class="day-image" loading="lazy" onclick="openModal('day1', 2)">
                    <img src="images/day1-qinhuai2.jpg" alt="秦淮河" class="day-image" loading="lazy" onclick="openModal('day1', 3)">
                    <div class="image-caption">🌙 秦淮河夜色 · 桨声灯影里的金陵梦</div>
                </div>
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌙</span> 夫子庙 · 秦淮河夜游</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市秦淮区贡院街</p>
                        <p><span class="info-label">⏰ 开放时间：</span>街区全天</p>
                        <p><span class="info-label">🎫 门票：</span>街区免费</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Day2 -->
        <section id="day2" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day2</div>
                    <div class="day-date">钟山访古 · 梧桐漫步 <span class="weather-icon">⛅️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day2 精确时间安排（钟山精华日）</h4>
                    <ul>
                        <li><strong>8:00-10:30</strong> 酒店 → 明孝陵</li>
                        <li><strong>10:30-13:00</strong> 明孝陵（2.5h）</li>
                        <li><strong>13:00-13:30</strong> 明孝陵 → 中山陵</li>
                        <li><strong>14:00-16:30</strong> 中山陵 + 音乐台（2.5h）</li>
                        <li><strong>16:30-17:00</strong> 中山陵 → 颐和路</li>
                        <li><strong>17:00-18:30</strong> 梧桐大道（1.5h）</li>
                    </ul>
                </div>
                <div class="quote">"钟山龙蟠，石头虎踞。"<div class="quote-author">—— 《太平御览》</div></div>
                <img src="images/day2-mingxiaoling.jpg" alt="明孝陵" class="day-image" loading="lazy" onclick="openModal('day2', 0)">
                <div class="image-caption">🍂 明孝陵神道 · 六百年石像生</div>
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>👑</span> 明孝陵</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>70元/人</p>
                    </div>
                </div>
                <img src="images/day2-zhongshanling.jpg" alt="中山陵" class="day-image" loading="lazy" onclick="openModal('day2', 1)">
                <div class="image-caption">🏛️ 中山陵 · 音乐台白鸽群飞</div>
                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 中山陵 <span class="warning-tag">需预约</span></div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>免费（需预约）</p>
                    </div>
                </div>
                <div class="day-images-grid">
                    <img src="images/day2-wutong1.jpg" alt="梧桐大道" class="day-image" loading="lazy" onclick="openModal('day2', 2)">
                    <img src="images/day2-wutong2.jpg" alt="梧桐大道" class="day-image" loading="lazy" onclick="openModal('day2', 3)">
                    <div class="image-caption">🌳 梧桐大道（颐和路）· 梧桐树下的民国往事</div>
                </div>
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：梧桐大道 → 南京大学</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚲 骑行：</span>约10分钟</p>
                        <p><span class="info-label">🚕 打车：</span>约12-15元</p>
                        <div class="transport-summary">💰 本段交通预算：约12-15元</div>
                    </div>
                </div>
                <div class="day-images-grid">
                    <img src="images/day2-nanda1.jpg" alt="南京大学" class="day-image" loading="lazy" onclick="openModal('day2', 4)">
                    <img src="images/day2-nanda2.jpg" alt="南京大学" class="day-image" loading="lazy" onclick="openModal('day2', 5)">
                    <div class="image-caption">🎓 南京大学鼓楼校区</div>
                </div>
            </div>
        </section>

        <!-- Day3 -->
        <section id="day3" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day3</div>
                    <div class="day-date">二选一 · 红山森林/城墙漫步 <span class="weather-icon">⛅️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day3 精确时间安排（方案A）</h4>
                    <ul>
                        <li><strong>9:00-9:30</strong> 酒店 → 红山动物园</li>
                        <li><strong>9:30-13:00</strong> 红山动物园（3.5h）</li>
                        <li><strong>13:00-13:30</strong> 午餐</li>
                        <li><strong>13:30-17:00</strong> 玄武湖散步/划船（2h）</li>
                        <li><strong>17:00-18:30</strong> 鸡鸣寺</li>
                    </ul>
                </div>
                <img src="images/day3-hongshan.jpg" alt="红山动物园" class="day-image" loading="lazy" onclick="openModal('day3', 0)">
                <div class="image-caption">🐼 红山森林动物园</div>
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：红山 → 玄武湖/鸡鸣寺</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚇 地铁：</span>约30分钟，3元</p>
                        <div class="transport-summary">💰 本段交通预算：约3元</div>
                    </div>
                </div>
                <img src="images/day3-jimingsi.jpg" alt="鸡鸣寺" class="day-image" loading="lazy" onclick="openModal('day3', 1)">
                <div class="image-caption">🏯 鸡鸣寺</div>
                <img src="images/day3-xuanwuhu.jpg" alt="玄武湖" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🌅 玄武湖</div>
                <img src="images/day3-nightride.jpg" alt="夜骑玄武湖" class="day-image" loading="lazy" onclick="openModal('day3', 3)">
                <div class="image-caption">🌙 夜骑玄武湖（可选）</div>
            </div>
        </section>

        <!-- Day4 -->
        <section id="day4" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day4</div>
                    <div class="day-date">民国遗韵 · 博物之旅 <span class="weather-icon">☀️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day4 精确时间安排（博物日）</h4>
                    <ul>
                        <li><strong>9:45-13:00</strong> 南京博物院（3h+）</li>
                        <li><strong>14:00-17:00</strong> 总统府（2.5h）</li>
                    </ul>
                </div>
                <img src="images/day4-bowuyuan.jpg" alt="南京博物院" class="day-image" loading="lazy" onclick="openModal('day4', 0)">
                <div class="image-caption">🏛️ 南京博物院 <span class="warning-tag">最难约TOP1</span></div>
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：南博 → 总统府</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚶 步行：</span>约15分钟</p>
                        <div class="transport-summary">💰 本段交通预算：约0元（步行）</div>
                    </div>
                </div>
                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府</div>
                </div>
            </div>
        </section>

        <!-- Day5 -->
        <section id="day5" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day5</div>
                    <div class="day-date">铭记历史 · 治愈收尾 <span class="weather-icon">⛅️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day5 精确时间安排（铭记+治愈）</h4>
                    <ul>
                        <li><strong>9:45-12:30</strong> 纪念馆（2.5h）</li>
                        <li><strong>14:00-17:30</strong> 下午治愈三选一</li>
                    </ul>
                </div>
                <img src="images/day5-jinianguan.jpg" alt="纪念馆" class="day-image" loading="lazy" onclick="openModal('day5', 0)">
                <div class="image-caption">🕊️ 纪念馆 <span class="warning-tag">最难约TOP2</span></div>
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：纪念馆 → 新城区</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚇 地铁：</span>约15分钟，2元</p>
                        <div class="transport-summary">💰 本段交通预算：约2元</div>
                    </div>
                </div>
                <div class="day-images-grid">
                    <img src="images/day5-nanjing-eye1.jpg" alt="南京眼" class="day-image" loading="lazy" onclick="openModal('day5', 1)">
                    <img src="images/day5-baoli-theatre.jpg" alt="保利大剧院" class="day-image" loading="lazy" onclick="openModal('day5', 2)">
                    <div class="image-caption">🏙️ 南京眼/保利大剧院</div>
                </div>
            </div>
        </section>

        <!-- Day6 -->
        <section id="day6" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day6</div>
                    <div class="day-date">告别金陵 · 奔赴黄山 <span class="weather-icon">🌤️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day6 精确时间安排（转场日）</h4>
                    <ul>
                        <li><strong>12:30-13:30</strong> 前往南京南站</li>
                        <li><strong>13:30-15:30</strong> 🚄南京南 → 黄山北</li>
                        <li><strong>15:30-16:30</strong> 黄山北 → 汤口镇</li>
                    </ul>
                </div>
                <div class="day-images-grid">
                    <img src="images/day6-tangkou1.jpg" alt="汤口镇" class="day-image" loading="lazy" onclick="openModal('day6', 0)">
                    <img src="images/day6-tangkou2.jpg" alt="汤口镇" class="day-image" loading="lazy" onclick="openModal('day6', 1)">
                    <img src="images/day6-tangkou3.jpg" alt="汤口镇" class="day-image" loading="lazy" onclick="openModal('day6', 2)">
                    <div class="image-caption">🏨 汤口镇 · 黄山脚下休整</div>
                </div>
            </div>
        </section>

        <!-- Day7 -->
        <section id="day7" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day7</div>
                    <div class="day-date">黄山一日游 · 索道上下 <span class="weather-icon">☀️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day7 精确时间安排（黄山登顶日）</h4>
                    <ul>
                        <li><strong>8:00-8:20</strong> 云谷索道上山</li>
                        <li><strong>8:20-12:00</strong> 始信峰→光明顶（3.5h）</li>
                        <li><strong>12:30-14:30</strong> 光明顶→迎客松（2h）</li>
                        <li><strong>14:30-15:00</strong> 迎客松拍照 ⚠️ 务必15:00前离开</li>
                        <li><strong>15:00-16:30</strong> 玉屏索道下山 ⚠️ 末班17:00</li>
                    </ul>
                </div>
                <div class="day-images-grid">
                    <img src="images/day7-yunhai1.jpg" alt="黄山云海" class="day-image" loading="lazy" onclick="openModal('day7', 0)">
                    <img src="images/day7-yunhai2.jpg" alt="黄山云海" class="day-image" loading="lazy" onclick="openModal('day7', 1)">
                    <div class="image-caption">☁️ 黄山云海</div>
                </div>
                <img src="images/day7-shixinfeng.jpg" alt="始信峰" class="day-image" loading="lazy" onclick="openModal('day7', 2)">
                <div class="image-caption">🌲 始信峰</div>
                <img src="images/day7-guangmingding.jpg" alt="光明顶" class="day-image" loading="lazy" onclick="openModal('day7', 3)">
                <div class="image-caption">✨ 光明顶</div>
                <img src="images/day7-yingkesong.jpg" alt="迎客松" class="day-image" loading="lazy" onclick="openModal('day7', 4)">
                <div class="image-caption">🌲 迎客松</div>
            </div>
        </section>

        <!-- Day8 -->
        <section id="day8" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day8</div>
                    <div class="day-date">汤口闲逛 · 傍晚返程 <span class="weather-icon">⛅️</span></div>
                </div>
                <div class="tips-box">
                    <h4>⏰ Day8 精确时间安排（返程日）</h4>
                    <ul>
                        <li><strong>9:30-12:00</strong> 汤口周边闲逛</li>
                        <li><strong>13:30-14:30</strong> 汤口 → 黄山北站</li>
                    </ul>
                </div>
                <img src="images/day8-tangkou-around.jpg" alt="汤口周边" class="day-image" loading="lazy" onclick="openModal('day8', 0)">
                <div class="image-caption">🌿 汤口周边 · 自然醒的慢时光</div>
            </div>
        </section>

        <!-- 公共板块：吃喝逛 -->
        <section id="food" class="section">
            <div class="public-section">
                <h2 class="public-title">🍜 吃喝逛 · 城市漫游指南</h2>
                <div class="public-card">
                    <h4>南京必吃美食</h4>
                    <ul>
                        <li>小潘记鸭血粉丝汤（珠江路）</li>
                        <li>蒋有记锅贴（老门东）</li>
                        <li>李记清真馆（打钉巷）</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>黄山徽菜</h4>
                    <ul>
                        <li>臭鳜鱼：闻着臭吃着香</li>
                        <li>毛豆腐：煎后蘸辣酱</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 公共板块：住宿安排 -->
        <section id="hotel" class="section">
            <div class="public-section">
                <h2 class="public-title">🏨 住宿安排</h2>
                <div class="public-card">
                    <h4>南京段（Day1-Day5）</h4>
                    <p><span class="booking-status pending" onclick="toggleBookingStatus(this)">🔴 待预订</span></p>
                </div>
                <div class="public-card">
                    <h4>黄山段（Day6-Day7）</h4>
                    <p><span class="booking-status pending" onclick="toggleBookingStatus(this)">🔴 待预订</span></p>
                </div>
            </div>
        </section>

        <!-- 公共板块：行李清单 -->
        <section id="luggage" class="section">
            <div class="public-section">
                <h2 class="public-title">🎒 行李清单</h2>
                <div class="category-btns">
                    <button class="category-btn active" onclick="showCategory('all')">全部</button>
                    <button class="category-btn" onclick="showCategory('doc')">📄 证件类</button>
                    <button class="category-btn" onclick="showCategory('city')">🏙️ 城市出行</button>
                    <button class="category-btn" onclick="showCategory('mountain')">⛰️ 登山装备</button>
                </div>
                <div id="category-all" class="category-list active">
                    <div class="public-card">
                        <h4>通用证件（必带）</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="身份证"> 身份证</li>
                            <li><input type="checkbox" aria-label="学生证"> 学生证</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- 公共板块：须知 -->
        <section id="avoid" class="section">
            <div class="public-section">
                <h2 class="public-title">⚠️ 避坑须知</h2>
                <div class="public-card">
                    <h4>南京避坑</h4>
                    <ul>
                        <li>❌ 夫子庙别买特产</li>
                        <li>✅ 老门东往里走</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 公共板块：预约清单 -->
        <section id="booking" class="section">
            <div class="public-section">
                <h2 class="public-title">📝 预约清单</h2>
                <div class="public-card">
                    <h4>南京必预约</h4>
                    <ul>
                        <li>📍 中山陵：免费预约</li>
                        <li>⚠️ 南京博物院：最难约！提前7天0点蹲守</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 公共板块：应急联系卡 -->
        <section id="emergency" class="section">
            <div class="public-section">
                <h2 class="public-title">🆘 应急联系卡</h2>
                <div class="emergency-card">
                    <h4>南京景点电话</h4>
                    <ul>
                        <li>中山陵园风景区：025-84461111</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 结语 -->
        <div class="conclusion">
            <h2>旅行攻略总结</h2>
            <p>
                <strong>南京5天：</strong>Day1→Day2→Day3→Day4→Day5<br>
                <strong>黄山3天：</strong>Day6→Day7→Day8<br>
                ✨ v15版：精确时间安排 + 交通互斥 + 无障碍优化
            </p>
        </div>
        <div class="footer">
            <p>✨ 南京黄山之旅 · 2026年 · 8天7晚深度旅行攻略 v15（完整优化版）</p>
        </div>
    </div>

    <!-- 图片模态框 -->
    <div class="modal" id="imageModal" onclick="closeModal(event)">
        <button class="modal-close" aria-label="关闭图片">×</button>
        <button class="modal-arrow left" onclick="changeImage(-1, event)" aria-label="上一张">‹</button>
        <img class="modal-img" id="modalImage" src="" alt="放大图片">
        <button class="modal-arrow right" onclick="changeImage(1, event)" aria-label="下一张">›</button>
    </div>

    <!-- 回到顶部按钮 -->
    <button class="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" aria-label="回到顶部">↑</button>

    <script>
        /* 图片数组 */
        const dayImages = {
            'day1': ['images/day1-ganxi.jpg', 'images/day1-laomendong.jpg', 'images/day1-qinhuai1.jpg', 'images/day1-qinhuai2.jpg'],
            'day2': ['images/day2-mingxiaoling.jpg', 'images/day2-zhongshanling.jpg', 'images/day2-wutong1.jpg', 'images/day2-wutong2.jpg', 'images/day2-nanda1.jpg', 'images/day2-nanda2.jpg'],
            'day3': ['images/day3-hongshan.jpg', 'images/day3-jimingsi.jpg', 'images/day3-xuanwuhu.jpg', 'images/day3-nightride.jpg'],
            'day4': ['images/day4-bowuyuan.jpg', 'images/day4-zongtong1.jpg', 'images/day4-zongtong2.jpg'],
            'day5': ['images/day5-jinianguan.jpg', 'images/day5-nanjing-eye1.jpg', 'images/day5-baoli-theatre.jpg'],
            'day6': ['images/day6-tangkou1.jpg', 'images/day6-tangkou2.jpg', 'images/day6-tangkou3.jpg'],
            'day7': ['images/day7-yunhai1.jpg', 'images/day7-yunhai2.jpg', 'images/day7-shixinfeng.jpg', 'images/day7-guangmingding.jpg', 'images/day7-yingkesong.jpg'],
            'day8': ['images/day8-tangkou-around.jpg']
        };
        let currentDay = '';
        let currentImageIndex = 0;

        /* 显示指定板块 */
        function showSection(sectionId) {
            document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
            document.querySelectorAll('.top-nav .nav-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            updateBottomTab(sectionId);
            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        /* 进入行程 */
        function enterItinerary() {
            showSection('day1');
            document.querySelector('.top-nav .nav-btn[onclick*="day1"]').classList.add('active');
        }

        /* 切换底部Tab */
        function switchTab(tabName) {
            document.querySelectorAll('.bottom-tab .tab-item').forEach(tab => tab.classList.remove('active'));
            event.target.closest('.tab-item').classList.add('active');
            let sectionId;
            switch(tabName) {
                case 'itinerary': sectionId = 'day1'; break;
                case 'food': sectionId = 'food'; break;
                case 'hotel': sectionId = 'hotel'; break;
                case 'luggage': sectionId = 'luggage'; break;
                case 'avoid': sectionId = 'avoid'; break;
                case 'booking': sectionId = 'booking'; break;
                case 'emergency': sectionId = 'emergency'; break;
            }
            showSection(sectionId);
        }

        /* 更新底部Tab状态 */
        function updateBottomTab(sectionId) {
            document.querySelectorAll('.bottom-tab .tab-item').forEach(tab => tab.classList.remove('active'));
            const tabMap = {
                'day1': 'itinerary', 'day2': 'itinerary', 'day3': 'itinerary', 'day4': 'itinerary',
                'day5': 'itinerary', 'day6': 'itinerary', 'day7': 'itinerary', 'day8': 'itinerary',
                'food': 'food', 'hotel': 'hotel', 'luggage': 'luggage', 'avoid': 'avoid', 'booking': 'booking', 'emergency': 'emergency'
            };
            const targetTab = document.querySelector(`.bottom-tab .tab-item[data-tab="${tabMap[sectionId]}"]`);
            if (targetTab) targetTab.classList.add('active');
        }

        /* 切换景点卡片折叠 */
        function toggleCard(card) { card.classList.toggle('collapsed'); }

        /* 交通卡片互斥逻辑 */
        function toggleTransportCard(clickedCard) {
            clickedCard.classList.toggle('collapsed');
            if (!clickedCard.classList.contains('collapsed')) {
                document.querySelectorAll('.transport-card').forEach(card => {
                    if (card !== clickedCard && !card.classList.contains('collapsed')) {
                        card.classList.add('collapsed');
                    }
                });
            }
        }

        /* 打开图片模态框 */
        function openModal(day, index) {
            currentDay = day;
            currentImageIndex = index;
            document.getElementById('modalImage').src = dayImages[day][index];
            document.getElementById('imageModal').classList.add('active');
        }

        /* 切换图片 */
        function changeImage(direction, event) {
            event.stopPropagation();
            const images = dayImages[currentDay];
            currentImageIndex = (currentImageIndex + direction + images.length) % images.length;
            document.getElementById('modalImage').src = images[currentImageIndex];
        }

        /* 关闭模态框 */
        function closeModal(event) {
            if (event.target === document.getElementById('imageModal') || event.target.classList.contains('modal-close')) {
                document.getElementById('imageModal').classList.remove('active');
            }
        }

        /* 切换分类 */
        function showCategory(category) {
            document.querySelectorAll('.category-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            document.querySelectorAll('.category-list').forEach(list => list.classList.remove('active'));
            document.getElementById(`category-${category}`).classList.add('active');
        }

        /* 切换酒店状态 */
        function toggleBookingStatus(statusSpan) {
            if (statusSpan.classList.contains('pending')) {
                statusSpan.classList.remove('pending');
                statusSpan.classList.add('booked');
                statusSpan.textContent = '✅ 已预订';
            } else {
                statusSpan.classList.remove('booked');
                statusSpan.classList.add('pending');
                statusSpan.textContent = '🔴 待预订';
            }
        }

        /* 回到顶部按钮平滑消失 */
        window.addEventListener('scroll', function() {
            const backToTop = document.querySelector('.back-to-top');
            if (window.scrollY > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        /* 行李清单本地存储 */
        document.querySelectorAll('.checklist input[type="checkbox"]').forEach(checkbox => {
            const key = checkbox.parentElement.textContent.trim();
            checkbox.checked = localStorage.getItem(key) === 'true';
            checkbox.addEventListener('change', function() {
                localStorage.setItem(key, this.checked);
            });
        });

        /* 打印函数 */
        function printItinerary() {
            alert('建议用Chrome打印，勾选"背景图形"以保留卡片阴影');
            window.print();
        }

        /* 滑动切换 */
        const daySections = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8'];
        let touchStartX = 0;
        document.querySelector('.content-container').addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        });
        document.querySelector('.content-container').addEventListener('touchend', e => {
            const touchEndX = e.changedTouches[0].screenX;
            const diff = touchStartX - touchEndX;
            if (Math.abs(diff) > 50) {
                const currentSection = document.querySelector('.section.active');
                const currentId = currentSection.id;
                const currentIndex = daySections.indexOf(currentId);
                if (currentIndex !== -1) {
                    if (diff > 0 && currentIndex < daySections.length - 1) {
                        showSection(daySections[currentIndex + 1]);
                        updateNavButton(daySections[currentIndex + 1]);
                    } else if (diff < 0 && currentIndex > 0) {
                        showSection(daySections[currentIndex - 1]);
                        updateNavButton(daySections[currentIndex - 1]);
                    } else {
                        if (navigator.vibrate) { navigator.vibrate(50); }
                    }
                }
            }
        });

        function updateNavButton(sectionId) {
            document.querySelectorAll('.top-nav .nav-btn').forEach(btn => btn.classList.remove('active'));
            const targetBtn = document.querySelector(`.top-nav .nav-btn[onclick="showSection('${sectionId}')"]`);
            if (targetBtn) targetBtn.classList.add('active');
        }
    </script>
</body>
</html>'''

with open(r'D:\nanjing\nanjing-v15-complete.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('v15-complete.html 创建完成！')
