# Overseas Short Drama Screenwriter Skill

一套面向海外短剧 / 微短剧 / AI 漫剧的完整编剧 Skill。

它不是分镜 Skill，也不是视频生成 Skill。它负责从最新海外短剧与网络小说趋势研究开始，完成原创选题、本地化、人物、全剧结构、分集结构、逐场写作、对白、完整剧本和重写审校。

## 目录

```text
skills/
└── overseas-short-drama-screenwriter/
    ├── SKILL.md
    └── references/
        ├── market-research.md
        ├── story-development.md
        ├── localization.md
        ├── screenplay-writing.md
        ├── quality-gates.md
        └── output-templates.md
```

## 核心工作流

```text
最新海外市场研究
→ 趋势 / Trope / 情绪价值提炼
→ 原创创意池
→ 本地化 Creative Brief
→ 人物与关系
→ 全剧 Story Engine
→ 分集大纲
→ Episode Beat Sheet
→ Scene List
→ 逐场完整剧本
→ 连贯性 / 本地化 / 原创性 / 节奏审校
→ 最终剧本
```

默认目标是：**写出完整剧本，而不是只提供创意或大纲。**

## 使用方式

让支持 Agent Skills / SKILL.md 的 AI 读取：

`skills/overseas-short-drama-screenwriter/SKILL.md`

典型调用：

- “研究美国最近 30 天短剧和网文趋势，原创 5 个项目，选最佳一个写成 60 集完整短剧剧本。”
- “目标市场英国，女性 25–44 岁，先研究最新榜单，再写一个本地化英文微短剧。”
- “这是我的故事梗概，不需要重新选题，直接按海外短剧方式完善并写完整剧本。”

如果没有指定国家，Skill 默认优先按 **美国英语市场** 工作，但在开始创作前仍应重新检查最新市场数据。
