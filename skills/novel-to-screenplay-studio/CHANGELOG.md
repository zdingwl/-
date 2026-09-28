# Changelog

## 2.0.0 — 2026-09-28

### Added

- 双入口：小说 / IP 改编与原创剧本
- 电影、剧集、短剧、动画媒介路由
- 120 知识点 Level 2 知识地图
- Adaptation Matrix：KEEP / TRANSFORM / MERGE / MOVE / CUT / INVENT
- Source Index 与长小说分块读取规则
- Story DNA
- POV Map
- 内心戏外化系统
- 人物合并与支线压缩规则
- Reveal / Secret / Knowledge State
- Story Bible 与 Handoff State
- Scene Contract
- Dialogue as Action / Subtext / Voice Fingerprint
- Script Doctor / P0-P1-P2 修订优先级
- 小说改编工作流
- 原创剧本工作流
- 输出模板
- 回归测试 Rubric 与案例库
- 中文使用手册与示例项目

### Changed

- 从单文件 foundation 升级为多层 Skill 架构：
  `SKILL.md → workflows → references → evaluations`
- 默认连续推进，非关键缺失信息使用 ASSUMED，不逐阶段反复确认
- 长项目不再依赖短期上下文记忆，而是显式维护正典状态

### Compatibility

- 保留 `overseas-short-drama-screenwriter` 作为海外短剧专项 Skill
- 两套 Skill 可串联使用
