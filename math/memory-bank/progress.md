# 开发进度记录

## Phase 0 — 脚手架与基础设施

### Step 0.1：创建 Flutter 项目 ✅

**日期**：2026-05-12

**操作内容**：
1. 将 `AGENTS.md`、`RULES.md` 从 `math/` 根目录迁移到 `math/memory-bank/`
2. 因 `math/` 非空目录，`flutter create` 无法执行，手动创建所有项目文件
3. 手动创建 `pubspec.yaml`，按 tech-stack.md 写入 14 个运行时依赖 + 7 个开发依赖
4. 创建 `lib/main.dart`：干净的 `YicunApp`，无计数示例代码
5. 创建 `test/widget_test.dart`：一条 Widget 测试，验证欢迎语渲染
6. 创建 `analysis_options.yaml`、`.gitignore`

**创建的文件**：
- `pubspec.yaml` — 项目依赖配置（14 运行时 + 7 开发依赖）
- `lib/main.dart` — 入口文件，渲染 "进一寸，有一寸的欢喜。"
- `test/widget_test.dart` — 验证入口渲染
- `analysis_options.yaml` — lint 规则
- `.gitignore` — Flutter + 生成代码忽略规则

**验证结果**：
- `flutter pub get` — 126 个依赖安装成功
- `flutter test` — 1/1 通过
- `flutter analyze` — 未执行（需先 build_runner）

**注意事项**：
- 国内网络需设置镜像：`PUB_HOSTED_URL=https://pub.flutter-io.cn` `FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn`
- Flutter SDK 装在 `C:\tools\flutter`，版本 3.41.9 / Dart 3.11.5

**执行中遇到的问题**：
1. 根目录曾残留 AGENTS.md、design-document.md 等陈旧副本，需手动清理并提交删除
2. memory-bank/ 下残留旧的 @architecture.md，已删除
3. flutter pub get 首次下载 126 个包较慢（约 6 分钟），关闭 VPN 使用国内镜像后加速
4. Flutter SDK 下载了错误版本（3.29.2 的 URL 返回 634KB 无效文件），改用 3.27.4 后正常
