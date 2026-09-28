# Changelog

## 2.1.0 — 2026-09-28

### Added

- 17 个项目执行模板：Project State、Story Bible、Source Index、Source Analysis、Adaptation Bible、Character Bible、Relationship Map、Timeline、Secret Ledger、Knowledge State、Setup/Payoff、Episode Map、Scene List、Script Draft、Revision Report 等
- 长篇 / 百万字小说专用改编工作流
- Source Index 三层读取策略
- Chapter Function Map
- 章节 / 卷 → Sequence → Episode / Act 映射规则
- 改编适配度与压缩压力评分
- Adaptation Risk Report
- 人物关系网络事件抽取
- Story Bible 自动收敛工作流
- 项目自动初始化工作流
- 百万字网文项目工作空间示例

### Changed

- 长篇改编现在必须先完成全局索引与关键段二次深读，再锁 Story DNA
- 不再允许按小说章节编号机械映射剧集
- 项目状态从“聊天记忆”升级为显式模板与正典文件
- 主 Skill 新增长篇改编自动路由

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
