# 一寸 — 架构文档

## 技术栈

| 层面 | 选型 |
|------|------|
| 跨平台框架 | Flutter + Dart 3 |
| 状态管理 | Riverpod 2.x |
| 本地数据库 | drift (SQLite) |
| 轻量存储 | Hive |
| 网络请求 | dio |
| 序列化 | freezed + json_serializable |
| 路由 | go_router |
| 云同步（未来） | Supabase |

## 三层架构

```
┌────────────────────────────────────────────┐
│ presentation/     UI + Riverpod Provider    │
│   pages/     → 页面                         │
│   widgets/   → 可复用组件                   │
│   providers/ → 状态管理                     │
├────────────────────────────────────────────┤
│ domain/           纯 Dart，零 Flutter 依赖  │
│   models/    → 领域模型（freezed）           │
│   services/  → 业务逻辑（规则引擎、AI 拆解） │
├────────────────────────────────────────────┤
│ data/             数据层                     │
│   database/  → drift 表定义 + DAO          │
│   local/     → Hive 本地偏好               │
│   remote/    → AI API 调用                 │
│   repositories/ → 仓库（本地优先）          │
└────────────────────────────────────────────┘
```

## 数据流向

```
用户操作 → Provider → Repository → DAO → SQLite
                              ↘
                             AI API (可选)
```

## 核心数据实体

- **Goal** — 目标（标题、科目、动机、状态）
- **Task** — 任务（三档完成标准、强度、进度、中断点）
- **Session** — 专注记录（起止时间、关联任务）
- **DayRecord** — 每日汇总（状态、完成度、复盘）
- **Template** — 科目模板（官方预置 / 社区贡献）

## AI 策略

- 规则模板匹配优先 → 未匹配走免费 LLM API → 失败走基础兜底
- 结果缓存到 Hive，相同输入不重复请求

## 设计原则

1. 完成定义优先 — 保底/标准/冲刺三档
2. 低压力设计 — 无惩罚、无失败羞耻
3. 弹性计划 — 延期、降级、拆分、接力
4. 推进感优先 — 关注进度而非清零
5. 适配状态波动 — 根据状态推荐强度

> 详细产品设计见 `@design-document.md`
> 技术选型详情见 `tech-stack.md`
