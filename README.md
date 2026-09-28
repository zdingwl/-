# Screenplay Skills Studio

这是一个面向 ChatGPT / Agent Skills 的影视编剧仓库。

## 推荐：只用一个主入口

对于绝大多数“写剧本”任务，直接使用：

`skills/screenplay-studio/SKILL.md`

Screenplay Studio 2.0 已统一支持：

- 小说 / 网文 / 故事 / IP → 剧本
- 长篇、多卷、多文件小说 → 剧本
- 从零原创电影
- 从零原创电视剧 / 流媒体剧集
- 从零原创短剧
- 动画剧本
- 已有剧本诊断与重写
- 单场戏、对白与潜台词

用户不需要先判断该切换哪套编剧 Skill。

~~~text
用户需求
↓
screenplay-studio
├─ original
├─ adaptation
│  ├─ short / medium source
│  └─ long / multi-file source
├─ rewrite
└─ scene_only
↓
feature / episodic_series / short_drama / animation
↓
完整剧本
~~~

## Screenplay Studio 2.0

路径：

`skills/screenplay-studio/SKILL.md`

核心能力：

- 自动任务路由
- Story Contract
- Story Engine
- Character / Relationship Engine
- Structure / Sequence / Episode
- Scene Engine
- Dialogue / Subtext
- Source Index
- Story DNA
- Adaptation Matrix
- 长篇 Source Ingestion
- Story Bible
- Knowledge State
- Script Doctor
- Rewrite Passes
- 120 个 Level 1 知识点
- 120 个 Level 2 深度解析知识点

### 深度知识层

`skills/screenplay-studio/references/knowledge-map-level2.md`

Level 2 不一次性全部加载，而是按当前问题读取对应模块。

## 兼容与专项 Skill

仓库仍保留：

- `skills/novel-to-screenplay-studio/`：旧版长篇改编专项实现与兼容资料；新项目通常不必手动切换，Screenplay Studio 2.0 已内置长篇改编路径。
- `skills/overseas-short-drama-screenwriter/`：海外短剧市场、本地化、平台/国家专项。只有涉及当前市场、目标国家、平台趋势或商业本地化时再使用。

## 快速示例

### 小说改剧本

“把这部小说改成 8 集剧集。先完整读取素材，再做改编设计，最后直接写剧本。”

### 百万字网文

“读取我提供的全部文件，建立 Source Index、Story DNA、Adaptation Matrix 和 Story Bible，再改成 60 集短剧。不要一章一集。”

### 从零原创

“从零写一部 110 分钟悬疑电影。核心设定是……”

### 已有剧本重写

“先做 Script Doctor，找根因，再按优先级重写，不要只润色台词。”

## 共同边界

默认：

- 简体中文
- 用户要完整剧本时必须进入完整场景与对白
- 长项目维护 Story Bible / Continuity / Knowledge State
- 结构模板只用于诊断
- 不用漂亮台词掩盖结构问题
- 不自动混入分镜、摄影、焦段、生图或视频模型提示词
