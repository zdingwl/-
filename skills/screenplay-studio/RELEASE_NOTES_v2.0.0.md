# Screenplay Studio 2.0.0

## 一句话

从“几套编剧 Skill 需要人工选择”，升级为“一个主 Skill 自动处理原创、小说改编、长篇改编和剧本重写”。

## 主要变化

### 1. 一个主入口

以后常规使用只需要：

`skills/screenplay-studio/SKILL.md`

### 2. 百万字小说也在同一 Skill 内处理

新增长篇 Source Ingestion：

- Source Manifest
- Source Index
- Canon
- Timeline
- Character Knowledge
- Relationship Events
- Setup / Payoff
- Reveal Ledger
- Story DNA
- Adaptation Matrix

### 3. 120 点 Level 2

Level 1 告诉模型“检查什么”。

Level 2 进一步告诉模型：

- 为什么成立
- 怎么诊断
- 常见错误是什么
- 应该怎么修

### 4. 更少无意义确认

非根本性缺失自动使用 ASSUMED 推进。

### 5. 更严格的最终交付

用户要剧本时，不能停在分析、大纲、Beat Sheet 或人物小传。

最终必须真正进入：

- 场景
- 动作
- 人物
- 完整对白
- 转折
- 后果
