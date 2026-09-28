# Novel To Screenplay Studio 中文使用手册

## 1. 最简单的用法

让 ChatGPT / Agent 先读取：

`skills/novel-to-screenplay-studio/SKILL.md`

然后直接描述任务。

不需要自己手动指定全部工作流文件；主 Skill 会根据任务自动加载需要的 references 和 workflows。

---

## 2. 小说改编

### 长篇小说 → 剧集

```text
读取 skills/novel-to-screenplay-studio/SKILL.md。

把我提供的小说改编成 8 集流媒体剧。

要求：
- 先完整理解原作，再建立 Story DNA
- 不要按章节一章一集
- 允许合并人物和支线
- 保留核心关系、主题和结局
- 内心戏必须影视化
- 建立 Adaptation Matrix、Story Bible、Knowledge State
- 默认连续推进，不要每个阶段都问我确认
- 最终进入完整剧本正文
```

### 网文 → 短剧

```text
读取主 Skill。
把这部网文改成 60 集短剧。

要求：
- 保留主角、核心关系与结局
- 不按原章节机械切集
- 压缩功能重复角色
- 重排秘密和揭露
- 单集必须有目标、行动、变化和后果
- 高爽但不要重复打脸
- 不要机械每集硬反转
```

### 小说 → 电影

```text
把这部长篇小说改成约 120 分钟电影。
采用功能忠实改编。
保留最重要的人物关系和情绪承诺，
可以删除大量支线和配角。
先做改编决策，再写完整电影剧本。
```

---

## 3. 直接原创剧本

### 原创电影

```text
读取主 Skill。

概念：
一个失忆律师发现，自己曾经替真正的凶手赢下无罪判决。

直接开发成完整悬疑电影剧本。
不要只给创意和大纲。
完成 Premise、人物、Story Spine、Beat、Scene 后继续写完整剧本，并执行 Script Doctor。
```

### 原创剧集

```text
根据下面的概念直接设计一季 10 集剧集。

先建立 Season Engine 和核心关系，
再做 Episode Map、Scene List、完整剧本。
默认连续推进，非关键缺失参数由你合理暂定。
```

---

## 4. 继续已有项目

推荐：

```text
读取当前项目的 Story Bible、LOCKED 决策、最近 Handoff、
Knowledge State、Secret Ledger 和未回收 Setup / Payoff。

继续写第 6 集。
不要重新设计已经确认的角色和结局。
```

如果这些状态文件已经在项目中，Skill 应优先恢复状态，而不是从头讨论。

---

## 5. 剧本医生

```text
读取主 Skill 和这版剧本。

执行 Script Doctor。
先找根问题，不要先润色对白。

诊断顺序：
Premise
→ 主角主动性
→ 因果
→ 人物与关系
→ 结构
→ 场景
→ 信息释放
→ 对白
→ 连续性

按 P0 / P1 / P2 给出修复顺序。
```

---

## 6. 长小说 / 多文件

如果小说很长，可以直接要求：

```text
这是一个长篇小说项目。
请先扫描全部文件 / 章节并建立 Source Index，
然后分块读取并持续更新人物、时间线、秘密、伏笔和 Story Bible。

不要读完一部分就开始猜全剧。
全部关键素材读取完成后再锁 Story DNA 和改编总结构。
```

分块是模型管理上下文的内部手段，不代表把小说拆成多个独立故事。

---

## 7. 什么时候用海外短剧 Skill

如果任务核心是：

- 美国 / 英国 / 日本等目标国家
- 当前海外短剧趋势
- 平台热点
- 海外本地化
- 竖屏商业短剧

可以先用 `novel-to-screenplay-studio` 完成改编核心，再调用：

`skills/overseas-short-drama-screenwriter/SKILL.md`

强化市场和本地化。

---

## 8. 默认行为

默认：

- 简体中文
- 不中途反复确认非关键参数
- 结构问题优先于对白润色
- 长篇维护 Story Bible
- 不自动进入分镜
- 不输出镜头、焦段、生图 / 视频提示词
- 用户要完整剧本时一定进入正文


---

## 9. Genre Engine

如果类型明确，可以直接指定：

```text
读取主 Skill。

Primary Genre：Mystery
Secondary Genre：Family Drama
Tone：克制、现实主义

先建立 Genre Contract，
Mystery 负责核心问题链与 Reveal，
Family Drama 只增强人物关系和情绪，
不要混入高爽短剧规则。
```

或者：

```text
Primary Genre：Romance
要求：
- 慢燃
- 不靠重复误会
- 双方都有主动性
- 每次关系靠近 / 疏远都有具体事件依据
```

当前类型模块见：

`references/genres/README.md`

默认只加载 Primary Genre 和必要 Secondary Genre。
