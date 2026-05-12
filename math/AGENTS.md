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

## 开发规范

- domain 层零 Flutter 依赖
- 使用 `Result<T>` 封装仓库返回值
- freezed 模型禁止手动修改生成文件
- 核心逻辑（规则引擎、拆解器）必须编写单元测试

## 重要提示

写任何代码前必须完整阅读 memory-bank/architecture.md
写任何代码前必须完整阅读 memory-bank/design-document.md
每完成一个重大功能或里程碑后，必须更新 memory-bank/architecture.md
