# 一寸 — 架构文档

## 项目概览

一寸是 Flutter 移动端应用（目标平台：iOS / Android），使用 Riverpod 管理状态，drift 做本地持久化。

---

## 文件结构总览

```
math/
├── pubspec.yaml                  # 项目依赖清单（Flutter SDK + 14 运行时 + 7 开发依赖）
├── analysis_options.yaml         # Dart lint 规则配置
├── .gitignore                    # Git 忽略规则（Flutter + 生成代码 + IDE）
│
├── lib/
│   └── main.dart                 # 应用入口，启动 YicunApp
│
├── test/
│   └── widget_test.dart          # Widget 测试入口，验证欢迎语渲染
│
├── memory-bank/                  # 项目知识库（所有设计与规划文档）
│   ├── AGENTS.md                 # AI 开发者指南：必读文档索引与核心约束
│   ├── RULES.md                  # 项目规范全集（编码/测试/Git/安全/违规处理）
│   ├── design-document.md        # 产品设计文档（功能定义、数据模型、交互流程）
│   ├── tech-stack.md             # 技术选型文档（框架选型理由、依赖清单、目录结构）
│   ├── implementation-plan.md    # 实施计划（45 个 Step 的分步指令与验证标准）
│   ├── architecture.md           # ← 本文件：架构说明与文件职责
│   └── progress.md               # 开发进度记录（每个 Step 完成后更新）
│
└── .dart_tool/                   # Dart 工具缓存（自动生成，不提交）
```

---

## 各文件职责

### 项目根文件

| 文件 | 作用 | 维护者 |
|------|------|--------|
| `pubspec.yaml` | 定义项目名称、SDK 版本约束、所有依赖的版本号。这是 Flutter 项目的"心脏"，每次加依赖都需修改它 | 开发者 |
| `analysis_options.yaml` | 配置 Dart 静态分析规则。违反规则的代码会在 `flutter analyze` 时报错 | 开发者 |
| `.gitignore` | 排除不应提交到 Git 的文件：编译产物、IDE 配置、生成代码（`.freezed.dart` / `.g.dart`） | 一次性 |

### lib/ — 应用代码

| 文件 | 作用 | 将来会扩展为什么 |
|------|------|----------------|
| `main.dart` | 应用入口，调用 `runApp(YicunApp())` | 不变，保持简洁 |

**目录层次说明**（按 tech-stack.md 规划，后续 Phase 逐步创建）：

```
lib/
├── core/             跨层共享：主题、常量、工具函数、路由
│   ├── theme/        设计令牌（颜色、字号、圆角、阴影）
│   ├── constants/    文案常量、配置参数
│   ├── utils/        日期工具、文案映射、ID 生成
│   └── router/       go_router 路由表定义
│
├── data/             数据层：数据库 DAO、网络请求、仓库
│   ├── database/     drift 数据库定义、表、DAO
│   ├── local/        Hive 本地偏好
│   ├── remote/       AI API 客户端
│   └── repositories/ 仓库层（返回 Result<T>，本地优先）
│
├── domain/           纯 Dart 业务逻辑，零 Flutter 依赖
│   ├── models/       freezed 领域模型
│   └── services/     规则引擎、AI 拆解器、叙事生成、徽章判定
│
└── presentation/     UI + Riverpod Provider
    ├── providers/    跨页面共享状态
    ├── pages/        各页面（today / goal_detail / review / weekly / focus / settings）
    └── widgets/      可复用组件（task_card / intensity_slider / heatmap 等）
```

### test/ — 测试代码

| 文件 | 作用 | 测试类型 |
|------|------|---------|
| `widget_test.dart` | 验证 App 启动后渲染欢迎语 | Widget 测试 |

测试目录结构与 lib/ 镜像，按 `domain/` / `data/` / `presentation/` 分层组织。

### memory-bank/ — 知识库

| 文件 | 核心职责 | 谁应该读 |
|------|---------|---------|
| `AGENTS.md` | AI 的"使用说明书"：开始前读哪些文档、核心约束 | 每次开始编码前 |
| `RULES.md` | 项目"法律"：编码规范、测试规范、Git 规范、违规处理 | 每次编码/提交前 |
| `design-document.md` | 产品"圣经"：每一个功能为何存在、怎么交互 | 做新功能前 |
| `tech-stack.md` | 技术选型"地图"：为什么选 Flutter/Riverpod/drift，依赖清单 | 加依赖或评估方案时 |
| `implementation-plan.md` | 开发"路线图"：45 个 Step 的分步指南 | 每天开工前看当前 Phase |
| `architecture.md` | 本文件：全项目地图 | 理解全局时 |
| `progress.md` | "航海日志"：每个 Step 完成后记录做了什么、遇到什么问题 | 后续开发者回溯时 |

---

## 架构决策记录

### ADR-001：本地优先，无须登录

**决策**：应用核心功能无须用户注册即可使用。数据存本地 SQLite，云同步为未来可选功能。

**理由**：降低使用门槛，避免早期用户流失。

**影响**：
- 所有 Repository 优先读写本地数据库
- 用户 ID 使用本地生成的 UUID
- 未来增加云同步时，Repository 需增加 sync 逻辑，不影响现有调用方

### ADR-002：三层依赖方向

**决策**：`presentation → data → domain`，domain 层零 Flutter 依赖。

**理由**：domain 层的规则引擎、拆解器等核心逻辑必须可独立单元测试，不依赖 Flutter 运行时。

**影响**：
- domain 层的 import 中不得出现 `package:flutter/`
- domain 层不得使用 `DateTime.now()`，通过依赖注入提供时间

### ADR-003：所有 Repository 返回 Result<T>

**决策**：不使用异常进行流程控制。

**理由**：异常处理容易遗漏，通过 Result 类型强制调用方处理成功/失败两种路径。

**影响**：
- `sealed class Result<T>` + `Success` / `Failure` 子类
- Provider 中统一 `when(data: ..., loading: ..., error: ...)`

### ADR-004：UUID 做所有实体的主键

**决策**：Goal、Task、Session 等所有实体使用 UUID v4 字符串作 ID。

**理由**：本地优先 + 未来云同步需要全局唯一 ID，auto-increment 整数在合并时冲突。

**影响**：
- `IdGenerator.newUuid()` 使用 `Uuid().v4()` 生成
- 所有 drift 表的 id 字段为 `TextColumn`
- DAO 插入时需显式传入 ID

### ADR-005：JSON 分层约定（Template 场景）

**决策**：模型的 JSON 序列化/反序列化归属 Model 层，DAO 存原始 String，Repository 层负责解码。

**理由**：单一职责 — Model 知道如何序列化自己，DAO 只做存储，Repository 做业务逻辑。

**影响**：
- `Template` 模型必须实现 `toJson()` / `fromJson()`
- DAO 的 `task_templates_json` 字段为 `TextColumn`，不关心内容
- Repository 的 get 方法负责 `jsonDecode`，insert 方法负责 `jsonEncode`

---

## 技术依赖摘要

| 依赖 | 用途 | 替代候选（不选理由） |
|------|------|-------------------|
| Flutter + Dart 3 | 跨平台框架 | React Native（JS 桥接层增加排查成本） |
| flutter_riverpod | 状态管理 | Bloc（样板代码多）、Provider（已被取代） |
| drift | 本地数据库 | sqflite（无类型安全、无 migration） |
| go_router | 声明式路由 | getX（侵入性强） |
| freezed | 不可变模型 | 手写（容易出错） |
| dio | HTTP 客户端 | http（不够灵活） |
| uuid | ID 生成 | 手写（不标准） |
| hive | 本地偏好持久化 | shared_preferences（不支持复杂类型） |

---

> **文档版本**：v1.0
> **最后更新**：2026-05-12
> **维护**：本文件随产品演进持续更新，每次重大功能或里程碑后必须更新。
