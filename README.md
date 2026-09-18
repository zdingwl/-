# Overseas Short Drama Screenwriter Skill

一套面向海外短剧 / 微短剧 / AI 漫剧项目的完整编剧 Skill。

它不是分镜 Skill，也不是视频生成 Skill。它负责从市场研究、原创选题、本地化、人物设计、故事结构，到完整剧本写作、诊断和重写。

## 能力范围

- 海外市场与题材趋势研究（需要当前信息时实时检索）
- 原创项目开发与 Creative Brief
- 目标市场本地化
- 人物关系与人物弧设计
- 连载故事发动机设计
- 短剧分集结构与节奏设计
- 场景级完整剧本
- 对白优化与连续性检查
- 独立质检和重写建议

## 项目结构

```text
skills/
└── overseas-short-drama-screenwriter/
    ├── SKILL.md
    ├── evaluations/
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
确认目标国家
→ 市场研究（需要时实时检索）
→ 趋势 / Trope / 情绪价值分析
→ 原创创意池
→ 本地化 Creative Brief
→ 人物与关系
→ Story Engine
→ 分集大纲
→ Beat Sheet
→ Scene List
→ 完整剧本
→ 连贯性 / 本地化 / 原创性 / 节奏检查
→ 最终修订
```

## 使用方式

让支持 Agent Skills / SKILL.md 的 AI 读取：

`skills/overseas-short-drama-screenwriter/SKILL.md`

示例：

- “研究美国最近短剧趋势，原创项目并写成完整短剧剧本。”
- “目标市场英国，女性 25–44 岁，先做市场研究，再创作本地化微短剧。”
- “已有故事梗概，按海外短剧结构完善并输出完整剧本。”

## 质量要求

本 Skill 默认追求：

1. 不停留在创意阶段，而是产出可继续开发的完整剧本。
2. 涉及当前市场判断时，使用当前资料而不是历史印象。
3. 输出前进行结构、人物、节奏和连续性检查。
4. 默认中文输出，只有用户明确要求外语时生成外语。

如果没有指定国家，创作前需要先确认目标市场。