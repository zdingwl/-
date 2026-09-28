# Workflow：项目初始化

目标：根据输入自动创建“刚好够用”的工作空间，不让用户手动选十几个模板。

---

# 1. 判断入口

```text
已有小说 / IP / 章节 / 故事素材
→ Adaptation Project

只有概念 / 人物 / 主题 / 冲突
→ Original Project
```

---

# 2. 判断规模

## 短项目

单部短片、单集、短篇素材：

只创建必要状态。

## 中型项目

电影、有限剧、10–30 集：

创建完整 Story Bible + Continuity。

## 长型项目

长篇小说、长季播、30+ 集、百万字素材：

必须创建 Source Index 和全套连续性状态。

---

# 3. Adaptation Project 初始化

最小：

- Project State
- Source Analysis
- Story Bible
- Adaptation Bible

长篇追加：

- Source Index
- Chapter Function Map
- Timeline
- Secret Ledger
- Knowledge State
- Setup / Payoff
- Adaptation Risk Report

---

# 4. Original Project 初始化

最小：

- Project State
- Story Bible
- Character Bible

剧集 / 长篇追加：

- Relationship Map
- Timeline
- Secret Ledger
- Knowledge State
- Setup / Payoff
- Episode Map

---

# 5. 初始化状态

一开始不要伪造正典。

已知用户事实：

LOCKED

为了推进合理补充：

ASSUMED

可能方案：

PROPOSED

明确不要：

REJECTED

---

# 6. 默认连续推进

如果用户已经说“直接做”“继续”“全部完成”：

- 不逐模板请求确认
- 不逐阶段停下
- 非关键缺失参数 ASSUMED 后继续
- 只有根本方向无法合理推断时才需要询问

---

# 7. 初始化完成后的路由

```text
长篇改编
→ workflows/long-novel-adaptation.md

普通改编
→ workflows/novel-adaptation.md

原创
→ workflows/original-screenplay.md
```
