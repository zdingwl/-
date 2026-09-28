# v2.1.0 Release Notes

## Novel To Screenplay Studio 2.1

2.1 的重点不是继续增加编剧理论，而是把 2.0 的知识体系变成可长期运行的“项目工作空间”。

## 新增：项目模板系统

新增项目状态与生产模板，覆盖：

- Project State
- Story Bible
- Source Index
- Source Analysis
- Adaptation Bible
- Adaptation Risk Report
- Character Bible
- Relationship Map
- Timeline
- Knowledge State
- Secret Ledger
- Setup / Payoff
- Chapter Function Map
- Episode Map
- Scene List
- Script Draft
- Revision Report

## 新增：百万字小说改编管线

正式流程：

```text
项目初始化
→ 全量目录扫描
→ Source Index
→ 分块功能读取
→ 全局增量合并
→ 关键段二次深读
→ Story Bible 收敛
→ Adaptation Risk
→ Chapter Function Map
→ Sequence
→ Episode / Act
→ Scene
→ Draft
→ Handoff
→ Revision
```

### 关键变化

不允许：

```text
第1章 = 第1集
第2章 = 第2集
```

现在改为：

```text
章节
→ 戏剧功能
→ 状态变化
→ Sequence
→ Episode / Act
```

## 新增：人物关系抽取

关系图从实际互动事件生成，持续跟踪：

- 权力
- 信任
- 依赖
- 秘密
- 欲望
- 冲突
- 关系转折

不再仅靠“母女 / 情侣 / 同事”等身份标签。

## 新增：Story Bible 自动收敛

长篇素材读取后，系统会从 Source Index 中收敛：

- 正典事实
- 人物
- 关系
- 时间线
- 秘密
- 知识状态
- Setup / Payoff
- Story DNA

并区分：

LOCKED / ASSUMED / PROPOSED / REJECTED。

## 新增：改编风险与评分

可诊断：

- 压缩压力
- 多 POV 难度
- 内心叙述负担
- 时间线复杂度
- 人物合并风险
- Reveal 风险
- 制作规模风险
- 目标媒介适配度

评分只用于发现改编工作量，不用于机械判断作品优劣。

## 推荐入口

`skills/novel-to-screenplay-studio/SKILL.md`

## 长篇入口

`skills/novel-to-screenplay-studio/workflows/long-novel-adaptation.md`

## 项目模板

`skills/novel-to-screenplay-studio/templates/README.md`
