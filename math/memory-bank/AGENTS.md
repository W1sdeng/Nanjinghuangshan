# 一寸 — 开发指南

## 项目概述

考研/长期学习状态感知型管理工具。「登山手账」隐喻，帮助用户拆解目标、弹性执行、温柔复盘。

## 技术栈

- Flutter + Dart 3
- Riverpod 2.x（状态管理）
- drift（本地 SQLite）
- dio（网络请求）
- freezed + json_serializable（序列化）
- go_router（路由）

## 项目结构

```
lib/
├── core/        主题、常量、工具、路由
├── data/        数据库、网络、仓库
├── domain/      模型、业务逻辑（纯 Dart）
└── presentation/ UI、Provider
```

## 必读文档（开始前必须阅读）

1. `RULES.md` — 全局编码规范、测试规范、Git 规范、错误处理（违规后果自负）
2. `design-document.md` — 产品设计全局
3. `architecture.md` — 技术架构
4. `implementation-plan.md` — 当前阶段的实施步骤

## 核心约束（违反 = 拒绝提交）

- domain 层零 Flutter 依赖
- 所有 Repository 返回 `Result<T>`，禁止抛异常
- freezed 模型禁止手动修改生成文件
- 核心逻辑（规则引擎、拆解器）必须编写单元测试，覆盖率 > 90%
- 每步开发后必须运行 `flutter test`，全部通过才能提交
- 禁止 `var` 推断返回值、禁止 `dynamic`、禁止 `!` 强制解包、禁止 `late`、禁止 `print()`

## 重要提示

写任何代码前必须完整阅读 architecture.md
写任何代码前必须完整阅读 design-document.md
每完成一个重大功能或里程碑后，必须更新 architecture.md
