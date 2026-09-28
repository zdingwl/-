# Screenplay Skills Studio

这是一个面向 ChatGPT / Agent Skills 的编剧 Skill 仓库。

当前包含两套互补系统：

```text
skills/
├── novel-to-screenplay-studio/
└── overseas-short-drama-screenwriter/
```

---

# 1. Novel To Screenplay Studio

路径：

`skills/novel-to-screenplay-studio/SKILL.md`

用于：

- 小说 / 网文 / IP → 电影剧本
- 小说 / 网文 / IP → 电视剧 / 流媒体剧集
- 小说 / 网文 / IP → 短剧
- 小说 / IP → 动画剧本
- 一个概念 → 原创电影
- 一个概念 → 原创剧集
- 一个概念 → 原创短剧
- 一个概念 → 原创动画
- 剧本诊断与重写

核心不是“把小说改成对白”，而是：

```text
读取素材
→ 提取 Story DNA
→ 改编取舍
→ 内心戏外化
→ 人物 / 支线重构
→ POV / 时间 / Reveal 重排
→ 媒介适配
→ 结构
→ Beat / Episode
→ Scene
→ 完整剧本
→ Story Bible
→ Script Doctor
→ Final
```

### 关键文件

```text
skills/novel-to-screenplay-studio/
├── SKILL.md
├── README.md
├── references/
│   ├── knowledge-map-120.md
│   ├── adaptation-engine.md
│   ├── original-screenplay-engine.md
│   ├── medium-profiles.md
│   ├── scene-dialogue-craft.md
│   ├── continuity-story-bible.md
│   ├── revision-quality-gates.md
│   ├── output-templates.md
│   └── craft-sources.md
├── workflows/
│   ├── novel-adaptation.md
│   └── original-screenplay.md
└── evaluations/
    ├── README.md
    ├── rubric.md
    └── cases.md
```

### 120 知识点地图

`references/knowledge-map-120.md`

覆盖：

- 项目定义
- Story DNA
- 改编取舍
- 内心戏影视化
- POV
- 人物重构
- 结构与因果
- 场景
- 对白
- 电影 / 剧集 / 短剧 / 动画
- Story Bible
- Knowledge State
- 原创开发
- Script Doctor
- 回归测试

---

# 2. Overseas Short Drama Screenwriter

路径：

`skills/overseas-short-drama-screenwriter/SKILL.md`

这是面向海外短剧 / 微短剧 / AI 漫剧的专项系统。

适合：

- 当前海外短剧市场研究
- 目标国家本地化
- Trope / 情绪价值分析
- 海外短剧原创开发
- 连载 Story Engine
- Narrative Momentum
- 短剧分集
- 完整短剧剧本
- 长篇连续性
- 剧本医生与独立质检

核心流程：

```text
目标国家
→ 当前市场研究
→ 创作模式
→ Creative Brief
→ 人物与关系
→ Story Engine
→ Narrative Momentum
→ 全剧结构
→ Episode Map
→ 完整剧本
→ Continuity
→ Script Doctor
→ Final
```

---

# 两套 Skill 怎么选

## 用 Novel To Screenplay Studio

当任务核心是：

- 小说改编
- IP 改编
- 电影
- 电视剧 / 流媒体
- 动画
- 通用原创剧本
- 通用剧本诊断

## 用 Overseas Short Drama Screenwriter

当任务核心是：

- 海外短剧市场
- 目标国家本地化
- 当前热门题材
- 竖屏短剧商业创作
- 海外短剧发行逻辑

如果是：

> “把一部小说改成海外短剧”

推荐先用：

`novel-to-screenplay-studio`

完成改编核心、人物压缩和影视结构，

再使用：

`overseas-short-drama-screenwriter`

做目标国家市场、本地化和短剧专项强化。

---

# 使用示例

### 小说 → 剧集

> 把这部长篇小说改成 8 集流媒体剧。先读取全部素材，建立 Story DNA 和改编决策，不要按章节一章一集，然后写完整剧本。

### 小说 → 短剧

> 把这部网文改成 60 集短剧。保留主角、核心关系和结局，可以合并角色和支线。每集必须来自完整因果，不要机械反转。

### 直接原创电影

> 我只有一个概念：一个失忆律师发现自己曾替真正的凶手赢下无罪判决。直接开发成完整悬疑电影剧本。

### 直接原创剧集

> 根据这个世界观设计一季 10 集剧集，从人物、Season Engine、Episode Map 到完整剧本。

### 剧本医生

> 读取这版剧本，先找根问题。不要先改台词，按 Premise、主角主动性、因果、结构、场景、信息、对白、连续性的顺序诊断。

---

# 共同边界

两套 Skill 都默认：

- 简体中文输出
- 用户要求完整剧本时必须进入完整场景和对白
- 不用漂亮台词掩盖结构问题
- 长项目维护 Story Bible / Continuity
- 不把结构模板当成唯一真理
- 默认止于剧本
- 不自动混入分镜、镜头、焦段、生图或视频模型提示词
