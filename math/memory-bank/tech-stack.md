# 一寸 — 技术栈推荐

> 原则：简单但健壮，一人能驾驭，不走太重。

---

## 一、整体选型

```
┌─────────────────────────────────────────────┐
│               Flutter Framework               │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐ │
│  │  Riverpod │ │   drift   │ │    dio       │ │
│  │ 状态管理  │ │ 本地数据库 │ │ 网络请求     │ │
│  └──────────┘ └──────────┘ └──────────────┘ │
│         │           │              │          │
│         ▼           ▼              ▼          │
│  ┌─────────────────────────────────────────┐ │
│  │        三层架构（data/domain/presentation）│ │
│  └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

| 层面 | 选型 | 理由 |
|------|------|------|
| 跨平台框架 | **Flutter** | 一套代码覆盖 iOS/Android，UI 表现力强，一人能维护 |
| 语言 | **Dart 3** | 空安全、模式匹配、sealed class，适合领域建模 |
| 状态管理 | **Riverpod 2.x** | 编译时安全、天然支持异步、比 Bloc 轻量 |
| 本地数据库 | **drift** | 类型安全 SQLite，支持 migration、关系查询 |
| 轻量存储 | **Hive** / `shared_preferences` | 存用户设置、缓存 |
| HTTP 客户端 | **dio** | 拦截器、重试、超时，对接 AI API |
| JSON 序列化 | **freezed + json_serializable** | 不可变数据类，与 Riverpod 搭配好 |
| 路由 | **go_router** | 声明式路由，支持深层链接 |
| 云同步（未来） | **Supabase** | PostgreSQL 基础，实时能力，免费额度友好 |

---

## 二、核心依赖清单

```yaml
# pubspec.yaml 核心依赖
dependencies:
  flutter:
    sdk: flutter

  # 状态管理
  flutter_riverpod: ^2.5.0
  riverpod_annotation: ^2.3.0

  # 数据库
  drift: ^2.16.0
  sqlite3_flutter_libs: ^0.5.0
  path_provider: ^2.1.0
  path: ^1.8.0

  # 网络
  dio: ^5.4.0

  # 序列化
  freezed_annotation: ^2.4.0
  json_annotation: ^4.8.0

  # 路由
  go_router: ^14.0.0

  # ID 生成
  uuid: ^4.3.0

  # 本地偏好
  hive_flutter: ^1.1.0

  # UI
  flutter_local_notifications: ^17.0.0  # 低压提醒
  fl_chart: ^0.68.0                      # 情绪曲线 / 热力图
  intl: ^0.19.0                          # 日期格式化

dev_dependencies:
  flutter_test:
    sdk: flutter
  drift_dev: ^2.16.0
  build_runner: ^2.4.0
  freezed: ^2.5.0
  json_serializable: ^6.7.0
  riverpod_generator: ^2.4.0
  mockito: ^5.4.0
```

---

## 三、项目结构

```
lib/
├── main.dart                       # 入口
├── app.dart                        # MaterialApp 配置、主题、路由
│
├── core/
│   ├── theme/                      # 设计令牌 → 颜色、圆角、阴影、字号
│   │   ├── app_colors.dart
│   │   ├── app_typography.dart
│   │   └── app_theme.dart
│   ├── constants/                  # 文案常量、配置参数
│   │   ├── app_strings.dart        # 文案温度规范
│   │   └── app_config.dart         # API key、缓存策略
│   ├── utils/                      # 工具函数
│   │   ├── date_utils.dart
│   │   └── text_utils.dart         # 文案映射（带到明天→延期）
│   └── router/
│       └── app_router.dart         # go_router 路由表
│
├── data/
│   ├── database/                   # drift 数据库层
│   │   ├── app_database.dart       # 数据库定义、migration
│   │   ├── tables/                 # 表定义
│   │   │   ├── goals_table.dart
│   │   │   ├── tasks_table.dart
│   │   │   ├── sessions_table.dart
│   │   │   ├── day_records_table.dart
│   │   │   └── templates_table.dart
│   │   └── daos/                   # 数据访问对象
│   │       ├── goal_dao.dart
│   │       ├── task_dao.dart
│   │       └── day_record_dao.dart
│   ├── local/                      # Hive 本地偏好
│   │   └── preferences_service.dart
│   ├── remote/                     # 网络请求
│   │   ├── ai_client.dart          # LLM API 调用
│   │   └── sync_client.dart        # 云同步（预留）
│   └── repositories/              # 仓库层 → 本地优先，云端备份
│       ├── goal_repository.dart
│       ├── task_repository.dart
│       └── state_repository.dart   # 状态感知数据
│
├── domain/
│   ├── models/                    # 领域模型（freezed）
│   │   ├── goal.dart
│   │   ├── task.dart
│   │   ├── session.dart
│   │   ├── day_record.dart
│   │   ├── template.dart
│   │   └── badge.dart
│   └── services/                  # 纯业务逻辑
│       ├── intensity_engine.dart   # 状态推荐规则引擎
│       ├── decomposition_service.dart  # AI 拆解器
│       ├── narrative_service.dart  # 周报叙事生成
│       └── badge_service.dart      # 徽章判定
│
├── presentation/
│   ├── providers/                  # Riverpod provider 定义
│   │   ├── goal_providers.dart
│   │   ├── task_providers.dart
│   │   ├── today_providers.dart    # 今日一页聚合
│   │   └── state_providers.dart    # 状态感知
│   ├── pages/                      # 页面
│   │   ├── today/                  # 今日一页
│   │   ├── goal_detail/            # 目标卡片详情
│   │   ├── review/                 # 来时路
│   │   ├── weekly_report/          # 本周山径
│   │   ├── focus/                  # 专注计时器
│   │   └── settings/               # 设置
│   └── widgets/                    # 可复用组件
│       ├── task_card.dart
│       ├── intensity_slider.dart   # 难度滑杆
│       ├── mood_selector.dart
│       ├── heatmap_grid.dart
│       └── badge_display.dart
│
└── test/                           # 单元 & Widget 测试
    ├── domain/
    │   ├── intensity_engine_test.dart
    │   └── decomposition_service_test.dart
    ├── data/
    │   └── repositories/
    └── presentation/
        └── providers/
```

### 目录规则

| 层 | 职责 | 依赖方向 |
|----|------|---------|
| `domain/` | 纯 Dart，零依赖 Flutter | 什么也不依赖 |
| `data/` | 数据库、网络、仓库 | 依赖 domain |
| `presentation/` | UI + Provider | 依赖 domain + data |
| `core/` | 主题、工具、配置 | 纯工具，无业务 |

---

## 四、核心模块技术实现要点

### 4.1 本地数据库（drift）

库表设计直接对应设计文档第 4 节的数据模型：

```dart
// goals_table.dart
class Goals extends Table {
  TextColumn get id => text()();
  TextColumn get title => text()();
  TextColumn get subject => text()();
  TextColumn get motivation => text()();
  TextColumn get deadline => text().nullable()();
  TextColumn get status => text()();  // active|paused|completed|archived
  DateTimeColumn get createdAt => dateTime()();

  @override
  Set<Column> get primaryKey => {id};
}

// tasks_table.dart
class Tasks extends Table {
  TextColumn get id => text()();
  TextColumn get goalId => text().references(Goals, #id)();
  TextColumn get title => text()();
  TextColumn get criteriaMinimal => text()();
  TextColumn get criteriaStandard => text()();
  TextColumn get criteriaSprint => text()();
  TextColumn get currentIntensity => text()();  // minimal|standard|冲刺
  RealColumn get progress => real()();           // 0-100
  TextColumn get status => text()();             // pending|in_progress|completed|carried_over
  TextColumn get completionQuality => text().nullable()();
  TextColumn get scheduledDate => text()();      // ISO date
  DateTimeColumn get createdAt => dateTime()();

  @override
  Set<Column> get primaryKey => {id};
}
```

**Migration 策略**：
- MVP 阶段不设计复杂 migration
- 版本号递增 + `onUpgrade` 回调逐版本迁移
- schema 稳定前允许清库重置（开发期）

### 4.2 状态感知推荐引擎（纯 Dart）

```dart
// domain/services/intensity_engine.dart
class IntensityEngine {
  const IntensityEngine();

  IntensityRecommendation recommend({
    required int consecutiveHighIntensityDays,
    required CompletionLevel yesterdayCompletion,
    required EnergyLevel energy,
    required MoodLevel mood,
    Map<String, double>? subjectProcrastinationRates,
  }) {
    if (consecutiveHighIntensityDays >= 3) {
      return IntensityRecommendation.standard(
        message: '你最近3天都是冲刺，今天试试标准模式？',
      );
    }
    if (yesterdayCompletion == CompletionLevel.minimal) {
      return IntensityRecommendation.minimal(
        message: '昨天只完成了保底，今天建议先守住一个核心。',
      );
    }
    if (energy == EnergyLevel.tired && mood == MoodLevel.anxious) {
      return IntensityRecommendation.rest(
        message: '看起来很疲惫，今天要不要休息一天？',
      );
    }
    // ... 更多规则
    return IntensityRecommendation.standard();
  }
}
```

- **纯函数 + 无状态**，方便单元测试
- 数据源来自 `DayRecord`（昨日完成度、状态数据）
- 不引入规则引擎库，if-else 足够

### 4.3 AI 拆解器

```dart
// data/remote/ai_client.dart
class AiClient {
  final Dio _dio;

  Future<String?> decomposeGoal(String userInput) async {
    try {
      final response = await _dio.post(
        'https://api.deepseek.com/v1/chat/completions',  // 示例：DeepSeek
        data: {
          'model': 'deepseek-chat',
          'messages': [
            {'role': 'system', 'content': _systemPrompt},
            {'role': 'user', 'content': userInput},
          ],
          'temperature': 0.3,
        },
        options: Options(timeout: const Duration(seconds: 15)),
      );
      return response.data['choices'][0]['message']['content'];
    } on DioException catch (_) {
      return null;  // 降级 → 走规则模板
    }
  }
}
```

- **先匹配模板 → 匹配不到走 AI → AI 失败走基础模板**，三层降级
- AI 结果缓存到本地 Hive，相同输入不再重复请求
- 使用 `freezed` 做请求/响应的不可变模型
- API key 通过环境变量注入，不硬编码

### 4.4 今日一页聚合 Provider

```dart
// presentation/providers/today_providers.dart
@riverpod
class TodayPageData extends _$TodayPageData {
  @override
  Future<TodayPageState> build() async {
    final goalRepo = ref.watch(goalRepositoryProvider);
    final taskRepo = ref.watch(taskRepositoryProvider);

    final todayTasks = await taskRepo.getTasksScheduledFor(today);
    final minimalDefense = _selectMinimalDefense(todayTasks);
    val carryOver = await taskRepo.getCarryOverTasks();
    val yesterdayCompletion = await goalRepo.getYesterdayCompletion();

    return TodayPageState(
      tasks: todayTasks,
      minimalDefense: minimalDefense,
      carryOverTasks: carryOver,
      yesterdayCompletion: yesterdayCompletion,
    );
  }
}
```

### 4.5 启动陪伴模式

- 硬编码的最小行动模板（不打 DB，不存云端）
- 模板按 `subject + task_type` 索引，纯本地常量
- 用户关闭陪伴模式后通过 `Hive` 存偏好，不走数据库

---

## 五、一人开发的工程策略

### 5.1 开发顺序

| 阶段 | 内容 | 预估 |
|------|------|------|
| Phase 0 | 脚手架搭建：项目结构、数据库表定义、主题系统 | 3-5 天 |
| Phase 1 | 目标卡片 CRUD + 今日一页 + 任务新建/编辑/完成 | 2 周 |
| Phase 2 | 启动陪伴模式 + 延期/接力/降级 | 1 周 |
| Phase 3 | 状态感知 + 规则引擎 + 难度滑杆 | 1.5 周 |
| Phase 4 | 来时路回顾 + 复盘改计划 | 1.5 周 |
| Phase 5 | AI 拆解器集成 + 科目模板库 | 2 周 |
| Phase 6 | 周报 + 徽章 + 提醒 + 专注计时器 | 2 周 |
| Phase 7 | 内测打磨 + Bug 修复 | 2 周 |

> 总计：约 12 周（3 个月）可交付内测版

### 5.2 不做的事（MVP 阶段）

- ❌ 云同步（Phase 6 以后）
- ❌ 社区模板审核后台
- ❌ 桌面组件
- ❌ 多语言
- ❌ 第三方登录
- ❌ 单元测试全覆盖（核心逻辑必须测：规则引擎、拆解器）

### 5.3 测试策略

| 层级 | 工具 | 覆盖率目标 |
|------|------|-----------|
| domain/services 纯逻辑 | `flutter_test` + `mockito` | 必须覆盖 90%+ |
| data/repositories | `flutter_test` + drift 内存数据库 | 核心路径 |
| presentation/providers | `riverpod` 测试工具 | 关键 Provider |
| Widget | `flutter_test` | 核心页面（今日一页、目标卡片） |

### 5.4 代码规范

- 使用 `dart format` + `analyzer` 保证风格一致
- freezed 模型禁止手动修改生成文件
- 所有领域层代码**零 Flutter 依赖**，方便测试
- Repository 返回值一律使用 `Result<T>` 封装（成功/失败），不直接抛异常

```dart
sealed class Result<T> {
  const Result();
}

final class Success<T> extends Result<T> {
  final T data;
  const Success(this.data);
}

final class Failure<T> extends Result<T> {
  final String message;
  final Object? error;
  const Failure(this.message, {this.error});
}
```

---

## 六、选型理由总结

| 候选 | 为什么不选 | 一寸的选择 |
|------|-----------|-----------|
| React Native | JS 桥接层增加排查成本，TypeScript 泛型不如 Dart 模式匹配灵活 | **Flutter** |
| Swift + Kotlin | 一人维护两套原生代码，开发速度翻倍 | **Flutter** |
| Bloc | 样板代码多，对 solo dev 太重 | **Riverpod** |
| sqflite | 裸 SQLite，无类型安全、无 migration 工具 | **drift** |
| Firebase Firestore | 强制云端、离线支持弱，不适合本地优先 | **Supabase**（未来） |
| getX | 侵入性强、隐式依赖，不利于长期维护 | **go_router** |
| Provider | 已被 Riverpod 取代 | **Riverpod** |

---

> **文档版本**：v1.0
> **最后更新**：2026-05-12
> **说明**：本技术栈推荐基于一人独立开发、移动端优先、本地优先的约束。若团队规模或产品方向变化，需重新评估。
