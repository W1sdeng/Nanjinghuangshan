# 一寸 — 实施计划

> 本计划面向 AI 开发者，按阶段拆分为小而具体的步骤。
> 每一步都包含验证指令，**不能跳过测试直接进入下一步**。

---

## 目录

- [Phase 0 — 脚手架与基础设施](#phase-0--脚手架与基础设施)
- [Phase 1 — 目标与任务 CRUD + 今日一页](#phase-1--目标与任务-crud--今日一页)
- [Phase 2 — 弹性执行与柔性调整](#phase-2--弹性执行与柔性调整)
- [Phase 3 — 状态感知与智能推荐](#phase-3--状态感知与智能推荐)
- [Phase 4 — 回顾与复盘](#phase-4--回顾与复盘)
- [Phase 5 — AI 拆解与科目模板](#phase-5--ai-拆解与科目模板)
- [Phase 6 — 效能增强](#phase-6--效能增强)
- [Phase 7 — 打磨与内测](#phase-7--打磨与内测)

---

## Phase 0 — 脚手架与基础设施

### Step 0.1：创建 Flutter 项目

**指令**：
1. 在 `math/` 目录下执行 `flutter create --org com.yicun --project-name yicun .`
2. 确保项目在 `lib/` 根目录有 `main.dart`，在 `test/` 根目录有 `widget_test.dart`
3. 删除默认的计数示例代码（CounterApp），保留干净的 `main.dart`

**验证**：
- 运行 `flutter analyze`，无错误
- 运行 `flutter test`，至少通过一个占位测试
- 运行 `flutter run -d chrome`（或模拟器），看到一个空白页面

---

### Step 0.2：配置 pubspec.yaml 依赖

**指令**：
1. 打开 `pubspec.yaml`，按 tech-stack.md 第 2 节添加所有核心依赖
2. 运行 `flutter pub get`，确保所有依赖安装成功
3. 运行 `flutter pub outdated` 确认无重大版本冲突

**验证**：
- `flutter pub get` 退出码为 0
- `flutter analyze` 无错误（即使有未使用的 import 警告也允许，后面会用到）
- `flutter test` 仍通过

---

### Step 0.3：搭建项目目录结构

**指令**：
1. 在 `lib/` 下按以下结构创建所有目录（空目录放 `.gitkeep`）：
   - `core/theme/`、`core/constants/`、`core/utils/`、`core/router/`
   - `data/database/tables/`、`data/database/daos/`、`data/local/`、`data/remote/`、`data/repositories/`
   - `domain/models/`、`domain/services/`
   - `presentation/providers/`、`presentation/pages/today/`、`presentation/pages/goal_detail/`、`presentation/pages/review/`、`presentation/pages/weekly_report/`、`presentation/pages/focus/`、`presentation/pages/settings/`、`presentation/widgets/`
2. 在 `test/` 下创建对应测试目录结构

**验证**：
- `flutter analyze` 无错误
- 所有 `_test.dart` 目录存在但暂无测试文件（`flutter test` 输出 0 测试跳过）

---

### Step 0.4：搭建主题系统

**指令**：
1. 在 `core/theme/app_colors.dart` 中定义设计文档第 7.2 节的色值常量：
   - 主色系：鼠尾草绿、陶土棕、雾霾蓝
   - 完成度三色：保底蓝 `#A8C8E8`、标准橙 `#E8B88A`、冲刺金棕 `#C8A878`
   - 背景色：暖白 `#FAF8F5`
   - 文字色：深灰 `#2D2D2D`、中灰 `#6B6B6B`
2. 在 `core/theme/app_typography.dart` 中定义字体层级常量
3. 在 `core/theme/app_theme.dart` 中组装 `ThemeData`，设置圆角 12px、轻投影、卡片底色
4. 在 `main.dart` 中应用该主题

**验证**：
- `flutter analyze` 无错误
- 写一个 Widget 测试：创建 `MaterialApp` 使用该主题，渲染一个 `Container` 带卡片圆角，运行 `flutter test` 通过

---

### Step 0.5：实现 Result 类型

**指令**：
1. 在 `domain/models/result.dart` 中定义 sealed class `Result<T>`，包含 `Success<T>` 和 `Failure<T>` 两个子类
2. `Success` 携带 `T data`，`Failure` 携带 `String message` 和可选 `Object? error`

**验证**：
- 写单元测试覆盖：
  - `Success` 可以解构出 `data`
  - `Failure` 可以读取 `message` 和 `error`
  - 使用 `when` 模式匹配能正确区分成功和失败
- `flutter test` 通过，且覆盖率行覆盖 100%

---

### Step 0.6：定义 drift 数据库表

**指令**：
1. 在 `data/database/tables/` 下依次创建 5 个表定义文件：
   - `goals_table.dart`：字段 id, title, subject, motivation, deadline(可空), status, created_at
   - `tasks_table.dart`：字段 id, goal_id(外键), title, criteria_minimal, criteria_standard, criteria_冲刺, current_intensity, progress, status, completion_quality(可空), scheduled_date, last_interrupt_at(可空), interrupt_note(可空), carried_from(可空), consecutive_days, estimated_duration, actual_duration, created_at
   - `sessions_table.dart`：字段 id, task_id(外键), start_time, end_time(可空), duration_planned, duration_actual, mood_before(可空), mood_after(可空)
   - `day_records_table.dart`：字段 id, date(唯一), energy(可空), mood(可空), reaction_time(可空), recommended_intensity(可空), reflection_reason(可空), reflection_suggestion(可空), total_focus_minutes
   - `templates_table.dart`：字段 id, subject, name, is_official, contributor(可空), status(可空), usage_count, task_templates_json(存储 JSON 字符串)
2. 在 `data/database/app_database.dart` 中定义 `AppDatabase` 类，继承 drift 的 `_$AppDatabase`，包含上述 5 张表
3. 设置 `schemaVersion = 1`，`onUpgrade` 回调留空

**验证**：
- 运行 `dart run build_runner build` 生成数据库代码，无错误
- 写 DAO 测试：创建内存数据库 `await AppDatabase.forTest(memory)`，验证建表后表存在（通过 `select(id)` 不抛异常）
- `flutter test` 通过

---

### Step 0.7：定义 freezed 领域模型

**指令**：
1. 在 `domain/models/` 下按设计文档第 4 节定义 freezed 模型：
   - `goal.dart`：Goal 类，匹配 goals 表字段（不含 tasks 列表）
   - `task.dart`：Task 类，匹配 tasks 表字段
   - `session.dart`：Session 类，匹配 sessions 表字段
   - `day_record.dart`：DayRecord 类，匹配 day_records 表字段
   - `template.dart`：Template 类 + TaskTemplate 内部类，匹配 templates 表字段
   - `badge.dart`：Badge 类，含 id, type, level, unlocked_at, progress
2. 所有模型使用 `@freezed` 注解，实现 `copyWith`、`==`、`hashCode`、JSON 序列化

**验证**：
- `dart run build_runner build` 成功，无错误
- 写单元测试：创建一个完整模型实例，验证 `copyWith` 修改单一字段不改变其他字段
- 写单元测试：models 层不导入任何 Flutter 包（检查 import 列表）
- `flutter test` 通过

---

### Step 0.8：实现核心工具函数

**指令**：
1. 在 `core/utils/date_utils.dart` 中实现：
   - `todayDateString()` → 返回 "2026-05-12" 格式
   - `timeBasedGreeting()` → 返回 "早安"/"下午好"/"晚上好"/"深夜了"
   - `weekNumber()` → 返回今年第几周
2. 在 `core/utils/text_utils.dart` 中实现：
   - `warmTermMap`：常规说法 → 一寸说法的映射表（设计文档第 5 节）
   - `translateToWarm(String term)`：根据映射表转换说法
3. 在 `core/constants/app_strings.dart` 中定义文案常量

**验证**：
- 写单元测试覆盖 `date_utils.dart` 中 3 个函数
- 写单元测试：`translateToWarm("任务延期")` 返回 `"带到明天"`
- 写单元测试：`translateToWarm("不存在的词")` 返回原词
- `flutter test` 通过

---

### Phase 0 完成检查

- [ ] `flutter analyze` 零错误
- [ ] `flutter test` 全部通过
- [ ] `dart run build_runner build` 无错误
- [ ] 数据库表定义与设计文档数据模型一致
- [ ] freezed 模型无手动修改生成的 `.g.dart` 文件

---

## Phase 1 — 目标与任务 CRUD + 今日一页

### Step 1.1：实现 Goal DAO

**指令**：
1. 在 `data/database/daos/goal_dao.dart` 中实现：
   - `insertGoal(Goal goal)`：插入一条目标记录
   - `getGoal(String id)`：按 ID 查询
   - `getAllGoals()`：查询所有目标，按 created_at 降序
   - `updateGoal(Goal goal)`：更新目标
   - `deleteGoal(String id)`：删除目标
   - `getActiveGoals()`：查询 status 为 active 的目标
2. 使用 `@UseRowClass(Goal)` 将查询结果自动映射到 freezed 模型

**验证**：
- 使用 drift 内存数据库写 DAO 测试：
  - 插入目标 → 查询验证字段值正确
  - 更新目标标题 → 查询验证已更新
  - 删除目标 → 查询返回空
  - 插入 3 个目标后 `getAllGoals()` 返回 3 条
- `flutter test` 通过

---

### Step 1.2：实现 Task DAO

**指令**：
1. 在 `data/database/daos/task_dao.dart` 中实现：
   - `insertTask(Task task)`：插入一条任务
   - `getTask(String id)`：按 ID 查询
   - `getTasksByGoalId(String goalId)`：查询某目标下的所有任务
   - `getTasksByDate(String date)`：查询某日期的所有任务（按 scheduled_date）
   - `getCarriedOverTasks()`：查询 status 为 carried_over 的任务
   - `updateTask(Task task)`：更新任务
   - `deleteTask(String id)`：删除任务
   - `getIncompleteTasksBefore(String date)`：查询指定日期前未完成的任务

**验证**：
- 写 DAO 测试（内存数据库）：
  - 插入一个 Goal，再插入 2 个关联 Task → `getTasksByGoalId` 返回 2 条
  - 更新任务 progress → 验证值已更新
  - 查询今日任务 → 验证 scheduled_date 过滤正确
- `flutter test` 通过

---

### Step 1.3：实现 GoalRepository

**指令**：
1. 在 `data/repositories/goal_repository.dart` 中实现：
   - 所有方法返回 `Result<T>` 类型
   - `createGoal(title, subject, motivation, deadline?)`：调用 Goal DAO
   - `getGoal(id)` → `Result<Goal>`
   - `getAllActiveGoals()` → `Result<List<Goal>>`
   - `updateGoal(goal)` → `Result<void>`
   - `deleteGoal(id)` → `Result<void>`
   - `getYesterdayCompletionRate()` → 返回昨日完成度百分比

**验证**：
- 写测试：使用内存数据库的 Repository 测试
  - 创建目标 → `Success` 且 data.id 不为空
  - 创建后 `getAllActiveGoals` 包含该目标
  - 删除后再查询返回 `Failure`
- `flutter test` 通过

---

### Step 1.4：实现 TaskRepository

**指令**：
1. 在 `data/repositories/task_repository.dart` 中实现：
   - 所有方法返回 `Result<T>` 类型
   - `createTask(...)`：按设计文档字段创建任务
   - `getTasksForToday()`：返回 `scheduled_date == today` 的任务列表
   - `getCarryOverTasks()`：返回接力任务
   - `updateTask(...)`、`deleteTask(...)`
   - `markCompleted(taskId, completionQuality)`：设置 status 为 completed，记录 quality
   - `carryOver(taskId)`：设置 status 为 carried_over，保留原数据的 40% 等进度
   - `delayToTomorrow(taskId)`：保留原有记录，创建新记录到明天

**验证**：
- 写测试：
  - 创建任务 → 验证 scheduled_date 设置正确
  - 调用 `carryOver` → 任务 status 变为 carried_over，consecutive_days 保留
  - 调用 `markCompleted` → quality 正确记录
- `flutter test` 通过

---

### Step 1.5：配置 go_router 基本路由

**指令**：
1. 在 `core/router/app_router.dart` 中配置路由：
   - `/` → TodayPage
   - `/goal/new` → GoalCreatePage
   - `/goal/:id` → GoalDetailPage
   - `/goal/:id/edit` → GoalEditPage
   - `/review` → ReviewPage
   - `/weekly` → WeeklyReportPage
   - `/settings` → SettingsPage
2. 所有页面先放占位 `Scaffold` + `Text('页面名')`
3. 在 `app.dart` 中初始化 `MaterialApp.router` 使用 go_router

**验证**：
- `flutter analyze` 无错误
- 运行 App，验证 `/` 路由渲染 TodayPage 占位内容
- 手动在浏览器 `/goal/new` 验证路由跳转

---

### Step 1.6：实现 Goal 创建页面

**指令**：
1. 在 `presentation/pages/goal_detail/` 下创建 `goal_create_page.dart`
2. 页面包含：
   - 标题输入框（"这个目标叫什么？"）
   - 科目选择器（英语/数学/政治/专业课 + "其他"）
   - 动机输入框（"为什么想做这件事？"）— 可选，placeholder 来自设计文档
   - 截止日期选择器（可选）
   - 底部「创建目标」按钮
3. 创建后跳转到目标详情页

**验证**：
- 写 Widget 测试：
  - 渲染页面 → 验证标题、科目选择器、创建按钮存在
  - 输入标题 "考研英语"、选择科目 "英语" → 点击创建 → 验证 `go_router` 跳转到详情页
- `flutter test` 通过

---

### Step 1.7：实现 Goal 详情页面（含 Task 列表）

**指令**：
1. 在 `presentation/pages/goal_detail/` 下创建 `goal_detail_page.dart`
2. 页面展示：
   - 目标标题和动机
   - 完成标准三档文本展示
   - 当前进度条
   - 已坚持天数
   - 关联任务列表
   - 底部「+ 新任务」按钮
3. 任务列表项显示：任务名、进度、强度档位标签（保底/标准/冲刺）

**验证**：
- 写 Widget 测试：
  - 创建目标 → 导航到详情页 → 验证标题显示正确
  - 添加 2 个任务 → 验证列表渲染 2 行
- `flutter test` 通过

---

### Step 1.8：实现 Task 创建页面

**指令**：
1. 创建 `task_create_page.dart`
2. 页面包含：
   - 任务标题输入框
   - 完成标准三档输入（3 个文本域）：保底 / 标准 / 冲刺
   - 科目选择（继承目标科目）
   - 预计耗时（分钟）输入
   - 是否适合作为保底任务（开关）
   - 创建按钮
3. 创建成功后返回详情页并刷新任务列表

**验证**：
- 写 Widget 测试：
  - 渲染页面 → 验证三档输入框存在
  - 填写并创建 → 验证返回详情页且任务列表新增一项
- `flutter test` 通过

---

### Step 1.9：实现今日一页 Provider

**指令**：
1. 在 `presentation/providers/today_providers.dart` 中定义 Riverpod Provider：
   - `todayPageDataProvider`：聚合以下数据
     - 今日任务列表（`taskRepository.getTasksForToday()`）
     - 保底防线任务（从今日任务中选 estimated_duration 最短的）
     - 接力任务列表（`taskRepository.getCarryOverTasks()`）
     - 昨日完成度
     - 时段问候语
2. 使用 `@riverpod` 注解，生成 `.g.dart`

**验证**：
- `dart run build_runner build` 无错误
- 写 Provider 测试：注入 mock TaskRepository，验证 Provider 返回的数据结构包含 5 个字段
- `flutter test` 通过

---

### Step 1.10：构建今日一页 UI

**指令**：
1. 在 `presentation/pages/today/today_page.dart` 中构建完整首页 UI：
   - 顶部：时段问候语 + 激励短句
   - 「今日必做」区域：任务卡片列表（每个卡片显示标题、科目图标、进度）
   - 「保底防线」区域：单独突出显示一个任务，带锁图标
   - 「继续上次」区域：如有接力任务则显示，显示进度百分比
   - 底部状态入口：3 个情感按钮（😊不错 / 😐还行 / 😴累）
2. 任务卡片支持左滑完成、右滑延期
3. 遵循设计文档第 3.1.1 节的页面布局，按 Neo-minimalism 风格实现

**验证**：
- 写 Widget 测试：
  - mock 今日有 2 个任务 → 验证渲染 2 个任务卡片
  - mock 有接力任务 → 验证「继续上次」区域显示
  - mock 无今日任务 → 验证「保底防线」显示空状态文案
- `flutter test` 通过
- 手动运行 App，验证 UI 布局与设计文档一致

---

### Step 1.11：实现任务状态切换（完成 / 延期）

**指令**：
1. 在任务卡片上实现手势交互：
   - **左滑**：弹出「点亮地标」按钮，点击后调用 `markCompleted`
   - **右滑**：弹出「带到明天」按钮，点击后调用 `delayToTomorrow`
2. 完成后显示激励提示（SnackBar 或底部 Sheet），文案来自设计文档第 3.2.4 节
3. 延期后卡片从今日列表消失，保底防线自动切换为下一个最短任务

**验证**：
- 写 Widget 测试：
  - 左滑 → 点击「点亮地标」→ 验证 `markCompleted` 被调用
  - 右滑 → 点击「带到明天」→ 验证 `delayToTomorrow` 被调用 → SnackBar 显示 "休息一下，明天继续。"
  - 保底防线任务完成后 → 验证防线自动切换到下一个任务
- `flutter test` 通过

---

### Phase 1 完成检查

- [ ] 目标 CRUD 完整可用（创建/查看/编辑/删除）
- [ ] 任务 CRUD 完整可用
- [ ] 今日一页展示今日任务、保底防线、接力任务
- [ ] 左滑完成任务、右滑延期任务
- [ ] `flutter analyze` 零错误，`flutter test` 全部通过

---

## Phase 2 — 弹性执行与柔性调整

### Step 2.1：实现启动陪伴模式

**指令**：
1. 在 `core/constants/` 下创建 `companion_templates.dart`，按设计文档第 3.1.3 节的陪伴模板表硬编码预置模板
2. 在 `presentation/widgets/` 下创建 `companion_mode_sheet.dart`：
   - 接受 `Task` 对象作为参数
   - 按科目+任务类型匹配陪伴模板
   - 分三步展示：最小行动指令 → 第一步确认 → 恭喜启动
   - 第三步提供「继续」（跳转到专注模式）和「关闭」（返回首页）
3. 将「继续」按钮连接到 FocusTimerPage（占位，Phase 6 实现）
4. 在 `settings_page.dart` 中添加「跳过陪伴模式」开关，状态存入 Hive

**验证**：
- 写 Widget 测试：
  - 传入数学刷题任务 → 验证第一步文案包含「打开真题册」
  - 点击「准备好了」→ 验证切换到第二步
  - 点击「做完了」→ 验证切换到第三步（恭喜启动）
  - 点击「继续」→ 验证路由跳转到 `/focus`
  - 点击「关闭」→ 验证返回首页
- `flutter test` 通过

---

### Step 2.2：实现任务接力（carry-over）

**指令**：
1. 在 TaskRepository 中：
   - `carryOver(taskId)`：将原任务 status 设为 carried_over，记录中断点，保留进度
   - `getCarryOverTasks()`：返回 status 为 carried_over 的任务列表
2. 这些任务在今日一页的「继续上次」区域显示
3. 点击「一键接续」→ 进入启动陪伴模式，上下文包含上次中断点 note
4. 接力任务的进度在原基础上继续增长，不归零

**验证**：
- 集成测试：
  - 创建任务 → 进度设为 40% → 调用 carryOver → 查询接力列表包含该任务
  - 接续后完成任务 → 验证 progress 变为 100%
  - 连续接力 2 次 → 验证任务仍在列表，不产生嵌套
- `flutter test` 通过

---

### Step 2.3：实现降级完成

**指令**：
1. 在任务详情页实现强度选择器（当前 Step 只做逻辑，UI 滑杆在 Step 2.4）：
   - 用户在任务执行时可手动将强度从「标准」降低到「保底」
   - 降级后完成标准文案切换为保底版
   - 完成任务时传入 `completionQuality: minimal`
2. 降级完成后的激励文案使用设计文档第 3.2.4 节「场景四」的内容

**验证**：
- 写测试：
  - 任务初始强度为 standard → 降级为 minimal → 验证 current_intensity 变更
  - 以 minimal quality 完成任务 → 验证 DayRecord 中该任务标记为保底
- `flutter test` 通过

---

### Step 2.4：实现难度滑杆 UI

**指令**：
1. 在 `presentation/widgets/intensity_slider.dart` 中实现三档滑杆：
   - 三档定位：保底/标准/冲刺，不可滑动到中间值
   - 拖到「保底」时完成标准切换为保底描述
   - 拖到「冲刺」时显示鼓励文案「今天状态不错！」
   - 不记录切换历史，不提示「降级」
2. 集成到目标卡片详情页的任务进度区域

**验证**：
- 写 Widget 测试：
  - 滑块默认在「标准」位 → 验证显示标准文案
  - 拖动到「保底」→ 验证完成标准切换为保底描述
  - 拖动到「冲刺」→ 验证显示鼓励文案
  - 反复拖动 → 验证无历史记录
- `flutter test` 通过

---

### Step 2.5：实现切道（中途切换调剂任务）

**指令**：
1. 在 `core/constants/` 中预置调剂任务池（3-5 个微小行动）：
   - "背 5 个单词 · 3min"
   - "整理一条笔记 · 5min"
   - "回顾昨天的进度 · 2min"
   - "做一道选择题 · 1min"
2. 在 `presentation/widgets/switch_track_sheet.dart` 中实现：
   - 专注中点击暂停 → 弹出底部 Sheet
   - 显示调剂任务选项列表
   - 选择后开始 3 分钟倒计时
   - 完成后显示「现在感觉好点了吗？」→ 提供「继续原来的任务」和「今天就到这里吧」
3. 调剂任务不计入今日完成度

**验证**：
- 写 Widget 测试：
  - 专注中暂停 → 验证 Sheet 弹出，显示 3 个调剂选项
  - 选择调剂任务 → 验证开始倒计时
  - 完成后 → 验证两个按钮存在
  - 选择「今天就到这里吧」→ 验证返回首页且今日任务列表不变
- `flutter test` 通过

---

### Step 2.6：实现延时逻辑（带到明天）

**指令**：
1. 完善 `delayToTomorrow(taskId)` 逻辑：
   - 当前任务保留原有记录，status 设为 carried_over
   - 创建新任务副本到 `scheduled_date = tomorrow`
   - 新任务保留原任务的 consecutive_days 火种
   - 连续延时超过 3 次 → 弹出建议：「这个任务连续延后了几天，要不要拆小一点？」
2. 在今日一页的右滑操作触发此逻辑

**验证**：
- 写测试：
  - 今天有任务 → 调用 delayToTomorrow → 验证明天多出一条任务
  - 验证原任务的 status 变为 carried_over
  - 连续延时 4 次 → 验证建议弹窗出现
- `flutter test` 通过

---

### Phase 2 完成检查

- [ ] 启动陪伴模式三步流程完整
- [ ] 任务接力（继续上次）可用
- [ ] 降级完成不触发负罪感
- [ ] 难度滑杆三档切换正确
- [ ] 切道调剂任务可用
- [ ] 带火种延时可用

---

## Phase 3 — 状态感知与智能推荐

### Step 3.1：实现 DayRecord DAO

**指令**：
1. 在 `data/database/daos/day_record_dao.dart` 中实现：
   - `upsertDayRecord(DayRecord record)`：按 date 唯一键插入或更新
   - `getDayRecord(String date)`：查询某天记录
   - `getRecentDayRecords(int days)`：查询最近 N 天的记录
   - `getMonthDayRecords(int year, int month)`：查询某月所有记录
   - `updateReflection(String date, String reason, String suggestion)`：更新复盘字段

**验证**：
- 写 DAO 测试：
  - 插入某天的记录 → 按 date 查询验证
  - 再次 upsert 同天记录 → 验证覆盖而非新增
  - 查询最近 7 天，只有 3 天有数据 → 返回 3 条
- `flutter test` 通过

---

### Step 3.2：实现状态感知模型与枚举

**指令**：
1. 在 `domain/models/` 中添加枚举类型：
   - `EnergyLevel`：充沛 / 正常 / 疲惫
   - `MoodLevel`：平静 / 焦虑 / 低落
2. 在 `domain/models/` 中添加 `StateAssessment` freezed 模型：
   - `energy: EnergyLevel`
   - `mood: MoodLevel`
   - `reactionTimes: List<int>`（反应测试的 3 次点击时间，毫秒）
   - `averageReactionTime: int`（计算属性）
3. 在 `domain/models/` 中添加 `IntensityRecommendation` freezed 模型：
   - `intensity: String`（minimal / standard / 冲刺 / rest）
   - `message: String?`

**验证**：
- `dart run build_runner build` 无错误
- 写单元测试：StateAssessment 计算 averageReactionTime 正确
- write 测试：IntensityRecommendation 创建时 message 可为 null
- 验证所有 model 不导入 Flutter 包

---

### Step 3.3：构建状态感知 UI

**指令**：
1. 在 `presentation/widgets/mood_selector.dart` 中实现：
   - 今日一页底部的 3 个情感按钮
   - 点击后触发状态感知流程
2. 在 `presentation/widgets/state_perception_sheet.dart` 中实现：
   - **阶段一**：精力选择（3 个按钮：充沛/正常/疲惫）
   - **阶段二**：情绪选择（3 个按钮：平静/焦虑/低落）
   - **阶段三**：反应测试（可选）— 屏幕中央按钮，「点一下屏幕，越快越好」，3 次随机间隔，取平均值
   - **阶段四**：推荐结果显示

**验证**：
- 写 Widget 测试：
  - 点击今日一页底部状态按钮 → 验证弹出 Sheet
  - 选择「充沛」→ 验证进入情绪选择阶段
  - 选择「平静」→ 验证进入反应测试阶段
  - 完成 3 次点击 → 验证进入推荐结果阶段
  - 验证推荐结果文案正确渲染
- `flutter test` 通过

---

### Step 3.4：实现规则引擎

**指令**：
1. 在 `domain/services/intensity_engine.dart` 中实现纯函数推荐引擎：
   - `recommend(StateAssessment assessment, DayRecord yesterdayRecord, int consecutiveHighIntensityDays)` 返回 `IntensityRecommendation`
   - 规则优先级（按顺序匹配）：
     a. 连续 3 天高强度 → 推荐「标准」，文案"你最近 3 天都是冲刺，今天试试标准模式？"
     b. 昨日仅保底完成 → 推荐「保底」，文案"昨天只完成了保底，今天建议先守住一个核心。"
     c. 精力疲惫 + 情绪焦虑/低落 → 推荐「休息」，文案"看起来很疲惫，今天要不要休息一天？"
     d. 某科目拖延率 > 60% → 推荐「标准」，文案"{科目}拖延率较高，今天优先安排吗？"
     e. 默认 → 推荐「标准」
2. 引擎不能有副作用（纯函数）

**验证**：
- 写单元测试覆盖 5 条规则，覆盖率 100%：
  - 连续 3 天高强度 → 验证返回 standard
  - 昨日保底完成 → 验证返回 minimal
  - 精力疲惫 + 情绪焦虑 → 验证返回 rest
  - 某科拖延率 70% → 验证文案包含该科目名
  - 无特殊情况 → 返回 standard
  - 精力充沛 + 昨日冲刺完成 + 无拖延科 → 默认 standard
- `flutter test` 通过

---

### Step 3.5：实现 StateRepository

**指令**：
1. 在 `data/repositories/state_repository.dart` 中实现：
   - `saveStateAssessment(StateAssessment assessment)`：保存到当日 DayRecord
   - `getStateForToday()`：获取当日状态
   - `getRecommendation()`：调用规则引擎，返回推荐
   - `getConsecutiveHighIntensityDays()`：计算连续高强度天数
   - 所有方法使用 Result 类型

**验证**：
- 写测试：
  - 保存状态 → 查询今日状态验证
  - 连续 3 天冲刺记录 → `getConsecutiveHighIntensityDays` 返回 3
  - 无昨日记录时推荐结果正确
- `flutter test` 通过

---

### Step 3.6：状态推荐与今日一页联动

**指令**：
1. 在 today_providers 中增加状态推荐逻辑：
   - 用户完成状态感知后，Provider 自动刷新
   - 推荐结果影响今日任务展示：
     - 推荐「保底」→ 所有任务卡片标记为保底模式
     - 推荐「休息」→ 显示休息建议卡片，任务列表折叠
     - 推荐「冲刺」→ 隐藏保底防线区域
2. 今日一页 UI 适配推荐结果

**验证**：
- 写 Provider 测试：
  - Mock 规则引擎返回「保底」→ 验证 Provider 中 todayTasks 的 intensity 已变更
  - Mock 规则引擎返回「休息」→ 验证 Provider 包含 restCard 字段
- `flutter test` 通过

---

### Phase 3 完成检查

- [ ] 状态感知流程完整（主观自评 + 反应测试 + 推荐结果）
- [ ] 规则引擎 5 条规则覆盖
- [ ] 推荐结果影响今日一页展示
- [ ] 纯函数引擎可独立测试

---

## Phase 4 — 回顾与复盘

### Step 4.1：实现回顾页 Provider

**指令**：
1. 在 `presentation/providers/` 下创建 `review_providers.dart`：
   - `monthRecordsProvider(year, month)`：查询某月所有 DayRecord
   - `selectedDayRecordProvider(date)`：查询特定日期的详情
   - `dayTasksProvider(date)`：查询某天的所有任务

**验证**：
- `dart run build_runner build` 无错误
- 写 Provider 测试：mock DAO 返回指定月份数据 → 验证 Provider 返回正确

---

### Step 4.2：构建回顾页热力图

**指令**：
1. 在 `presentation/widgets/heatmap_grid.dart` 中实现月度热力图：
   - 按设计文档第 3.3.1 节布局：5-6 列网格
   - 色值映射：无记录 → `#F0EDE8`、保底 → `#A8C8E8`、标准 → `#E8B88A`、冲刺 → `#C8A878`
   - 方格可选中的正方形（44×44px），圆角 6px
   - 点击某天 → 触发选中回调
2. 在 `presentation/pages/review/review_page.dart` 中组装：
   - 头部：年/月切换器（左右箭头 + 年月文字）
   - 热力图
   - 已选中的日卡片

**验证**：
- 写 Widget 测试：
  - 传入 30 条 DayRecord → 验证渲染 30+ 个方格
  - 验证保底/标准/冲刺颜色映射正确
  - 点击方格 → 验证选中回调触发
  - 切换月份 → 验证数据刷新
- `flutter test` 通过

---

### Step 4.3：构建日卡片详情

**指令**：
1. 在 `presentation/widgets/day_card.dart` 中实现：
   - 日期标题 + 星期
   - 已完成任务列表（带完成质量色标）
   - 未完成任务显示温和描述：「带到明天」/「降级完成」/「换条路走」
   - 底部：当日复盘小结（用户输入的文本）
   - 「复盘」按钮
2. 未完成任务不使用红叉，使用圆点+文字描述

**验证**：
- 写 Widget 测试：
  - 有 2 个已完成任务 → 验证显示 ✅ 图标和质量色标
  - 有 1 个未完成任务（carried_over）→ 验证显示「带到明天」
  - 有复盘小结文字 → 验证显示在底部
  - 「复盘」按钮存在 → 点击触发回调
- `flutter test` 通过

---

### Step 4.4：实现复盘改计划

**指令**：
1. 在 `presentation/widgets/reflection_sheet.dart` 中实现：
   - 标题：「今天为什么没完成？」
   - 多选选项（CheckboxListTile）：
     - "任务太大了"
     - "今天状态不好"
     - "安排不合理/太多了"
     - "单纯不想学"
     - "其他"
   - 选择后显示系统建议，按设计文档第 3.3.1 节建议表匹配
   - 「确认」按钮保存到 DayRecord
2. 系统建议根据选择自动动作：
   - 任务太大了 → 创建 2 个拆分后的子任务
   - 状态不好 → 设置明日该任务强度为保底
   - 安排不合理 → 调整明日任务顺序

**验证**：
- 写测试：
  - 选择「任务太大了」→ 验证 `reflection_reason` 正确存储，子任务被创建
  - 选择「状态不好」→ 验证明日该任务 default intensity 变为 minimal
  - 选择「单纯不想学」→ 验证调剂任务被推荐
- `flutter test` 通过

---

### Phase 4 完成检查

- [ ] 月度热力图渲染正确，色值匹配设计文档
- [ ] 日卡片展示任务详情，未完成显示温和文案
- [ ] 复盘改计划闭环可用
- [ ] 所有文案符合温度规范，无红叉 ❌

---

## Phase 5 — AI 拆解与科目模板

### Step 5.1：实现科目模板 DAO 与预置数据

**指令**：
1. 实现 `Template` 的 drift 表 DAO：CRUD + 按科目查询
2. 在 `data/database/app_database.dart` 的初始化回调中插入预置数据：
   - 英语 6 个模板
   - 数学 5 个模板
   - 政治 4 个模板
   - 专业课 3 个模板
3. 模板数据按设计文档第 3.2.2 节的规范编写

**验证**：
- 初始化数据库后 → 查询所有模板 → 返回 18 条
- 按科目过滤 → 各科目返回正确数量
- `flutter test` 通过

---

### Step 5.2：实现模板选择器 UI

**指令**：
1. 在任务创建流程中插入「从模板创建」入口：
   - 用户选择科目后 → 展示该科目下的模板列表
   - 选择模板 → 自动填入三档完成标准和预计耗时
   - 仍允许用户手动编辑
2. 模板卡片展示：模板名、预计耗时、使用次数

**验证**：
- 写 Widget 测试：
  - 选择科目「英语」→ 验证显示 6 个模板
  - 点击「背单词」模板 → 验证三档标准自动填入
  - 验证仍可手动编辑填入的文本
- `flutter test` 通过

---

### Step 5.3：实现 AI 客户端

**指令**：
1. 在 `data/remote/ai_client.dart` 中使用 dio 实现：
   - `decomposeGoal(String userInput)` 方法
   - 使用 DeepSeek 开放平台 API（免费模型）
   - 请求体包含 system prompt（设计文档第 3.2.3 节）
   - 超时设置 15 秒
   - 异常捕获返回 null
2. API key 通过环境变量或配置文件注入，不硬编码

**验证**：
- 写测试使用 mock 的 Dio（不发起真实网络请求）：
  - mock 成功响应 → `decomposeGoal` 返回解析后的 JSON 字符串
  - mock 网络超时 → 返回 null
  - mock API 返回格式错误 → 返回 null
- `flutter test` 通过

---

### Step 5.4：实现规则拆解器（本地兜底）

**指令**：
1. 在 `domain/services/decomposition_service.dart` 中实现：
   - `decompose(input, subject)` 方法
   - 先尝试模板匹配（按科目关键词）
   - 匹配到模板 → 按模板拆解为每日任务
   - 未匹配到 → 调用 AI Client
   - AI 失败 → 返回通用建议（"建议手动拆分为每天 2-3 小时的任务"）
2. 拆解结果缓存到 Hive（key = input 的 hash），缓存有效期 24 小时

**验证**：
- 写单元测试：
  - 输入「一周搞定马原」→ 匹配到政治模板 → 返回 5-7 天的任务列表
  - 输入「学英语」→ 未匹配模板，mock AI 返回 null → 降级返回通用建议
  - 相同输入重复调用 → 第二次命中缓存（验证 Hive 调用次数）
- `flutter test` 通过

---

### Step 5.5：实现拆解器 UI

**指令**：
1. 在今日一页或目标创建页添加「一键拆解」入口
2. 拆解交互流程：
   - 用户输入自然语言目标 → 点击「一键拆解」
   - 显示加载状态
   - 拆解结果以每日卡片列表展示
   - 用户可编辑/删除单个日期的任务
   - 确认后批量生成任务
3. 加载状态使用骨架屏

**验证**：
- 写 Widget 测试：
  - 点击「一键拆解」→ 验证加载状态和骨架屏显示
  - 加载完成 → 验证每日卡片列表渲染
  - 编辑某日任务 → 验证可修改
  - 确认 → 验证所有任务被创建
- `flutter test` 通过

---

### Phase 5 完成检查

- [ ] 18 个官方模板预置可用
- [ ] 模板选择器可自动填入三档标准
- [ ] AI 拆解可用，失败时降级到兜底建议
- [ ] 拆解结果缓存有效

---

## Phase 6 — 效能增强

### Step 6.1：实现轻量专注计时器

**指令**：
1. 在 `presentation/pages/focus/focus_page.dart` 中实现：
   - 时长选择：3 个预设按钮（10 分钟试试 / 15 分钟启动 / 30 分钟深度）+ 自定义输入
   - 选时后显示：「歇一会儿」按钮（暂停计时）
   - 计时中显示倒计时 + 关联任务名
   - 计时结束 → 自动记录时长到 Session 表
2. 暂停时弹出切道 Sheet（调用 Step 2.5 的组件）
3. 放弃计时使用「换条路走」文案

**验证**：
- 写 Widget 测试：
  - 选择「15 分钟启动」→ 验证倒计时显示 15:00
  - 点击「歇一会儿」→ 验证暂停，切道 Sheet 弹出
  - 计时结束 → 验证 Session 记录写入
  - 点击「换条路走」→ 验证退出计时，返回首页
- `flutter test` 通过

---

### Step 6.2：实现本周山径（周报）

**指令**：
1. 在 `domain/services/narrative_service.dart` 中实现叙事生成：
   - `generateWeeklyNarrative(List<DayRecord> weekRecords)` → 按设计文档第 3.3.2 节的规则生成一句话总结
2. 在 `presentation/pages/weekly_report/weekly_report_page.dart` 中构建周报 UI：
   - 顶部叙事结语
   - 数据概览卡片（推进天数、保底天数、总时长、最专注科目）
   - 情绪曲线图（使用 fl_chart 库）
   - 本周高光区域
   - 下周建议
3. 每周一自动生成，用户也可随时查看

**验证**：
- 写单元测试：
  - 周数据中数学完成度最高 → 叙事包含「数学」
  - 周四情绪最低但守住了保底 → 叙事包含「周四特别累但守住了保底」
  - 全部 7 天无数据 → 返回空周报
- 写 Widget 测试：周报各区域存在
- `flutter test` 通过

---

### Step 6.3：实现徽章系统

**指令**：
1. 在 `domain/services/badge_service.dart` 中实现：
   - `checkAndAward(List<DayRecord> recentRecords)` → 检查所有徽章条件
   - 设计文档第 3.3.3 节的 5 种徽章类型各实现 2-3 个等级
2. 徽章条件检查在每日任务完成后自动触发
3. 在 `presentation/widgets/badge_display.dart` 中实现徽章展示卡片

**验证**：
- 写单元测试：
  - 连续 3 天有推进 → 获得「持续推进者·3天」徽章
  - 连续 5 天保底完成 → 获得「保底守护者·5天」徽章
  - 同一徽章跨等级不重复触发（已有低等级，不再次触发）
  - 断档后不撤销已有徽章
- `flutter test` 通过

---

### Step 6.4：实现低压提醒

**指令**：
1. 使用 `flutter_local_notifications` 实现本地推送
2. 按设计文档第 3.4.2 节的时刻表配置提醒：
   - 10:00 — 核心任务提醒
   - 14:00 — 状态提示
   - 18:00 — 保底提醒
   - 22:30 — 深夜鼓励
   - 3 天未登录 — 回归问候
3. 所有提醒使用设计文档规定的文案
4. 设置页面提供开关：完全关闭提醒

**验证**：
- 写测试（mock 通知插件）：
  - 设置提醒 → 验证 `flutter_local_notifications` 的 `show` 被调用
  - 关闭提醒 → 验证 `cancelAll` 被调用
  - 验证文案中不含「拖延」「落后」「警告」
- `flutter test` 通过

---

### Phase 6 完成检查

- [ ] 专注计时器可用，暂停/继续/换路
- [ ] 周报生成叙事准确
- [ ] 徽章条件判定正确，断档不撤销
- [ ] 低压提醒文案符合温度规范

---

## Phase 7 — 打磨与内测

### Step 7.1：实现首次使用引导

**指令**：
1. 检测首次启动（Hive 存 `is_onboarding_complete` 标记）
2. 首次启动显示引导页（3 屏）：
   - 第 1 屏：登山手账隐喻 + slogan
   - 第 2 屏：保底/标准/冲刺概念
   - 第 3 屏：「一句话开始」→ 直接进入创建第一个目标的流程
3. 引导页使用 PageView，底部有圆点指示器和 Skip 按钮
4. 引导完成后跳转到今日一页

**验证**：
- 写 Widget 测试：
  - 首次启动 → 验证显示引导页，不显示今日一页
  - 滑动到第 3 屏 → 验证「开始」按钮存在
  - 点击「开始」→ 验证引导标记写入 Hive
  - 第二次启动 → 直接显示今日一页
- `flutter test` 通过

---

### Step 7.2：全功能冒烟测试

**指令**：
1. 创建端到端测试路径：
   - 首次引导 → 创建目标 → 创建今日任务 → 启动陪伴 → 完成任务 → 复盘 → 查看热力图 → 查看周报
2. 验证设计原则检查清单（design-document.md 第 8 节）：
   - 全 App 搜索❌字符 → 确保不使用红叉
   - 全 App 搜索「拖延」「落后」「放弃」「失败」→ 确保不使用这些词汇
   - 验证所有页面无需登录即可使用

**验证**：
- `flutter analyze` 无错误
- `flutter test` 全部通过
- 运行文本扫描脚本：确认无禁用语出现在 UI 层

---

### Step 7.3：性能与边界检查

**指令**：
1. 处理边界情况：
   - 大文本输入（标题超过 100 字符）→ 截断
   - 空任务列表 → 显示空状态插画和引导文案
   - 删除有子任务的目标 → 确认弹窗
   - 跨天数据正确（跨月、跨年）
2. 确保所有异步操作有加载状态和错误处理
3. 确保离线环境下所有核心功能可用（断网测试）

**验证**：
- 空列表页面 → 验证显示「还没有任务，创建一个吧」
- 删除目标 → 验证弹窗确认
- 开启飞行模式 → 验证今日一页、任务 CRUD、回顾页正常工作
- `flutter test` 全部通过

---

### Step 7.4：最终质量门禁

**指令**：
1. `dart format --output=none --set-exit-if-changed .` — 代码格式无问题
2. `flutter analyze` — 零警告零错误
3. `flutter test --coverage` — 全部通过
4. 检查 `test/` 目录覆盖率报告，确保 domain/services 覆盖 > 90%

**验证**：
- 三条命令全部通过
- `flutter test --coverage` 后检查 `coverage/lcov.info` 中 domain/services 的覆盖率

---

### Phase 7 完成检查

- [ ] 首次引导流程完整
- [ ] 全 App 无禁用语（❌/拖延/落后/放弃/失败）
- [ ] 空状态、大文本、删除确认等边界处理
- [ ] 离线核心功能可用
- [ ] domain/services 覆盖率 > 90%
- [ ] flutter analyze 零错误

---

## 附录 A：测试运行命令速查

| 命令 | 说明 |
|------|------|
| `flutter analyze` | 静态分析 |
| `flutter test` | 运行所有测试 |
| `flutter test test/domain/services/intensity_engine_test.dart` | 运行特定测试文件 |
| `flutter test --coverage` | 带覆盖率运行 |
| `dart run build_runner build` | 生成 freezed/drift 代码 |
| `dart format .` | 格式化代码 |
| `flutter run -d chrome` | 浏览器运行 |

## 附录 B：每步产出清单模板

每完成一个 Step，确保以下 3 个文件存在或操作完成：

```
□ 源文件已创建（`.dart`）
□ 测试文件已创建（`_test.dart`）
□ `flutter test` 通过
□ `flutter analyze` 无新增错误
```

> **文档版本**：v1.0
> **最后更新**：2026-05-12
> **说明**：本计划按 7 个 Phase 分步实施，共约 45 个 Step。每步读作一条独立的 AI 开发者指令，不可跳过验证。
