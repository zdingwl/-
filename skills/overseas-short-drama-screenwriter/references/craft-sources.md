# 编剧 Skill 融合来源与取舍

本文件用于维护当前 Skill 的方法来源和设计取舍。

目的不是复制外部 Skill，而是记录：哪些公开项目提供了值得吸收的方法、我们吸收了哪类原则、哪些内容因为不适合“海外短剧 → 中文完整剧本”工作流而没有采用。

> 运行时不必每次读取本文件。它主要用于后续升级、审查和避免重复造轮子。

---

# 1. FerroxLabs / wayland — write-screenplay

参考价值：**完整剧本流水线骨架**。

吸收：

- 从结构到人物、场景、初稿、结构修订的顺序
- 完整初稿之后必须做结构编辑，而不是把第一稿当终稿
- 场景必须推进剧情、揭示人物或提升冲突
- 发现结构问题时回到结构层修，而不是在台词层打补丁

没有直接采用：

- 电影 90–120 页等固定长片交付指标
- Pitch / query letter 等发行销售流程

原因：当前 Skill 的核心是海外短剧和连续剧本，不是好莱坞长片投递。

---

# 2. POUND0423 / AI-drama-pound — ai-short-drama-screenwriter

参考价值：**竖屏短剧完整编剧流程与边界控制**。

吸收：

- 创作简报 → 全剧 → 单集 → 分场 → 台词 → 修改
- 只要求剧本时，不越界进入分镜 / 视频提示词
- Hook、冲突、反转、集尾问题必须服务剧情推进
- 剧本审阅要指出问题、影响和修改方向
- 当前平台趋势必须查证，不能用旧知识冒充现况

没有直接采用：

- 繁体中文默认输出
- 固定面向中文本土短剧的社会逻辑

原因：本项目默认简体中文主稿，但故事逻辑必须面向指定海外国家。

---

# 3. jtydhr88 / screenwriting-skills

参考价值：**专业编剧知识深度最高的公开 Skill 体系之一**。

重点吸收：

## premise / theme

- 主题不是口号，而是由故事事件证明或挑战的命题
- 需要存在对立价值，避免故事只有单向说教

## story structure

- 不把任何一种结构方法当唯一真理
- 用结构诊断转折、升级、危机和高潮，而不是为了填模板造事件

## scene craft

- 场景必须有价值变化
- 场景内部由行动 / 反应 / 改变策略组成
- 重要 Scene Turn 会改变人物下一步行为

## dialogue

- 对白首先是行动
- 区分“说出来的 / 没说的 / 人物自己也不愿面对的”
- 说明性信息尽量变成人物争夺的筹码
- 不同人物必须拥有不同语言系统

## series structure

- 单集需要独立的结构和 Act-out / Cliffhanger 逻辑
- A/B/C 故事线的存在必须有功能
- 流媒体即使没有明显幕标，也仍存在信息、权力或目标转向形成的隐形结构

## writers' room

- 先找根问题，再修表面症状
- Revision 应区分结构、人物、场景和对白层级

没有直接采用：

- 与特定电视剧时长 / 广告位绑定的页码表
- 情景喜剧、舞台剧、戏曲等当前项目暂不需要的专项规则

---

# 4. gaojesse999 / ai-scripts — screenwriter

参考价值：**McKee / Campbell / Aristotle 的精炼戏剧工具 + 双语剧本意识**。

吸收：

- Want / Need / Hamartia / Arc
- Causality Audit
- Scene Value Movement
- Story Bible
- 双语对白对照时保持目标语言自然，不做中文逐字直译
- 剧本与视觉生产工具分离

没有采用：

- “用户必须自己提供故事”这一前提

原因：本 Skill 需要自己根据最新海外市场生成原创故事。

---

# 5. ChrisChen667788 / wind-comic — screenwriter

参考价值：**AI 长篇一致性与 Story Bible**。

吸收：

- 长项目维护 Story Bible
- 角色 Voice Fingerprint
- Continuity / 状态追踪
- Critic → Rewrite 思路
- 长篇不能只靠模型短期记忆持续生成

没有采用：

- 分镜 / 逐镜生产内容

原因：当前 Skill 明确止于完整剧本。

---

# 6. ZzzTSudio / Kimi-skill-package — screenplay

参考价值：**长剧本任务编排方式**。

重点吸收：

- 整体结构先锁定，再逐单元写作
- 一次只正式写一幕或一集，避免大批量生成时偷工减料
- 连续性强的单元串行处理
- 每一集完成后维护人物状态、物件、信息、未解决剧情
- 写作和 Review 分成不同 Pass
- 视觉叙事需要 Sound-Off Test
- Anti-AI：不同角色声音、少解释、晚进早出

没有采用：

- 强制 Word / docx 输出
- 特定多 Agent / 文件系统命令
- 摄影和制作细节

原因：这些属于具体运行环境或下游生产，不应写死在通用剧本 Skill 中。

---

# 7. ur-grue / autopunk-media-skills — screenwriting suite

参考价值：**原子化、可独立审核的编剧工具设计**。

值得吸收的几个模块：

## beat-sheet-builder

- Beat 必须是具体事件，不是“发生一次挫折”这种占位词
- 结构诊断应指出最薄弱的关键 Beat

## scene-writer

- Scene brief 必须明确人物目标、场景功能和进出状态
- 场景是大故事中的一个变化单元

## dialogue-polisher

- 对白精修与场景结构修复是两件事
- 对白二次 Pass 应保护场景原有戏剧功能
- 去 on-the-nose、区分角色声音、增强潜台词

## script-notes-writer / coverage-report-writer

- Revision 先指出一个根问题
- 问题必须带证据、影响和可执行方向
- 修改优先级按影响排序，而不是平均处理

没有采用：

- 面向制片公司 Coverage 的销售评分作为核心流程

原因：当前项目主要用于内部 AI 剧本创作，而非传统制片公司审稿表。

---

# 8. SkillMedev / Story Structure Architect

参考价值：**宏观结构诊断**。

吸收：

- 结构框架按故事选择，不强行套一种方法
- 中段必须真正改变规则、目标或意义
- 场景 / Beat 按因果而非单纯时间排序
- Setup / Payoff 明确追踪
- 张力曲线允许有谷，但不能长时间停止推进

没有采用：

- 小说章节写作规则

原因：当前 Skill 只做影视剧本。

---

# 9. mudden2380078550-creator / write-chinese-long-screenplay

参考价值：**中文长剧本自然度和人物知识控制**。

吸收：

- 背景设定必须真正改变人物选择和代价
- 人物要区分“知道 / 不知道 / 误信”
- 高压状态下人物如何换策略需要提前考虑
- 中文正文减少模板连接词和过度解释
- 不为了理论标签添加无因果场景

没有采用：

- 只允许两个输入文件的项目工程结构

原因：我们的上游还有实时市场研究、Creative Brief 和本地化研究。

---

# 当前融合后的核心方法

最终不是把所有 Skill 堆在一起，而是压缩成一条统一工作链：

```text
目标国家确认
→ 本次实时市场研究
→ Story DNA / 市场机会
→ 原创 Concept Pool
→ Premise / Theme / Story Spine
→ 人物 / 关系 / 对抗力量
→ Series Engine
→ 全剧宏观结构
→ 全集 Episode Map
→ Setup / Payoff / Reveal Ledger
→ 逐集 Episode Card
→ Scene Contract
→ 中文完整剧本
→ 外语对白 + 中文逐句翻译（需要时）
→ Story Bible / Handoff State
→ 结构审查
→ 人物与关系审查
→ 场景审查
→ 对白二次精修
→ 本地化 / 连续性 / 原创性终审
```

# 核心取舍原则

当不同 Skill 的规则冲突时，按以下优先级处理：

```text
1. 用户明确要求
2. 最新市场事实与目标国家现实
3. 已锁定 Story Bible / 正典事实
4. 因果逻辑与人物选择
5. 当前媒介（海外竖屏短剧）
6. 场景与对白工艺
7. 传统结构模板
```

任何编剧理论都不能推翻已经建立的因果和人物真实性，只能帮助诊断问题。
