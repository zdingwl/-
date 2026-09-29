---
name: screenplay-studio
description: >
  统一影视编剧主 Skill。用于从零原创电影、电视剧/流媒体剧集、短剧、动画，
  或把小说/网文/故事/IP改成剧本，或诊断重写已有剧本。普通素材与超长/多文件
  小说都在本 Skill 内自动路由；长篇先建立 Source Index、Story DNA、
  Adaptation Matrix、Story Bible 与 Knowledge State，再进入影视结构和剧本正文。
  用户要求写剧本时，最终交付必须是可见、可听、可演的场景、动作和完整对白。
---

# Screenplay Studio 2.0

## 1. 使命

把输入真正写成“戏”。

本 Skill 是通用编剧主入口。用户不需要自己选择“原创 Skill”或“小说改编 Skill”。

支持：

- 从零原创
- 小说 / 网文 / IP / 故事 → 剧本
- 长篇 / 多卷 / 多文件小说 → 剧本
- 已有剧本诊断与重写
- 单场戏、对白与潜台词
- 电影、剧集、短剧、动画

默认简体中文。

## 2. 执行总则

每次执行都遵循：

~~~text
识别任务
→ 选择最小必要模块
→ 建立/读取项目状态
→ 完成当前阶段
→ 进入用户真正要求的交付层
→ 质量诊断
→ 修订
→ 更新项目状态
~~~

不要把内部规划当最终结果。

用户说“写剧本”时，必须进入剧本正文。

用户说“直接做完”时，非根本性缺失自行作合理假设并继续，不逐阶段索要确认。

## 3. 自动路由

内部建立：

~~~yaml
task_router:
  mode: original | adaptation | rewrite | scene_only | development
  source_scale: none | short | medium | long | multi_file
  medium: feature | episodic_series | short_drama | animation
  genre:
  target_scope:
  target_length:
  fidelity: high | functional | free
  current_stage:
  user_goal:
  locked_requirements:
  assumptions:
~~~

### Original

从概念、人物、世界观、类型或一句话创意开发。

读取：

- `references/story-structure-engine.md`
- `references/character-engine.md`
- `references/scene-dialogue-engine.md`
- `workflows/original-screenplay.md`
- 对应媒介 workflow

### Adaptation — short / medium

已有普通体量小说、故事、梗概、IP 或真实素材。

读取：

- `references/adaptation-input.md`
- `references/adaptation-engine.md`
- `workflows/story-to-screenplay.md`

### Adaptation — long / multi_file

几十万字、百万字、多卷、多文件或复杂多 POV 项目。

读取：

- `references/source-ingestion.md`
- `references/adaptation-engine.md`
- `references/project-state-continuity.md`
- `workflows/long-novel-to-screenplay.md`

长篇仍由本 Skill 完成，不要求用户切换到其他 Skill。

### Rewrite

已有剧本诊断、重写、压缩、扩展或局部修复。

读取：

- `references/script-doctor.md`
- `workflows/rewrite-existing-script.md`

### Scene Only

只要求写或改一场时：

- 读取必要前情和项目状态
- 建立 Scene Contract
- 直接写完整场景
- 不重新输出整部大纲

## 4. 媒介路由

### Feature

读取：

- `workflows/feature-film.md`

重点：单一强主线、Sequence 升级、中段重定义、完整人物弧、高潮汇合。

### Episodic Series

读取：

- `references/series-engine.md`
- `workflows/episodic-series.md`

重点：Series Engine、Season Question、Episode Function、A/B/C Lines、长期关系与连续性。

### Short Drama

读取：

- `workflows/short-drama.md`

重点：快速处境、微型戏剧单元、有效变化密度、小兑现→新后果。

涉及当前海外市场、目标国家、平台趋势或商业本地化时，再调用相应专项 Skill 或实时资料。

### Animation

使用同一人物、因果与场景原则；允许更强视觉表达，但世界规则、能力限制和动作后果必须稳定。

## 5. 最小必要加载

不要一次读取整个知识库。

### Level 1

快速开发和常规写作按需读取：

- `references/knowledge-map-120.md`
- `references/story-structure-engine.md`
- `references/character-engine.md`
- `references/scene-dialogue-engine.md`
- `references/series-engine.md`
- `references/genre-engine.md`
- `references/screenplay-format.md`
- `references/script-doctor.md`

### Level 2

复杂项目、反复修不好或需要根因诊断时读取：

- `references/knowledge-map-level2.md`

再只加载 `references/knowledge-level2/` 中与当前问题对应的模块。

Level 2 每个知识点包含：

- 定义
- 机制
- 诊断
- 常见失败
- 修复

## 6. 项目状态

中长项目必须维护：

- Canon
- LOCKED / ASSUMED / PROPOSED / REJECTED
- Story Contract
- Character State
- Relationship State
- Timeline
- Locations
- Objects / Resources / Evidence
- Secrets
- Audience Knowledge
- Character Knowledge
- Setup / Payoff
- Adaptation Ledger
- Unresolved Questions
- Current / Completed Units
- Rewrite History

读取：

- `references/project-state-continuity.md`
- `templates/Project_State_Template.md`

不要用模糊记忆替代 Story Bible。

## 7. 核心编剧顺序

原创：

~~~text
Project Contract
→ Premise / Logline
→ Audience Promise / Genre Contract
→ Dramatic Question / Theme Question
→ Protagonist Want / Need / Misbelief
→ Opposing Force / Stakes / Core Relationship
→ Story Engine
→ Ending State
→ Structure
→ Sequence / Episode
→ Scene Map
→ Scene Contracts
→ Draft
→ Script Doctor
→ Rewrite
~~~

改编：

~~~text
Source Ingestion
→ Source Index
→ Canon / Timeline / Knowledge State
→ Story DNA
→ Adaptation Contract
→ Adaptation Matrix
→ Character / Subplot Compression
→ POV / Reveal / Timeline Redesign
→ Interior Externalization
→ Screen Causality
→ Medium Structure
→ Scene Map
→ Draft
→ Adaptation Integrity Review
→ Rewrite
~~~

## 8. 不可绕过的戏剧规则

1. 主角必须通过选择推动主要因果。
2. 对抗力量必须拥有独立目标并会适应主角。
3. 重大事件尽量由“因为 / 所以 / 但是 / 因此”连接。
4. 关键选择必须产生后果并改变后续可选空间。
5. 结构服务压力与选择，不机械填节点。
6. 场景必须存在目标、阻力、策略、反制、转折和状态变化。
7. 对白首先是行动，不是剧情说明书。
8. 心理优先外化为选择、行为、关系策略、道具、空间和信息控制。
9. 信息释放必须区分观众知道什么、人物知道/误信/不知道什么。
10. 高潮不能靠偶然替主角解决核心问题。
11. 长项目必须更新连续性状态。
12. 改编保留“功能与情绪承诺”，而非逐句搬运。

详细机制按需读取 Level 1 / Level 2 文件。

## 9. 改编决策

重要源元素使用：

- KEEP
- TRANSFORM
- MERGE
- MOVE
- CUT
- INVENT

每项至少判断：

- 原作功能
- 情绪价值
- 因果依赖
- 识别度
- 屏幕可执行性
- 新影视功能
- 影响项
- 风险

模板：

- `templates/Adaptation_Matrix_Template.md`

禁止机械“一章一集”。

## 10. 长篇读取门槛

长篇正式进入 Adaptation Design 前，至少确认：

- 主线因果可追踪
- 主要人物功能已知
- 结局已读取
- 核心秘密与 Reveal 顺序已知
- 关键 Setup / Payoff 已索引
- 后文对前文的重解释已检查
- 核心情绪承诺可说明
- 主要人物 Knowledge State 可追踪

条件不满足时继续读取源素材，不根据前几章猜整部作品。

## 11. Scene Contract

正式写关键场景前，内部至少明确：

~~~yaml
scene_contract:
  location_time:
  entering_state:
  dramatic_question:
  character_goal:
  obstacle:
  tactic:
  counter_tactic:
  information_in_play:
  subtext:
  turn:
  value_shift:
  consequence:
  exiting_state:
  why_next_scene:
~~~

最小逻辑：

~~~text
目标
→ 尝试
→ 阻力
→ 策略变化
→ 反制
→ 转折
→ 状态变化
→ 后果
~~~

## 12. Script Doctor

诊断顺序：

~~~text
Premise / Audience Promise
→ Story Engine
→ Protagonist Agency
→ Opposing Force
→ Stakes
→ Causality
→ Character / Core Relationship
→ Structure
→ Sequence / Episode
→ Scene Turns
→ Information Design
→ Dialogue
→ Visual Action
→ Continuity
→ Format
~~~

出现上游问题时，不先润色下游。

## 13. 正文与格式

默认使用 Master Scene 思路。

正文主要包含：

- Scene Heading
- Action
- Character
- Dialogue
- Parenthetical（必要时）
- Transition（必要时）

读取：

- `references/screenplay-format.md`

除非用户明确要求，不自动写：

- 景别
- 焦段
- 推拉摇移
- 灯光参数
- 分镜
- 生图提示词
- 视频提示词

动作行只写可见、可听、可演的信息。

## 14. 输出契约

### 用户要开发

可以交付：

- Project Contract
- Story Contract
- 人物/关系
- Structure / Episode Map
- Scene Map
- 风险与待定项

### 用户要写剧本

最终必须交付：

- 场景标题
- 可见动作
- 人物行为
- 角色名
- 完整对白
- 场景转折
- 后果

### 用户要小说改剧本

不要把 Source Index、Story DNA 或改编分析当最终成品。

默认走到：

~~~text
必要的改编定位
→ 核心改编决策
→ 影视版结构
→ 剧本正文
~~~

### 用户要诊断

输出：

- 症状
- 证据
- 根因
- 严重度
- 修复顺序
- 具体改法

用户同时要求重写时，诊断后继续执行重写。

## 15. 失败模式

禁止：

- 把小说分析当剧本
- 用户要正文却只给大纲
- 一章等于一集
- 用旁白承包全部内心戏
- 主角长期被剧情拖着走
- 对手只在作者需要时出现
- 中段重复前段
- 高潮靠偶然解决
- 场景只有信息没有争夺
- 所有人说话像同一个作者
- 固定每 N 秒制造反转
- 长项目不维护状态
- 角色知道自己不该知道的信息
- 无要求混入摄影、分镜或生成模型提示词

## 16. 完成检查

~~~text
□ 路由正确
□ 目标媒介明确
□ 长篇素材完成必要全局读取
□ Story Contract 成立
□ 主角持续做选择
□ 对抗力量会反制
□ Stakes 具体并升级
□ 重大剧情有因果
□ 中段产生实质改变
□ 高潮来自人物高代价选择
□ 人物弧有行为证据
□ 核心关系真实变化
□ 场景有目标、阻力、转折和后果
□ 对白具有行动与潜台词
□ 主要人物声音可区分
□ 心理已尽量外化
□ 信息与秘密状态清楚
□ Setup / Payoff 可追踪
□ 长项目连续性稳定
□ 正文可见、可听、可演
□ 用户要剧本时已真正进入剧本正文
~~~
