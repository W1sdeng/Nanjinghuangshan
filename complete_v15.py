# 继续完成v15-final.html的剩余部分
# 读取现有文件，找到插入点，然后追加剩余内容

file_path = r'D:\nanjing\nanjing-v15-final.html'

# 剩余内容（Day3-Day8 + 公共板块 + JavaScript）
remaining_content = '''
        
        <!-- ==========================================
             Day3 - 二选一 · 红山探秘 或 城墙漫步
             方案A：红山动物园深度游 → 玄武湖散步 → 鸡鸣寺傍晚
             方案B：颐和路再逛 → 鸡鸣寺+城墙 → 玄武湖骑行
             精确时间安排
             ========================================== -->
        <section id="day3" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day3</div>
                    <div class="day-date">二选一 · 红山探秘 或 城墙漫步 <span class="weather-icon">⛅️</span></div>
                </div>
                
                <!-- 精确时间安排 - 方案A -->
                <div class="tips-box">
                    <h4>⏰ Day3 精确时间安排（方案A：红山+城墙）</h4>
                    <ul>
                        <li><strong>8:00-9:00</strong> 起床、洗漱</li>
                        <li><strong>9:00-9:30</strong> 酒店 → 红山动物园（地铁约30分钟）</li>
                        <li><strong>9:30-13:00</strong> 红山动物园（3.5h，北门进南门出）</li>
                        <li><strong>13:00-13:30</strong> 午餐</li>
                        <li><strong>13:30-14:15</strong> 红山 → 玄武湖/鸡鸣寺（地铁约35分钟）</li>
                        <li><strong>14:15-15:00</strong> 酒店休息1小时（恢复体力）</li>
                        <li><strong>15:00-17:00</strong> 玄武湖（散步/划船2h）</li>
                        <li><strong>17:00-18:30</strong> 鸡鸣寺（1.5h，傍晚光线极美）</li>
                        <li><strong>18:30</strong> 晚餐 / 老门东夜逛</li>
                        <li><strong>💪 精力旺盛者可选夜骑</strong>：19:30出发，顺时针环湖约9km（约1.5h）</li>
                    </ul>
                </div>
                
                <!-- 精确时间安排 - 方案B -->
                <div class="tips-box">
                    <h4>⏰ Day3 精确时间安排（方案B：城墙休闲）</h4>
                    <ul>
                        <li><strong>9:00-10:00</strong> 自然醒、早餐</li>
                        <li><strong>10:00-11:30</strong> 颐和路再逛（上午人少）</li>
                        <li><strong>11:30-12:30</strong> 午餐</li>
                        <li><strong>12:30-13:00</strong> 前往鸡鸣寺</li>
                        <li><strong>13:00-14:30</strong> 鸡鸣寺 + 台城城墙（1.5h）</li>
                        <li><strong>14:30-17:00</strong> 玄武湖骑行/泛舟（2.5h，轻松往返）</li>
                        <li><strong>17:00</strong> 晚餐</li>
                    </ul>
                </div>
                
                <div class="quote">"动物园是城市的良心。"<div class="quote-author">—— 佚名</div></div>
                
                <img src="images/day3-hongshan.jpg" alt="红山森林动物园口碑最好" class="day-image" loading="lazy" onclick="openModal('day3', 0)">
                <div class="image-caption">🐼 红山森林动物园 · 国内口碑最好的动物园</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🐘</span> 红山森林动物园</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>40元/人</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>3-4小时（上午9:00-13:00）</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：北门→大熊猫馆→考拉馆→长颈鹿馆→猴山→南门</li>
                            <li>最佳拍照点：大熊猫"和和""平平"上午9点前最活跃</li>
                        </ul>
                    </div>
                </div>

                <!-- 交通卡片：红山 → 玄武湖/鸡鸣寺 -->
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：红山动物园 → 玄武湖/鸡鸣寺</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚇 地铁：</span>红山动物园站1号线→鼓楼换4号线→鸡鸣寺站，约30分钟，3元</p>
                        <p><span class="info-label">🚕 打车：</span>约8.5km，25分钟，28-32元，4人拼车人均7-8元</p>
                        <p><span class="info-label">⚠️ 注意：</span>早高峰地铁拥挤，建议8:30前出发</p>
                        <div class="transport-summary">💰 本段交通预算：约28-32元（打车）或 3元（地铁）</div>
                    </div>
                </div>

                <img src="images/day3-jimingsi.jpg" alt="鸡鸣寺南朝四百八十寺" class="day-image" loading="lazy" onclick="openModal('day3', 1)">
                <div class="image-caption">🏯 鸡鸣寺 · 南朝四百八十寺之首</div>

                <img src="images/day3-xuanwuhu.jpg" alt="玄武湖金陵明珠" class="day-image" loading="lazy" onclick="openModal('day3', 2)">
                <div class="image-caption">🌅 玄武湖 · 金陵明珠，散步或骑行皆宜</div>

                <img src="images/day3-nightride.jpg" alt="夜骑玄武湖灯光" class="day-image" loading="lazy" onclick="openModal('day3', 3)">
                <div class="image-caption">🌙 夜骑玄武湖 · 解放门段灯光最美（可选）</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏯</span> 鸡鸣寺 → 台城城墙 → 玄武湖</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>鸡鸣寺10元，台城城墙30元，玄武湖免费</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>2-3小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：鸡鸣寺→登药师佛塔→台城城墙→玄武湖</li>
                            <li>最佳拍照点：鸡鸣寺拍紫峰大厦同框，台城拍玄武湖全景</li>
                            <li>💪 精力旺盛者可选夜骑：19:30解放门顺时针环湖（约9km）</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day4 - 民国遗韵 · 博物之旅
             景点：南京博物院 → 总统府
             精确时间安排
             ========================================== -->
        <section id="day4" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day4</div>
                    <div class="day-date">民国遗韵 · 博物之旅 <span class="weather-icon">☀️</span></div>
                </div>
                
                <!-- 精确时间安排 -->
                <div class="tips-box">
                    <h4>⏰ Day4 精确时间安排（博物日）</h4>
                    <ul>
                        <li><strong>8:00-9:00</strong> 起床、洗漱</li>
                        <li><strong>9:00-9:45</strong> 早餐 + 前往南博（地铁约30分钟）</li>
                        <li><strong>9:45-13:00</strong> 南京博物院（3h+，9点开馆尽量早到）</li>
                        <li><strong>13:00-14:00</strong> 午餐 + 休息（中山东路附近）</li>
                        <li><strong>14:00-14:15</strong> 南博 → 总统府（步行15分钟）</li>
                        <li><strong>14:15-17:00</strong> 总统府（2.5h）</li>
                        <li><strong>17:00</strong> 1912街区晚餐/新街口逛街（总统府出门即到）</li>
                    </ul>
                </div>
                
                <div class="quote">"一条颐和路，半部民国史。"<div class="quote-author">—— 南京民谚</div></div>
                
                <img src="images/day4-bowuyuan.jpg" alt="南京博物院中国三大博物馆" class="day-image" loading="lazy" onclick="openModal('day4', 0)">
                <div class="image-caption">🏛️ 南京博物院 · 中国三大博物馆之一 <span class="warning-tag">最难约TOP1</span></div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 南京博物院 <span class="warning-tag">提前7天0点蹲守</span></div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 地址：</span>南京市玄武区中山东路321号</p>
                        <p><span class="info-label">⏰ 开放时间：</span>9:00-17:00，周一闭馆</p>
                        <p><span class="info-label">🎫 门票：</span>免费（必须提前预约）</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>3-4小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：历史馆→特展馆→艺术馆→民国馆→非遗馆</li>
                            <li>最佳拍照点：民国馆复古街道，历史馆旋转楼梯光影绝美</li>
                        </ul>
                    </div>
                </div>

                <!-- 交通卡片：南博 → 总统府 -->
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 交通：南博 → 总统府（建议午休后再出发）</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚶 步行：</span>约15分钟，中山东路直走，梧桐遮阴</p>
                        <p><span class="info-label">🚇 地铁：</span>明故宫站2号线→大行宫站，1站，2元</p>
                        <p><span class="info-label">🚕 打车：</span>起步价约11元，5分钟</p>
                        <p><span class="info-label">💡 建议：</span>出南博后在中山东路附近午餐休息1小时再出发</p>
                        <div class="transport-summary">💰 本段交通预算：约11元（打车）或 2元（地铁）</div>
                    </div>
                </div>

                <div class="day-images-grid">
                    <img src="images/day4-zongtong1.jpg" alt="总统府民国中枢" class="day-image" loading="lazy" onclick="openModal('day4', 1)">
                    <img src="images/day4-zongtong2.jpg" alt="总统府子超楼" class="day-image" loading="lazy" onclick="openModal('day4', 2)">
                    <div class="image-caption">🏛️ 总统府 · 民国中枢与江南园林交融</div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏛️</span> 总统府 <span class="warning-tag">需预约</span></div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>40元/人（需预约）</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>2-3小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：门楼→大堂→子超楼→煦园→孙中山办公室</li>
                            <li>最佳拍照点：子超楼民国风楼梯，煦园江南园林漏窗</li>
                            <li>🏙️ 出总统府即到1912街区，民国建筑酒吧街，适合晚餐</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day5 - 铭记历史 · 治愈收尾
             景点：纪念馆 → 治愈三选一
             精确时间安排
             ========================================== -->
        <section id="day5" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day5</div>
                    <div class="day-date">铭记历史 · 治愈收尾 <span class="weather-icon">⛅️</span></div>
                </div>
                
                <!-- 精确时间安排 -->
                <div class="tips-box">
                    <h4>⏰ Day5 精确时间安排（铭记+治愈）</h4>
                    <ul>
                        <li><strong>8:00-9:00</strong> 起床、洗漱</li>
                        <li><strong>9:00-9:45</strong> 早餐 + 前往纪念馆（地铁约30分钟）</li>
                        <li><strong>9:45-12:30</strong> 纪念馆（2.5h，保持肃穆）</li>
                        <li><strong>12:30-13:30</strong> 建邺万达午餐（调整情绪）</li>
                        <li><strong>13:30-14:00</strong> 前往新城区（地铁约15分钟）</li>
                        <li><strong>14:00-17:30</strong> 下午治愈三选一（3.5h）</li>
                        <li><strong>17:30</strong> 晚餐 / 南京眼夜景（若下午选了②）</li>
                    </ul>
                </div>
                
                <div class="quote">"忘记历史就意味着背叛。"<div class="quote-author">—— 列宁</div></div>
                
                <img src="images/day5-jinianguan.jpg" alt="纪念馆以史为鉴" class="day-image" loading="lazy" onclick="openModal('day5', 0)">
                <div class="image-caption">🕊️ 侵华日军南京大屠杀遇难同胞纪念馆 · 以史为鉴 <span class="warning-tag">最难约TOP2</span></div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🕊️</span> 纪念馆 <span class="warning-tag">提前7天0点蹲守</span></div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 门票：</span>免费（必须提前预约）</p>
                        <p><span class="info-label">⏱️ 建议游玩：</span>2-3小时</p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：入口→史料陈列厅→"万人坑"遗址→冥思厅</li>
                            <li>馆内保持肃穆，禁止拍照</li>
                        </ul>
                    </div>
                </div>

                <!-- 交通卡片：纪念馆 → 新城区 -->
                <div class="transport-card collapsed" onclick="toggleTransportCard(this)">
                    <div class="attraction-title"><span>🚗</span> 下午交通：纪念馆 → 新城区（三选一）</div>
                    <div class="transport-detail">
                        <p><span class="info-label">🚇 地铁：</span>云锦路站2号线→元通站（河西方向），约15分钟</p>
                        <p><span class="info-label">🚕 打车：</span>到南京眼约6km，15分钟，约20元</p>
                        <div class="transport-summary">💰 本段交通预算：约20元（打车）或 2元（地铁）</div>
                    </div>
                </div>

                <div class="tips-box">
                    <h4>🌿 下午治愈三选一（全部同方向，轻松收尾）</h4>
                    <ul>
                        <li>① 南京云锦博物馆（免费，室内，安静华美）</li>
                        <li>② 南京眼步行桥+保利大剧院（新城风貌，拍照圣地）</li>
                        <li>③ 河西金鹰世界/华采天地逛街（现代商场+晚餐）</li>
                        <li>若选②，晚上可继续看南京眼夜景</li>
                    </ul>
                </div>

                <div class="day-images-grid">
                    <img src="images/day5-nanjing-eye1.jpg" alt="南京眼步行桥" class="day-image" loading="lazy" onclick="openModal('day5', 1)">
                    <img src="images/day5-baoli-theatre.jpg" alt="保利大剧院" class="day-image" loading="lazy" onclick="openModal('day5', 2)">
                    <div class="image-caption">🏙️ 南京眼步行桥/保利大剧院 · 新城风貌（下午三选一）</div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day6 - 告别金陵 · 奔赴黄山
             活动：上午自由补漏 → 高铁赴黄山 → 入住汤口
             精确时间安排
             ========================================== -->
        <section id="day6" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day6</div>
                    <div class="day-date">告别金陵 · 奔赴黄山 <span class="weather-icon">🌤️</span></div>
                </div>
                
                <!-- 精确时间安排 -->
                <div class="tips-box">
                    <h4>⏰ Day6 精确时间安排（转场日）</h4>
                    <ul>
                        <li><strong>8:00-9:30</strong> 自然醒、早餐</li>
                        <li><strong>9:30-11:30</strong> 上午自由（科巷/颐和路/长江大桥三选一）</li>
                        <li><strong>11:30-12:30</strong> 午餐</li>
                        <li><strong>12:30-13:00</strong> 前往南京南站（地铁约30分钟）</li>
                        <li><strong>13:00-13:30</strong> 候车上车</li>
                        <li><strong>13:30-15:30</strong> 🚄南京南 → 黄山北（2h）</li>
                        <li><strong>15:30-16:30</strong> 黄山北 → 汤口镇（大巴/打车约40分钟）</li>
                        <li><strong>16:30-17:00</strong> 酒店入住</li>
                        <li><strong>17:00-18:30</strong> 汤口镇逛逛</li>
                        <li><strong>18:30</strong> 徽菜晚餐</li>
                    </ul>
                </div>
                
                <div class="quote">"江南佳丽地，金陵帝王州。"<div class="quote-author">—— 谢朓</div></div>
                
                <div class="day-images-grid">
                    <img src="images/day6-tangkou1.jpg" alt="汤口镇黄山脚下" class="day-image" loading="lazy" onclick="openModal('day6', 0)">
                    <img src="images/day6-tangkou2.jpg" alt="汤口镇镇中心" class="day-image" loading="lazy" onclick="openModal('day6', 1)">
                    <div class="image-caption">🏨 汤口镇 · 黄山脚下休整</div>
                </div>
                <img src="images/day6-tangkou3.jpg" alt="汤口镇酒店周边" class="day-image" loading="lazy" onclick="openModal('day6', 2)">
                <div class="image-caption">🏨 汤口镇 · 酒店周边</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🍜</span> 上午自由/补漏</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📝 活动：</span>自然醒，补美食，买伴手礼</p>
                        <p>方案A：科巷菜场（本地人早餐圣地）</p>
                        <p>方案B：颐和路再骑行</p>
                        <p>方案C：南京长江大桥玻璃栈道</p>
                    </div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🚄</span> 高铁赴黄山</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📍 车次：</span>南京南→黄山北，中午前后，约2小时</p>
                        <p><span class="info-label">🎫 票价：</span>二等座约150-180元</p>
                    </div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏨</span> 入住汤口桔子水晶酒店</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📝 提示：</span>晚上吃徽菜，补充次日登山补给</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day7 - 黄山一日游 · 索道上下
             路线：云谷索道上 → 始信峰 → 光明顶 → 迎客松 → 玉屏索道下
             精确时间安排
             ========================================== -->
        <section id="day7" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day7</div>
                    <div class="day-date">黄山一日游 · 索道上下 <span class="weather-icon">☀️</span></div>
                </div>
                
                <!-- 精确时间安排 -->
                <div class="tips-box">
                    <h4>⏰ Day7 精确时间安排（黄山登顶日）</h4>
                    <ul>
                        <li><strong>6:30-7:00</strong> 早起（索道日需早）</li>
                        <li><strong>7:00-7:30</strong> 早餐</li>
                        <li><strong>7:30-8:00</strong> 酒店 → 换乘中心 → 云谷索道</li>
                        <li><strong>8:00-8:20</strong> 云谷索道上山</li>
                        <li><strong>8:20-12:00</strong> 白鹅岭→始信峰→北海→光明顶（3.5h，边走边拍）</li>
                        <li><strong>12:00-12:30</strong> 光明顶午餐（自带干粮）</li>
                        <li><strong>12:30-14:30</strong> 光明顶→鳌鱼峰→迎客松（2h）</li>
                        <li><strong>14:30-15:00</strong> 迎客松拍照 ⚠️ 务必15:00前离开</li>
                        <li><strong>15:00-16:30</strong> 步行至玉屏索道 ⚠️ 末班约17:00！</li>
                        <li><strong>16:30-17:00</strong> 玉屏索道下山</li>
                        <li><strong>17:00-17:30</strong> 返回酒店休息</li>
                        <li><strong>18:30</strong> 徽菜晚餐，好好犒劳自己</li>
                    </ul>
                </div>
                
                <div class="quote">"五岳归来不看山，黄山归来不看岳。"<div class="quote-author">—— 徐霞客</div></div>

                <div class="day-images-grid">
                    <img src="images/day7-yunhai1.jpg" alt="黄山云海翻涌" class="day-image" loading="lazy" onclick="openModal('day7', 0)">
                    <img src="images/day7-yunhai2.jpg" alt="黄山云海松石" class="day-image" loading="lazy" onclick="openModal('day7', 1)">
                    <div class="image-caption">☁️ 黄山云海 · 云海翻涌与松石画廊</div>
                </div>

                <img src="images/day7-shixinfeng.jpg" alt="始信峰黄山小峰" class="day-image" loading="lazy" onclick="openModal('day7', 2)">
                <div class="image-caption">🌲 始信峰 · 黄山三十六小峰之首</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🚡</span> 云谷索道上 → 玉屏索道下 <span class="warning-tag">注意末班</span></div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🎫 索道票：</span>云谷80元，玉屏90元（提前购）</p>
                        <p><span class="info-label">📍 路线：</span>云谷上→白鹅岭→始信峰→光明顶→迎客松→玉屏下</p>
                        <p><span class="info-label">⏱️ 全程：</span>6-7小时</p>
                        <p><span class="info-label">⚠️ 玉屏索道末班约17:00，16:30前务必到达索道站</span></p>
                    </div>
                    <div class="old-tips">
                        <h4>🔍 老玩家Tips</h4>
                        <ul>
                            <li>省体力路线：云谷索道上→始信峰→光明顶→迎客松→玉屏索道下</li>
                            <li>最佳拍照点：始信峰"梦笔生花"，光明顶360度全景</li>
                            <li>山下登山杖10-20元，省30%体力</li>
                        </ul>
                    </div>
                </div>

                <img src="images/day7-guangmingding.jpg" alt="光明顶观景台" class="day-image" loading="lazy" onclick="openModal('day7', 3)">
                <div class="image-caption">✨ 光明顶 · 黄山第二高峰360度观景台</div>

                <img src="images/day7-yingkesong.jpg" alt="迎客松千年古松" class="day-image" loading="lazy" onclick="openModal('day7', 4)">
                <div class="image-caption">🌲 迎客松 · 千年古松，黄山标志</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🏨</span> 下山回汤口酒店躺平</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📝 活动：</span>下山后直接回酒店休息，晚上在汤口吃徽菜</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             Day8 - 汤口闲逛 · 傍晚返程
             活动：自然醒+周边闲逛 → 返程高铁
             精确时间安排
             ========================================== -->
        <section id="day8" class="section">
            <div class="day-card">
                <div class="day-header">
                    <div class="day-label">Day8</div>
                    <div class="day-date">汤口闲逛 · 傍晚返程 <span class="weather-icon">⛅️</span></div>
                </div>
                
                <!-- 精确时间安排 -->
                <div class="tips-box">
                    <h4>⏰ Day8 精确时间安排（返程日）</h4>
                    <ul>
                        <li><strong>8:30-9:30</strong> 自然醒、早餐</li>
                        <li><strong>9:30-12:00</strong> 汤口周边闲逛+买伴手礼（翡翠谷/九龙瀑可选）</li>
                        <li><strong>12:00-13:00</strong> 午餐</li>
                        <li><strong>13:00-13:30</strong> 退房</li>
                        <li><strong>13:30-14:30</strong> 汤口 → 黄山北站（约40分钟）</li>
                        <li><strong>下午/傍晚</strong> 🚄 返程高铁</li>
                    </ul>
                </div>
                
                <div class="quote">"旅行不是逃避生活，而是让生活不再逃避我们。"<div class="quote-author">—— 佚名</div></div>
                
                <img src="images/day8-tangkou-around.jpg" alt="汤口周边慢时光" class="day-image" loading="lazy" onclick="openModal('day8', 0)">
                <div class="image-caption">🌿 汤口周边 · 自然醒的慢时光</div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🌅</span> 自然醒+周边闲逛</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">📝 活动：</span>睡到自然醒，可在汤口周边逛逛（翡翠谷、九龙瀑可选），买黄山毛峰、徽墨酥等伴手礼</p>
                        <p>雨天备选：翡翠谷/九龙瀑雨天更壮观</p>
                    </div>
                </div>

                <div class="attraction-card" onclick="toggleCard(this)">
                    <div class="attraction-title"><span>🚄</span> 返程</div>
                    <div class="attraction-detail">
                        <p><span class="info-label">🚗 交通：</span>下午汤口→黄山北站（约40分钟）</p>
                        <p><span class="info-label">🚄 高铁：</span>傍晚车次，返回出发地</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- ==========================================
             公共板块1：吃喝逛 · 城市漫游指南
             内容：南京必吃美食 + 黄山徽菜 + 商场街区 + 可选晚场 + 伴手礼
             ========================================== -->
        <section id="food" class="section">
            <div class="public-section">
                <h2 class="public-title">🍜 吃喝逛 · 城市漫游指南</h2>

                <div class="public-card">
                    <h4>南京必吃美食</h4>
                    <ul>
                        <li>小潘记鸭血粉丝汤（珠江路）：本地人常去，汤鲜料足，人均25元</li>
                        <li>蒋有记锅贴（老门东）：牛肉锅贴，外脆里嫩，人均30元</li>
                        <li>李记清真馆（打钉巷）：锅贴排队王，值得等</li>
                        <li>芳婆糕团店（王府大街）：糖芋苗、酒酿元宵</li>
                        <li>黄勤记凉粉（老门东）：酸辣爽口，人均15元</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>黄山徽菜</h4>
                    <ul>
                        <li>臭鳜鱼：徽菜代表作，闻着臭吃着香</li>
                        <li>毛豆腐：煎后蘸辣酱，人均30元</li>
                        <li>黄山烧饼：梅干菜肉馅，酥脆可口</li>
                        <li>⚠️ 徽菜偏油偏咸，肠胃敏感者酌情点菜</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>🏙️ 商场/街区推荐</h4>
                    <ul>
                        <li><span class="sub-label">新街口</span>德基广场+新百+艾尚天地+明瓦廊小吃</li>
                        <li><span class="sub-label">老门东</span>先锋书店骏惠书屋+秦淮礼物文创</li>
                        <li><span class="sub-label">1912街区</span>总统府隔壁，民国建筑酒吧街</li>
                        <li><span class="sub-label">河西</span>金鹰世界+华采天地+南京眼</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>🏙️ 可选晚场（按天）</h4>
                    <ul>
                        <li>Day1：秦淮夜游（已有）</li>
                        <li>Day2：新街口夜逛+明瓦廊夜宵</li>
                        <li>Day3：老门东夜逛（先锋书店骏惠书屋）</li>
                        <li>Day4：1912街区（总统府出门即到）</li>
                        <li>Day5：南京眼夜景（若下午选了②）</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>🎁 伴手礼指南</h4>
                    <ul>
                        <li>泸溪河桃酥（各店均有，口感酥松）</li>
                        <li>韩复兴盐水鸭（真空包装，方便携带）</li>
                        <li>秦淮礼物文创店（夫子庙附近）</li>
                        <li>黄山毛峰+徽墨酥（汤口镇购买）</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- ==========================================
             公共板块2：住宿安排
             内容：南京段/黄山段/返程住宿 + 预订状态切换
             ========================================== -->
        <section id="hotel" class="section">
            <div class="public-section">
                <h2 class="public-title">🏨 住宿安排</h2>
                <div class="public-card">
                    <h4>南京段（Day1 - Day5）</h4>
                    <p><span class="info-label">📍 推荐区域：</span>夫子庙/新街口/大行宫附近</p>
                    <p><span class="info-label">🏨 状态：</span><span class="booking-status pending" onclick="toggleBookingStatus(this)">🔴 待预订</span></p>
                    <p><span class="info-label">💡 选房建议：</span>近地铁3号线，方便去南博、总统府、夫子庙；避开临街低层防噪音</p>
                </div>
                <div class="public-card">
                    <h4>黄山段（Day6 - Day7）</h4>
                    <p><span class="info-label">📍 推荐酒店：</span>黄山汤口桔子水晶或换乘中心附近</p>
                    <p><span class="info-label">🏨 状态：</span><span class="booking-status pending" onclick="toggleBookingStatus(this)">🔴 待预订</span></p>
                    <p><span class="info-label">💡 提醒：</span>务必选"汤口"而非"屯溪"；提前订可找山景房可观云雾</p>
                </div>
                <div class="public-card">
                    <h4>Day8 返程</h4>
                    <p>无住宿。若返程车晚，可考虑黄山北站附近钟点房休整。</p>
                </div>
            </div>
        </section>

        <!-- ==========================================
             公共板块3：行李清单
             内容：证件类/城市出行/登山装备 分类筛选+勾选
             ========================================== -->
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
                            <li><input type="checkbox" aria-label="学生证"> 学生证（半价神器）</li>
                            <li><input type="checkbox" aria-label="充电宝"> 充电宝+数据线</li>
                        </ul>
                    </div>
                    <div class="public-card">
                        <h4>南京·城市出行篇</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="舒适平底鞋"> 舒适平底鞋/小白鞋（日均步行1万+）</li>
                            <li><input type="checkbox" aria-label="防晒用品"> 防晒：帽子、墨镜、防晒霜</li>
                        </ul>
                    </div>
                    <div class="public-card">
                        <h4>黄山·登山保命篇</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="防滑登山鞋"> 防滑登山鞋（拒绝高跟鞋/板鞋）</li>
                            <li><input type="checkbox" aria-label="登山杖"> 登山杖（山下10-20元，省30%体力）</li>
                            <li><input type="checkbox" aria-label="一次性雨衣"> 一次性雨衣（山风大，禁打伞）</li>
                        </ul>
                    </div>
                </div>

                <div id="category-doc" class="category-list">
                    <div class="public-card">
                        <h4>通用证件（必带）</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="身份证"> 身份证</li>
                            <li><input type="checkbox" aria-label="学生证"> 学生证（半价神器）</li>
                        </ul>
                    </div>
                </div>

                <div id="category-city" class="category-list">
                    <div class="public-card">
                        <h4>南京·城市出行篇</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="舒适平底鞋"> 舒适平底鞋/小白鞋</li>
                            <li><input type="checkbox" aria-label="防晒用品"> 防晒用品</li>
                        </ul>
                    </div>
                </div>

                <div id="category-mountain" class="category-list">
                    <div class="public-card">
                        <h4>黄山·登山保命篇</h4>
                        <ul class="checklist">
                            <li><input type="checkbox" aria-label="防滑登山鞋"> 防滑登山鞋</li>
                            <li><input type="checkbox" aria-label="登山杖"> 登山杖</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
             公共板块4：避坑须知
             内容：南京避坑 + 黄山避坑 + 雨天备选
             ========================================== -->
        <section id="avoid" class="section">
            <div class="public-section">
                <h2 class="public-title">⚠️ 避坑须知</h2>
                <div class="public-card">
                    <h4>南京避坑</h4>
                    <ul>
                        <li>❌ 夫子庙别买特产、别坐高价画舫</li>
                        <li>✅ 老门东往里走，小吃更便宜</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>黄山避坑</h4>
                    <ul>
                        <li>❌ 拒绝黄牛/野导，只在官方小程序买</li>
                        <li>✅ 山上水10元/瓶，自备干粮和水</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>🌧️ 雨天备选方案</h4>
                    <ul>
                        <li>南京：六朝博物馆、江宁织造博物馆、大报恩寺遗址（室内为主）</li>
                        <li>黄山：翡翠谷/九龙瀑雨天更壮观</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- ==========================================
             公共板块5：预约清单
             内容：南京必预约 + 黄山必预约（含紧迫提醒）
             ========================================== -->
        <section id="booking" class="section">
            <div class="public-section">
                <h2 class="public-title">📝 预约清单</h2>
                <div class="public-card">
                    <h4>南京必预约（提前1-7天）</h4>
                    <ul>
                        <li>📍 中山陵：免费预约，周一闭馆</li>
                        <li>📍 南京总统府：40元/人，周一闭馆</li>
                        <li>⚠️ 南京博物院：最难约！提前7天0点蹲守</li>
                        <li>⚠️ 纪念馆：提前7天0点蹲守</li>
                    </ul>
                </div>
                <div class="public-card">
                    <h4>黄山必预约（提前3-7天）</h4>
                    <ul>
                        <li>📍 黄山风景区门票：190元/人</li>
                        <li>⚠️ 玉屏索道末班约17:00，注意时间</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- ==========================================
             公共板块6：应急联系卡
             内容：南京景点电话 + 黄山景点电话
             ========================================== -->
        <section id="emergency" class="section">
            <div class="public-section">
                <h2 class="public-title">🆘 应急联系卡</h2>
                <div class="emergency-card">
                    <h4>南京景点电话</h4>
                    <ul>
                        <li>中山陵园风景区：025-84461111</li>
                        <li>南京总统府：025-84578700</li>
                    </ul>
                </div>
                <div class="emergency-card">
                    <h4>黄山景点电话</h4>
                    <ul>
                        <li>黄山景区咨询：0559-5561111</li>
                        <li>黄山北站：0559-5562666</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <!-- ==========================================
             结语 - 旅行攻略总结
             ========================================== -->
        <div class="conclusion">
            <h2>旅行攻略总结</h2>
            <p>
                <strong>南京5天：</strong>Day1秦淮初探→Day2钟山+🌳梧桐大道→Day3红山/城墙二选一→Day4南博+总统府→Day5铭记历史+新城治愈<br><br>
                <strong>黄山3天：</strong>Day6赴黄山→Day7黄山一日游→Day8返程<br><br>
                ✨ v15版：精确时间安排 + 交通互斥 + 无障碍优化 + 平滑交互！
            </p>
        </div>

        <div class="footer">
            <p>✨ 南京黄山之旅 · 2026年 · 8天7晚深度旅行攻略 v15（完整优化版）</p>
        </div>
    </div>

    <!-- ==========================================
         图片放大模态框 - 加大关闭按钮，支持左右切换
         ========================================== -->
    <div class="modal" id="imageModal" onclick="closeModal(event)">
        <button class="modal-close" aria-label="关闭图片">×</button>
        <button class="modal-arrow left" onclick="changeImage(-1, event)" aria-label="上一张">‹</button>
        <img class="modal-img" id="modalImage" src="" alt="放大图片">
        <button class="modal-arrow right" onclick="changeImage(1, event)" aria-label="下一张">›</button>
    </div>

    <!-- 回到顶部按钮 - 平滑消失（opacity + visibility） -->
    <button class="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" aria-label="回到顶部">↑</button>

    <script>
        /* ==========================================
           图片数组 - 按天分组，支持多图切换
           索引对应HTML中的onclick调用
           ========================================== */
        const dayImages = {
            'day1': [
                'images/day1-ganxi.jpg',
                'images/day1-laomendong.jpg',
                'images/day1-qinhuai1.jpg',
                'images/day1-qinhuai2.jpg'
            ],
            'day2': [
                'images/day2-mingxiaoling.jpg',
                'images/day2-zhongshanling.jpg',
                'images/day2-wutong1.jpg',
                'images/day2-wutong2.jpg',
                'images/day2-nanda1.jpg',
                'images/day2-nanda2.jpg'
            ],
            'day3': [
                'images/day3-hongshan.jpg',
                'images/day3-jimingsi.jpg',
                'images/day3-xuanwuhu.jpg',
                'images/day3-nightride.jpg'  // 索引3：夜骑玄武湖
            ],
            'day4': [
                'images/day4-bowuyuan.jpg',
                'images/day4-zongtong1.jpg',
                'images/day4-zongtong2.jpg'
            ],
            'day5': [
                'images/day5-jinianguan.jpg',
                'images/day5-nanjing-eye1.jpg',  // 替换为新景点
                'images/day5-baoli-theatre.jpg'  // 替换为新景点
            ],
            'day6': [
                'images/day6-tangkou1.jpg',
                'images/day6-tangkou2.jpg',
                'images/day6-tangkou3.jpg'
            ],
            'day7': [
                'images/day7-yunhai1.jpg',
                'images/day7-yunhai2.jpg',
                'images/day7-shixinfeng.jpg',
                'images/day7-guangmingding.jpg',
                'images/day7-yingkesong.jpg'
            ],
            'day8': [
                'images/day8-tangkou-around.jpg'
            ]
        };
        let currentDay = '';
        let currentImageIndex = 0;

        /* ==========================================
           showSection - 显示指定板块，隐藏其他
           参数：sectionId - 板块ID（如 'home', 'day1', 'food' 等）
           ========================================== */
        function showSection(sectionId) {
            // 隐藏所有板块
            document.querySelectorAll('.section').forEach(section => {
                section.classList.remove('active');
            });
            // 显示目标板块
            document.getElementById(sectionId).classList.add('active');
            // 更新顶部导航按钮状态
            document.querySelectorAll('.top-nav .nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            // 更新底部Tab状态
            updateBottomTab(sectionId);
            // 平滑滚动到顶部
            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        /* ==========================================
           enterItinerary - 点击"进入行程"按钮时调用
           显示Day1行程
           ========================================== */
        function enterItinerary() {
            showSection('day1');
            document.querySelector('.top-nav .nav-btn[onclick*="day1"]').classList.add('active');
        }

        /* ==========================================
           switchTab - 底部Tab切换
           参数：tabName - Tab名称（'itinerary', 'food', 'hotel' 等）
           ========================================== */
        function switchTab(tabName) {
            // 更新Tab按钮状态
            document.querySelectorAll('.bottom-tab .tab-item').forEach(tab => {
                tab.classList.remove('active');
            });
            event.target.closest('.tab-item').classList.add('active');
            // 根据Tab名称确定要显示的板块
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

        /* ==========================================
           updateBottomTab - 根据当前板块更新底部Tab状态
           参数：sectionId - 当前板块ID
           ========================================== */
        function updateBottomTab(sectionId) {
            // 清除所有Tab的active状态
            document.querySelectorAll('.bottom-tab .tab-item').forEach(tab => {
                tab.classList.remove('active');
            });
            // 映射板块ID到Tab名称
            const tabMap = {
                'day1': 'itinerary', 'day2': 'itinerary', 'day3': 'itinerary', 'day4': 'itinerary',
                'day5': 'itinerary', 'day6': 'itinerary', 'day7': 'itinerary', 'day8': 'itinerary',
                'food': 'food', 'hotel': 'hotel', 'luggage': 'luggage', 'avoid': 'avoid', 'booking': 'booking', 'emergency': 'emergency'
            };
            // 激活对应的Tab
            const targetTab = document.querySelector(`.bottom-tab .tab-item[data-tab="${tabMap[sectionId]}"]`);
            if (targetTab) targetTab.classList.add('active');
        }

        /* ==========================================
           toggleCard - 切换景点卡片/交通卡片的折叠状态
           参数：card - 被点击的卡片元素
           ========================================== */
        function toggleCard(card) {
            card.classList.toggle('collapsed');
        }

        /* ==========================================
           toggleTransportCard - 交通卡片互斥逻辑
           打开一张交通卡片时，自动折叠其他所有交通卡片
           参数：clickedCard - 被点击的交通卡片
           ========================================== */
        function toggleTransportCard(clickedCard) {
            // 切换当前卡片的折叠状态
            clickedCard.classList.toggle('collapsed');
            // 如果当前卡片被展开（不是collapsed），则关闭其他交通卡片
            if (!clickedCard.classList.contains('collapsed')) {
                document.querySelectorAll('.transport-card').forEach(card => {
                    if (card !== clickedCard && !card.classList.contains('collapsed')) {
                        card.classList.add('collapsed');
                    }
                });
            }
        }

        /* ==========================================
           openModal - 打开图片放大模态框
           参数：day - 日期（如 'day1'）
                 index - 图片索引
           ========================================== */
        function openModal(day, index) {
            currentDay = day;
            currentImageIndex = index;
            document.getElementById('modalImage').src = dayImages[day][index];
            document.getElementById('imageModal').classList.add('active');
        }

        /* ==========================================
           changeImage - 切换模态框中的图片（上一张/下一张）
           参数：direction - 方向（-1：上一张，1：下一张）
                 event - 事件对象
           ========================================== */
        function changeImage(direction, event) {
            event.stopPropagation();
            const images = dayImages[currentDay];
            currentImageIndex = (currentImageIndex + direction + images.length) % images.length;
            document.getElementById('modalImage').src = images[currentImageIndex];
        }

        /* ==========================================
           closeModal - 关闭图片模态框
           点击模态框背景或关闭按钮时调用
           参数：event - 事件对象
           ========================================== */
        function closeModal(event) {
            if (event.target === document.getElementById('imageModal') || 
                event.target.classList.contains('modal-close')) {
                document.getElementById('imageModal').classList.remove('active');
                // 不清空src，方便下次快速打开
            }
        }

        /* ==========================================
           showCategory - 切换行李清单的分类显示
           参数：category - 分类名称（'all', 'doc', 'city', 'mountain'）
           ========================================== */
        function showCategory(category) {
            // 更新分类按钮状态
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            // 显示对应的分类列表
            document.querySelectorAll('.category-list').forEach(list => {
                list.classList.remove('active');
            });
            document.getElementById(`category-${category}`).classList.add('active');
        }

        /* ==========================================
           toggleBookingStatus - 切换酒店预订状态（待预订 ↔ 已预订）
           参数：statusSpan - 被点击的状态标签
           ========================================== */
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

        /* ==========================================
           回到顶部按钮 - 平滑消失（opacity + visibility）
           滚动超过300px时显示，否则隐藏
           ========================================== */
        window.addEventListener('scroll', function() {
            const backToTop = document.querySelector('.back-to-top');
            if (window.scrollY > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        /* ==========================================
           行李清单 - 勾选状态本地存储
           使用localStorage保存勾选状态
           ========================================== */
        document.querySelectorAll('.checklist input[type="checkbox"]').forEach(checkbox => {
            const key = checkbox.parentElement.textContent.trim();
            checkbox.checked = localStorage.getItem(key) === 'true';
            checkbox.addEventListener('change', function() {
                localStorage.setItem(key, this.checked);
            });
        });

        /* ==========================================
           打印函数 - 带提示
           ========================================== */
        function printItinerary() {
            alert('建议用Chrome打印，勾选"背景图形"以保留卡片阴影');
            window.print();
        }

        /* ==========================================
           每日卡片滑动切换（移动端）- 带边界震动
           ========================================== */
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
                        // 边界震动反馈
                        if (navigator.vibrate) { navigator.vibrate(50); }
                    }
                }
            }
        });

        /* ==========================================
           updateNavButton - 更新顶部导航按钮状态
           参数：sectionId - 目标板块ID
           ========================================== */
        function updateNavButton(sectionId) {
            document.querySelectorAll('.top-nav .nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            const targetBtn = document.querySelector(`.top-nav .nav-btn[onclick="showSection('${sectionId}')"]`);
            if (targetBtn) targetBtn.classList.add('active');
        }
    </script>
</body>
</html>'''

# 写入文件
with open(file_path, 'a', encoding='utf-8') as f:
    f.write(remaining_content)

print('v15-final.html 剩余部分写入完成！')
print('文件位置：', file_path)
