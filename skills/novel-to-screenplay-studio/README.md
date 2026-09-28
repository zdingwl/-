# Novel To Screenplay Studio

面向 ChatGPT / Agent Skills 的完整编剧 Skill。

它解决两类任务：

1. **小说 / IP / 既有故事 → 影视剧本**
2. **原创概念 → 完整剧本**

支持电影、电视剧/流媒体剧集、短剧和动画。

## 这套 Skill 不是什么

它不是“把小说句子改成对白”的转换器，也不是分镜、摄影、图片或视频生成 Skill。

它的核心工作是：

- 找到原作真正的 Story DNA
- 决定保留、变形、合并、移动、删除和新增
- 把内心叙述转换成可见行动与选择
- 重构人物目标、关系和人物弧
- 重排时间线、秘密和信息释放
- 设计适合目标媒介的结构
- 把结构写成真正的场景与完整对白
- 用 Story Bible 控制长篇连续性
- 用 Script Doctor 流程做结构性修订

## 入口

主文件：

`SKILL.md`

核心知识：

`references/knowledge-map-120.md`

小说改编：

`workflows/novel-adaptation.md`

原创剧本：

`workflows/original-screenplay.md`

## 使用示例

- “把我这部长篇小说改成 8 集流媒体剧，每集约 45 分钟。”
- “把这部网文改成 60 集短剧，但不要按章节一章一集。”
- “我只有一个概念：一个失忆律师发现自己曾经替凶手辩护。直接写成电影剧本。”
- “继续写第 4 集，沿用前面已经锁定的人物关系和秘密状态。”
- “对这版剧本做 Script Doctor，先找根问题，不要先润色台词。”

## 与仓库中现有海外短剧 Skill 的关系

`novel-to-screenplay-studio` 是通用编剧与改编主系统。

`overseas-short-drama-screenwriter` 是面向海外短剧市场研究、本地化和竖屏连续短剧的专项系统。

如果任务明确是“海外市场驱动短剧”，专项 Skill 更细；如果任务核心是“小说改编 / 原创电影 / 剧集 / 动画 / 通用短剧”，使用本 Skill。

## 默认输出

默认简体中文。

只有用户明确要求时生成英文或其他语言。

剧本阶段默认不包含分镜、镜头、焦段、运镜、生图或视频模型提示词。


## 快速入口

- 中文使用手册：`docs/USAGE.zh-CN.md`
- 小说改编示例：`examples/Example_Adaptation_Project.md`
- 原创剧本示例：`examples/Example_Original_Project.md`
- 版本记录：`CHANGELOG.md`
- v2.0.0 发布说明：`RELEASE_NOTES_v2.0.0.md`

## 长篇项目

长小说、多文件和多集项目默认采用：

```text
Source Index
→ 分块读取
→ Story Bible
→ Adaptation / Story Design
→ 正式写作
→ Handoff
```

分块读取不会把每个文件当成独立故事；全局人物、时间线、秘密和伏笔持续汇总。

默认连续推进。除非缺失信息会改变故事根本方向，否则不会在每个阶段反复要求确认。
