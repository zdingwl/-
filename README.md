# Screenplay Skills Studio

这是一个面向 ChatGPT / Agent Skills 的影视编剧 Skill 仓库。

当前包含三套分工明确、可以组合使用的系统：

~~~text
skills/
├── screenplay-studio/
├── novel-to-screenplay-studio/
└── overseas-short-drama-screenwriter/
~~~

---

# 1. Screenplay Studio —— 通用编剧主系统

路径：

skills/screenplay-studio/SKILL.md

这是默认的“写剧本”入口。

适用于：

- 从零原创电影剧本
- 从零原创电视剧 / 流媒体剧集
- 从零原创短剧
- 动画剧本
- 故事梗概 → 剧本
- 普通篇幅小说 / 故事 → 剧本
- 已有剧本诊断与重写
- 场景重写
- 对白与潜台词
- Script Doctor

核心流程：

~~~text
Project Brief
→ Premise / Logline
→ Story Contract
→ 人物 / 对抗 / 核心关系
→ Story Engine
→ 结构 / Sequence / Episode
→ Scene Map
→ 场景任务卡
→ 完整剧本
→ Story Bible
→ Script Doctor
→ Rewrite
→ Final Draft
~~~

核心知识：

- 120 个编剧知识点
- Story & Structure Engine
- Character Engine
- Scene & Dialogue Engine
- Series & Episode Engine
- Genre Engine
- Screenplay Format
- Script Doctor
- Rewrite Workflows

中文使用手册：

skills/screenplay-studio/docs/USAGE.zh-CN.md

---

# 2. Novel To Screenplay Studio —— 长小说 / IP 改编专项

路径：

skills/novel-to-screenplay-studio/SKILL.md

这套 Skill 不再作为普通“写剧本”的默认入口。

它主要负责：

- 长篇小说 / 网文 / IP 全量读取
- 多卷 / 多文件素材索引
- Source Index
- Story DNA 提取
- Adaptation Matrix
- 人物 / 支线压缩
- POV 与时间线重排
- 内心戏影视化
- Chapter Function Map
- 长篇 Story Bible
- 大体量改编风险控制
- Writer's Room 改编审稿

当小说体量很大时：

~~~text
novel-to-screenplay-studio
负责“把原作整理成可改编的结构事实”
↓
screenplay-studio
负责“把这些事实真正写成戏”
~~~

---

# 3. Overseas Short Drama Screenwriter —— 海外短剧专项

路径：

skills/overseas-short-drama-screenwriter/SKILL.md

适用于：

- 当前海外短剧市场研究
- 目标国家本地化
- 海外平台与受众
- Trope / 情绪价值分析
- 竖屏商业短剧
- Narrative Momentum
- 连载 Story Engine
- 海外短剧分集
- 海外短剧剧本医生

明确涉及“当前市场 / 热门 / 榜单 / 目标国家”时，应使用实时资料，而不是只依赖训练知识。

---

# 三套 Skill 怎么选

## 用户说“写剧本 / 编剧 / 原创电影 / 原创剧集 / 写短剧”

优先：

screenplay-studio

## 用户给的是超长小说 / 多卷 IP / 百万字网文

先：

novel-to-screenplay-studio

完成原作整理与改编设计后，再回：

screenplay-studio

写正式剧本。

## 用户明确要海外短剧市场、本地化、竖屏商业策略

加载：

overseas-short-drama-screenwriter

如果同时是小说改海外短剧：

~~~text
novel-to-screenplay-studio
→ screenplay-studio
→ overseas-short-drama-screenwriter
~~~

实际执行时只加载当前阶段需要的模块，不要一次性倾倒全部规则。

---

# Screenplay Studio 快速入口

- 主 Skill：skills/screenplay-studio/SKILL.md
- 120 知识地图：skills/screenplay-studio/references/knowledge-map-120.md
- 故事与结构：skills/screenplay-studio/references/story-structure-engine.md
- 人物：skills/screenplay-studio/references/character-engine.md
- 场景与对白：skills/screenplay-studio/references/scene-dialogue-engine.md
- 剧集系统：skills/screenplay-studio/references/series-engine.md
- 类型：skills/screenplay-studio/references/genre-engine.md
- 剧本格式：skills/screenplay-studio/references/screenplay-format.md
- 剧本医生：skills/screenplay-studio/references/script-doctor.md
- 原创工作流：skills/screenplay-studio/workflows/original-screenplay.md
- 故事转剧本：skills/screenplay-studio/workflows/story-to-screenplay.md
- 已有剧本重写：skills/screenplay-studio/workflows/rewrite-existing-script.md
- 中文使用手册：skills/screenplay-studio/docs/USAGE.zh-CN.md

---

# 共同边界

三套 Skill 默认：

- 简体中文输出
- 用户要求完整剧本时必须进入完整场景与对白
- 不用漂亮台词掩盖结构问题
- 长项目维护 Story Bible / Continuity / Knowledge State
- 不把结构模板当唯一真理
- 默认止于剧本
- 不自动混入分镜、镜头、焦段、生图或视频模型提示词
