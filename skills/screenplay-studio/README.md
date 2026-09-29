# Screenplay Studio 2.0

一个统一的影视编剧 Skill。

它同时支持：

- 小说 / 网文 / IP → 剧本
- 从零原创电影
- 从零原创电视剧 / 流媒体剧集
- 从零原创短剧
- 动画剧本
- 已有剧本诊断与重写
- 单场戏与对白重写
- 长篇、多卷、多文件小说的全量改编

## 推荐入口

只安装或只调用：

`skills/screenplay-studio/SKILL.md`

用户不需要先判断“该用原创 Skill 还是小说改编 Skill”。主 Skill 会根据素材规模、媒介和任务阶段自动路由。

## 2.0 的核心变化

- 长篇小说改编并入主 Skill
- 新增 Source Index / Adaptation Matrix / Knowledge State
- 新增长篇全量读取工作流
- 新增 120 知识点 Level 2 深度知识层
- 采用渐进式加载，避免一次塞入全部规则
- 强化“最终必须写成戏”的输出契约
- 强化 Project State / Story Bible / Continuity
- 强化根因级 Script Doctor
- 新增生存灾难 / 重生 / 系统 / 长线连载逻辑引擎
- 新增 World Phase、Future Knowledge、Timeline Divergence、Resource / Capability Ledger、Secrecy / Exposure 与跨季 Hook 状态

## 关键入口

- `SKILL.md`：主路由与执行规范
- `references/knowledge-map-120.md`：Level 1 快速知识地图
- `references/knowledge-map-level2.md`：Level 2 深度知识索引
- `references/knowledge-level2/`：120 个知识点逐条深度解析
- `references/adaptation-engine.md`：小说/IP改编引擎
- `references/source-ingestion.md`：长篇源素材读取
- `references/speculative-survival-serial-engine.md`：末世 / 灾难 / 重生 / 系统 / 资源经营 / 长线连载逻辑规则
- `templates/Serial_Survival_State_Template.md`：长期生存项目状态与伏笔模板
- `workflows/long-novel-to-screenplay.md`：长篇小说→剧本
- `docs/USAGE.zh-CN.md`：中文使用手册
- `docs/INSTALL.zh-CN.md`：安装与 ZIP 打包
- `scripts/package_skill.py`：生成单顶层目录的可安装 Skill ZIP
- `scripts/validate_skill.py`：结构、路径、Level 2、文件数量与大小验证

## 安装包

仓库根目录包含多套 Skill，因此不要直接上传整个仓库。

运行：

~~~bash
python skills/screenplay-studio/scripts/package_skill.py
~~~

默认生成：

`dist/screenplay-studio-2.0.0.zip`

该 ZIP 只包含一个顶层目录 `screenplay-studio/` 和一个 `SKILL.md`。

## 核心边界

本 Skill 负责“剧本”。

除非用户明确要求，不自动混入：

- 分镜
- 摄影镜头
- 焦段
- 灯光参数
- 生图提示词
- 视频提示词
