# 一寸 — 项目规范

> 无规矩不成方圆。本文件定义项目的一切约束，**所有开发者（含 AI）必须遵守**。
> 违反规则导致的 bug 等同于生产事故，必须回溯归因。

---

## 一、编码规范

### 1.1 Dart 语言规则

| # | 规则 | 违规示例 | 正确示例 |
|---|------|---------|---------|
| 1 | **禁止使用 `var` 推断函数返回值** | `var result = getData()` | `List<Goal> result = getData()` |
| 2 | **禁止使用 `dynamic` 类型** | `final dynamic x = ...` | 必须明确具体类型或使用泛型 |
| 3 | **禁止使用 `!` 强制解包** | `text!` | 使用 `??` 或 `?.` 或显式判空 |
| 4 | **禁止使用 `late` 关键字** | `late String name` | 构造函数初始化或 `?` 可空 |
| 5 | **禁止使用 `print()` 调试** | `print('debug')` | 使用 `log()` 或 `Logger` |
| 6 | **必用 `sealed class` 做状态联合** | `class Result {}` + 注释 | `sealed class Result<T> {}` |
| 7 | **必用 `const` 构造** | `SizedBox(width: 10)` | `const SizedBox(width: 10)` |
| 8 | **必用 `pattern matching` 代替 is/as** | `if (x is A) { (x as A).foo }` | `if (x case A())` |
| 9 | **必用 `copyWith` 更新 freezed 对象** | `Goal(title: newTitle)` | `goal.copyWith(title: newTitle)` |
| 10 | **禁止魔数/魔字符串** | `if (status == 'a')` | `if (status == GoalStatus.active)` |

### 1.2 命名规范

| 类别 | 规范 | 示例 |
|------|------|------|
| 文件/目录 | `snake_case` | `intensity_engine.dart` |
| 类/枚举/typedef | `PascalCase` | `IntensityEngine` |
| 变量/函数/参数 | `camelCase` | `getTodayTasks()` |
| 私有成员 | `_camelCase` | `_loadData()` |
| 常量/枚举值 | `camelCase` | `EnergyLevel.energetic` |
| 目录名 | 单数名词 | `goal_detail/`、`widgets/` |
| 测试文件 | `*_test.dart` | `intensity_engine_test.dart` |

### 1.3 文件组织规范

**每个 Dart 文件不得超过 400 行**。超过时必须拆分：
- 工具函数 → `utils/` 下的独立文件
- 巨型 Widget → 拆为多个 Widget 文件
- 巨型 Provider → 拆为多个 Provider 文件
- 巨型 Model → 拆为多个 Model 文件

**import 顺序**（必须遵守，用空行分隔）：

```dart
// 1. Flutter SDK
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

// 2. 第三方包
import 'package:dio/dio.dart';
import 'package:drift/drift.dart';

// 3. 项目内部：上层 → 下层（presentation → data → domain）
import 'package:yicun/domain/models/goal.dart';
import 'package:yicun/data/repositories/goal_repository.dart';
import 'package:yicun/presentation/providers/goal_providers.dart';

// 4. 相对路径导入（同一层）
import 'task_card.dart';
```

### 1.4 禁止的 API

以下 Dart/Flutter API **彻底禁用**，IDE 应配置为编译报错：

| 禁用 API | 替代方案 |
|---------|---------|
| `dynamic` | 具体类型或泛型 |
| `!` （bang operator） | `?.` + `??` + 模式匹配 |
| `late` | 构造函数初始化、`?` 可空、`late final`（仅限 const 构造场景） |
| `print()` | `log()` 或 `Logger` |
| `as` 类型转换 | `is` + 模式匹配 |
| `toStringAsFixed()` | `NumberFormat` |
| `DateTime.now()`（在业务逻辑中） | 通过 `Clock` 依赖注入 |
| `Random()`（在业务逻辑中） | 通过依赖注入 |

### 1.5 注释规范

- **禁止**写块注释 `/* */` 解释代码在做什么
- **允许**写行注释 `//` 解释「为什么」而不是「是什么」
- **必须**为公开 API 写 Dartdoc（`///`），说明职责、参数、返回值
- 代码应当自文档化——如果一段代码需要注释才能看懂，改为重构

---

## 二、架构规范

### 2.1 三层依赖规则（强制执行）

```
presentation/  →  domain/  +  data/
     │                      
     ▼                      
data/  →  domain/          
     │                      
     ▼                      
domain/  →  （纯 Dart，零 Flutter 依赖）
```

**禁止**：
- ❌ `domain/` 导入任何 `package:flutter/` 或 `package:drift/` 等框架包
- ❌ `domain/` 导入 `data/` 或 `presentation/`
- ❌ `data/` 导入 `presentation/`
- ❌ 跨层跳过（如 `presentation` 直接调 DAO 而不经过 Repository）

**每个文件的 import 检查方法**：检查文件顶部的 import 列表，domain 层出现 Flutter import 即为违规，必须立即修复。

### 2.2 数据流规则

```
UI Event → Provider（调用 Repository）
Repository（返回 Result<T>）→ Provider（更新状态）→ UI（重建）
```

**禁止**：
- ❌ Widget 直接调用 DAO 或 Repository
- ❌ Provider 直接操作数据库
- ❌ 在 Widget build 方法中发起异步操作
- ❌ 直接将 Repository 返回值传给 UI 不做错误处理

### 2.3 状态管理规范（Riverpod）

- 每个页面对应一个 Provider 文件（如 `today_providers.dart`）
- 跨页面共享的状态放在 `presentation/providers/` 根目录
- 单页面私有状态放在 `presentation/pages/<page>/providers/` 下
- 禁止使用 `ChangeNotifierProvider`——统一使用 `riverpod_generator` 的 `@riverpod` 注解
- 所有 Provider 必须使用 `@riverpod` 注解生成代码，不手动写 Provider
- Provider 命名规则：`data` 类用 `xxxProvider`，`notifier` 类用 `xxxController`

### 2.4 仓库层规范（Repository）

- **所有 Repository 方法返回 `Result<T>`**，不允许抛异常
- Repository 是本地数据库的唯一访问入口
- Repository 内部异常必须捕获并转为 `Failure`
- Repository 不得持有 UI 状态

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

### 2.5 数据库规范（drift）

- 所有表定义放在 `data/database/tables/`，一个表一个文件
- 所有 DAO 放在 `data/database/daos/`，一个 DAO 一个文件
- DAO 方法命名：`insert`/`get`/`getAll`/`update`/`delete` 前缀
- 禁止在 DAO 外部写 SQL 查询
- 禁止使用 `LIMIT 1`（用 `LIMIT 1` 时应当用 `get` 查询特定记录）
- 所有 migrate 必须写 `onUpgrade` 逐版本迁移，禁止清库

### 2.6 freezed 模型规则

- 所有领域模型使用 `@freezed`
- **禁止手动修改 `*.freezed.dart` 和 `*.g.dart` 生成文件**
- `copyWith` 是更新模型的唯一方式
- JSON 序列化使用 `@JsonSerializable()`，不用手写 `fromJson`/`toJson`
- 每次修改模型定义后必须运行 `dart run build_runner build`

---

## 三、AI 开发规范

### 3.1 AI 开发者通用指令

AI 开发者（包括当前会话）必须遵守以下规则：

| # | 规则 | 说明 |
|---|------|------|
| 1 | **读全再改** | 修改文件前必须完整阅读该文件，不得仅凭上下文猜测内容 |
| 2 | **一次变更最小化** | 每次 commit 只做一件事，严禁混入无关修改 |
| 3 | **写完即测** | 每写完一个功能必须运行对应的测试，不得跳过 |
| 4 | **生成文件不手动修改** | freezed/drift 生成的 `.g.dart` 文件禁止手动编辑 |
| 5 | **有错先查测试** | 运行 `flutter test` 定位 bug，而非肉眼检查代码 |
| 6 | **不引入未使用的依赖** | 新加 pub 依赖前必须先搜索确认项目是否已有同类依赖 |
| 7 | **不删除未理解的代码** | 如果要删除现有逻辑，必须先理解它被依赖的方式 |
| 8 | **按 Plan 执行** | 开发必须按 `memory-bank/implementation-plan.md` 的 Phase 顺序执行 |

### 3.2 代码生成命令速查

| 操作 | 命令 |
|------|------|
| 生成 freezed/drift 代码 | `dart run build_runner build` |
| 清理生成缓存 | `dart run build_runner clean` |
| 监听模式自动生成 | `dart run build_runner watch` |

**注意**：每次修改 model 或 table 后必须运行生成命令，否则编译报错。

---

## 四、测试规范

### 4.1 测试金字塔

```
      /\
     /  \         Widget / Integration 测试（10%）
    /    \
   /______\       
  /        \      Provider 测试（20%）
 /          \
/____________\
/              \  Repository 测试（20%）
/________________\
/                  \  Unit 测试 — 纯 Domain 逻辑（50%）
/____________________\
```

### 4.2 测试覆盖要求

| 层级 | 最低覆盖率 | 必须测什么 |
|------|-----------|-----------|
| `domain/services/` | **90%** | 所有分支、所有边界、所有异常路径 |
| `domain/models/` | **100%** | 构造、copyWith、序列化、相等性 |
| `data/repositories/` | **80%** | 成功路径、失败路径、边界条件 |
| `data/database/daos/` | **70%** | CRUD、过滤条件、级联行为 |
| `presentation/providers/` | **70%** | 核心 Provider 的数据聚合逻辑 |
| `presentation/pages/` (Widget) | **关键页面** | 今日一页、目标卡片、启动陪伴 |
| `presentation/widgets/` | **关键组件** | 难度滑杆、热力图、状态选择器 |

### 4.3 单元测试规范

**测试文件命名**：`{被测文件}.test.dart`（注意末尾是 `.test.dart` 而非 `_test.dart`）

**测试分组命名**（中文，便于阅读）：

```dart
group('IntensityEngine', () {
  group('recommend()', () {
    test('连续3天高强度 → 返回 standard 推荐', () {
      // ...
    });

    test('昨日保底完成 → 返回 minimal 推荐', () {
      // ...
    });
  });

  group('高风险科目检测', () {
    test('某科目拖延率 > 60% → 返回该科目推荐', () {
      // ...
    });
  });
});
```

**AAA 模式**（必须遵守）：

```dart
test('描述', () {
  // Arrange — 准备测试数据
  final engine = IntensityEngine();
  final state = StateAssessment(...);

  // Act — 执行被测方法
  final result = engine.recommend(state);

  // Assert — 验证结果
  expect(result.intensity, 'standard');
  expect(result.message, contains('冲刺'));
});
```

**禁止**：
- ❌ 在测试中访问网络或文件系统
- ❌ 使用 `sleep()` 等待异步
- ❌ 多个 assert 散布在测试中（应分多个 test）
- ❌ 依赖测试执行顺序

### 4.4 Mock 规范

| 场景 | Mock 工具 | 说明 |
|------|----------|------|
| Repository 测试 | Drift 内存数据库 | 真正的 SQLite 运行在内存中，不 mock |
| Provider 测试 | `mockito` 生成 mock 类 | Mock Repository 层 |
| Widget 测试 | `mockito` + Provider override | Mock 数据源 |
| AI Client 测试 | `mockito` mock Dio | 不发起真实网络请求 |
| Notification 测试 | `mockito` mock 插件 | 不发送真实通知 |

**禁止**：
- ❌ 手写 Mock 类（必须用 `mockito` 生成）
- ❌ Mock 值类型或纯函数（直接传真实数据）
- ❌ 在 DAO 测试中使用 Mock（必须用内存数据库）

### 4.5 Widget 测试规范

**定位控件的方法**（优先级从高到低）：

1. `find.byKey(Key('...'))` — 优先使用
2. `find.text('...')` — 文本定位
3. `find.byType(MyWidget)` — 类型定位（仅用于自定义 Widget）

**所有可交互控件必须设置 `Key`**，包括但不限于：
- 按钮
- 列表项
- 输入框
- 表单字段
- 底部 Sheet

**测试内容**：
- 验证关键 UI 元素存在
- 验证交互后状态变更
- 验证空状态/加载状态/错误状态
- 验证路由跳转

### 4.6 测试运行规则

| 场景 | 命令 | 要求 |
|------|------|------|
| 每次代码修改后 | `flutter analyze` + `flutter test` | 必须通过 |
| 每个 Step 完成后 | `flutter test` | 全部通过 |
| 每个 Phase 完成后 | `flutter test --coverage` | 查看覆盖率报告 |
| 提交前 | `flutter analyze` + `flutter test` | 零错误零警告 |

---

## 五、Git 规范

### 5.1 提交信息格式

```
<type>: <简短描述>

<可选：详细描述>
```

**type** 取值：

| type | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `refactor` | 重构 |
| `test` | 测试相关 |
| `docs` | 文档 |
| `style` | 代码格式（非语义变更） |
| `chore` | 构建/工具/依赖 |
| `perf` | 性能优化 |
| `init` | 项目初始化 |

**示例**：
```
feat: 实现难度滑杆三档切换

- 支持保底/标准/冲刺三档
- 滑到保底时完成标准切换为保底描述
- 不记录切换历史，不提示"降级"
```

### 5.2 提交前检查清单

每次 `git commit` 前必须检查：

- [ ] `flutter analyze` 零错误
- [ ] `flutter test` 全部通过
- [ ] 没有 `print()` 语句
- [ ] 没有未使用的 import
- [ ] 没有硬编码的 API key 或密钥
- [ ] 新文件都有测试文件
- [ ] `dart run build_runner build` 已执行（如果修改了 model/table）

### 5.3 分支策略

| 分支 | 用途 | 来源 | 合并到 |
|------|------|------|--------|
| `main` | 稳定发布 | — | — |
| `dev` | 开发集成 | `main` | `main` |
| `feat/<name>` | 单个功能 | `dev` | `dev` |
| `fix/<name>` | Bug 修复 | `dev` | `dev` |

一人开发时：直接在 `dev` 分支开发，每个 commit 对应一个 Step。

---

## 六、错误处理规范

### 6.1 错误分层

| 层 | 错误处理方式 | 示例 |
|----|-------------|------|
| DAO | 不处理，抛给 Repository | 数据库异常自然传播 |
| Repository | 捕获异常 → 包装为 `Failure` | `try { ... } on Exception catch (e) { return Failure(e.message); }` |
| Provider | 处理 `Result` → 暴露 loading/error/data 三态 | `when(data: ..., loading: ..., error: ...)` |
| Widget | 展示错误状态 | 错误提示条、重试按钮 |

### 6.2 错误展示规则

- 网络错误：显示「网络似乎不太稳定」+ 重试按钮
- 数据库错误：静默恢复 + log 记录，不展示给用户
- AI 超时：静默降级到规则模板，不给用户报错
- 数据为空：显示空状态插画 + 温和引导文案

### 6.3 禁止的异常处理模式

- ❌ `catch (e) { /* 空 */ }` — 静默吞掉异常
- ❌ `catch (e) { print(e); }` — 只打印不处理
- ❌ 用异常做流程控制（如 `throw` 表示「没找到」→ 应返回 `null`）
- ❌ 在 Repository 层未捕获异常就向上抛

---

## 七、安全保障

### 7.1 密钥管理

- **禁止**将 API key、Token、密钥硬编码在源代码中
- API key 通过环境变量注入：`--dart-define=API_KEY=xxx`
- 敏感配置放在 `lib/core/constants/app_config.dart` 中，运行时从环境变量读取
- `.env` 文件必须写入 `.gitignore`

### 7.2 数据安全

- 用户数据仅存储在本地 SQLite
- 如需云同步，必须用户主动开启并提供知情同意
- 禁止收集用户隐私数据（位置、通讯录、相册）
- 所有分析埋点必须先匿名化

---

## 八、技能与约束

### 8.1 必须遵循的约束

以下约束**任何时刻不得违反**：

| # | 约束 | 后果 |
|---|------|------|
| 1 | domain 层不得导入 Flutter | 编译失败，需重写 |
| 2 | 所有 Repository 返回 `Result<T>` | Provider 层未处理 Result 导致运行时异常 |
| 3 | 每次改 model 后运行 build_runner | `.g.dart` 与源文件不一致，运行时出错 |
| 4 | 禁止 `!` 强制解包 | 线上 null 崩溃 |
| 5 | 每步必须写测试再提交 | 无测试的代码视为未完成 |
| 6 | 任何文件不超过 400 行 | 维护成本指数增长 |

### 8.2 常见陷阱自查表

编码前对照检查：

- [ ] 这个功能是在 domain 层还是 presentation 层实现？
- [ ] 如果放在 domain 层，有没有引入 Flutter 依赖？
- [ ] 数据流是否经过 Repository → Provider → UI？
- [ ] 是否处理了空状态、加载状态、错误状态？
- [ ] 异步操作是否有超时控制？
- [ ] 文案是否符合「文案温度规范」？（design-document.md 第 5 节）
- [ ] 新增的字符串是否出现在 `app_strings.dart` 中？
- [ ] 是否已经为新增功能写了测试？

### 8.3 必须阅读的文档

在开始任何编码前：

1. `memory-bank/design-document.md` — 产品设计全局
2. `memory-bank/architecture.md` — 技术架构
3. `memory-bank/implementation-plan.md` — 当前阶段要做什么
4. `RULES.md`（本文件）— 编码规则

---

## 九、违规处理

| 违规级别 | 示例 | 处理方式 |
|---------|------|---------|
| 🔴 严重 | domain 层导入 Flutter、硬编码密钥、`!` 解包 | 拒绝提交，回溯重构 |
| 🟡 中等 | 无测试提交、文件超 400 行、魔字符串 | 补充测试，拆分文件 |
| 🟢 轻微 | import 顺序不对、命名不规范 | 提醒修正，下次提交前修复 |

**违规记录**：每次违反规则应在 `progress.md` 中记录，注明：
- 日期
- 违规内容
- 修复方式
- 如何防止再犯

---

> **文档版本**：v1.0
> **最后更新**：2026-05-12
> **适用范围**：所有开发一寸项目的 AI 与人类开发者
