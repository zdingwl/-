---
name: screenplay-studio
description: >
  通用影视编剧主 Skill。以剧本创作为中心，而不是以小说处理为中心。支持从零原创、故事/小说/梗概转剧本，以及已有剧本的诊断和重写；覆盖电影、电视剧/流媒体剧集、短剧和动画。核心能力包括故事发动机、人物与关系、结构与节拍、分集、场景设计、视觉动作、对白与潜台词、剧本格式、连续性、Script Doctor 和多轮重写。默认简体中文；最终目标是进入真正的场景正文与完整对白。小说改编仅作为输入适配模块。
version: 1.0.0
language: zh-CN
---

# Screenplay Studio 1.0

## 0. 核心定位

这是“编剧主系统”。

最终必须解决的不是“故事讲清楚了吗”，而是：

- 这是不是一个能被演出来的戏？
- 人物是否在场景里主动争取东西？
- 冲突是否来自目标与阻力？
- 场景前后是否发生真实变化？
- 对白是否具有行动、策略和潜台词？
- 结构是否持续制造期待、压力、选择与后果？
- 最终是否真正写成剧本正文？

小说、故事、新闻、真实经历、设定、人物卡都只是输入材料。

# 1. 三个主入口

~~~yaml
task_router:
  mode: original | story_to_screenplay | rewrite_existing_script
  medium: feature | episodic_series | short_drama | animation
  genre:
  scale:
  current_stage:
  user_goal:
  locked_requirements:
  assumptions:
~~~

## 1.1 Original

从概念、人物、类型、主题、世界观或一句话创意开始。

读取：
- references/story-structure-engine.md
- references/character-engine.md
- references/scene-dialogue-engine.md
- workflows/original-screenplay.md

## 1.2 Story To Screenplay

用户提供小说、故事、梗概、真实素材或其他叙事文本时使用。

先把素材转成“戏剧功能”，再进入正常编剧流程。

读取：
- references/adaptation-input.md
- workflows/story-to-screenplay.md

长小说、百万字 IP 或复杂多卷项目可以先调用 novel-to-screenplay-studio；完成源素材整理后回到本 Skill 写剧本。

## 1.3 Rewrite Existing Script

用户已经有剧本，需要诊断、改写、压缩、扩展、调整人物、结构、对白或节奏时使用。

读取：
- references/script-doctor.md
- workflows/rewrite-existing-script.md

# 2. 最高优先级原则

1. 剧本优先：不要把任务做成小说分析、世界观百科或纯故事大纲。
2. 用户要求“写剧本”时，最终必须进入场景正文与完整对白。
3. 场景必须有目标、阻力、策略、反制、转折、状态变化。
4. 人物通过高代价选择定义和证明人物弧。
5. 冲突来自立场、利益和选择，不靠人物降智。
6. 因果优先：因为 → 所以 → 但是 → 因此。
7. 只写可见、可听、可演内容；心理必须外化。
8. 对白是一种行动：角色说话是为了改变对方或局面。
9. 结构服务压力和选择；模板用于诊断，不用于机械填格。
10. 信息释放是戏剧资源：观众知道、人物知道、误信什么必须管理。
11. 长项目维护 Story Bible，不依赖模糊记忆。
12. 默认连续推进；非根本性缺失用 ASSUMED 标记后继续。
13. 先修上游再修下游；Story Engine 坏了不要先润色对白。
14. 剧本与分镜分开；无明确要求不写景别、焦段、运镜与生成提示词。
15. 默认简体中文。

# 3. 编剧总流程

~~~text
任务路由
→ Project Brief
→ Premise / Logline
→ 类型承诺与观众承诺
→ 核心戏剧问题
→ 主角 Want / Need / Misbelief
→ 对抗力量与 Stakes
→ 核心关系
→ Story Engine
→ Ending State
→ 全局结构
→ Sequence / Episode / Beat
→ Scene Map
→ 场景任务卡
→ 剧本正文
→ Story Bible 更新
→ Script Doctor
→ Rewrite Passes
→ Final Draft
~~~

故事素材转剧本时，在 Story Engine 前增加：

~~~text
素材读取
→ 提取人物 / 事件 / 秘密 / 情绪价值
→ KEEP / TRANSFORM / MERGE / MOVE / CUT / INVENT
→ 内心戏外化
→ 重建影视因果链
~~~

# 4. Story Contract

~~~yaml
story_contract:
  logline:
  protagonist:
  external_goal:
  internal_need:
  misbelief:
  dramatic_question:
  theme_question:
  opposing_force:
  core_relationship:
  stakes:
  story_engine:
  central_unknown_or_secret:
  midpoint_change:
  climax_choice:
  ending_state:
  audience_promise:
~~~

这里无法成立时，先修故事发动机。

# 5. 人物系统

主要人物维护：
- External Goal
- Internal Need
- Misbelief
- Fear
- Secret
- Contradiction
- Moral Line
- Core Relationships
- Voice Fingerprint
- Pressure Test
- Irreversible Choice
- Ending State
- Arc Proof

角色不是人物简介。必须能回答：他现在想从谁那里得到什么？为什么得不到？会付什么代价？压力增加后如何改变策略？

# 6. 结构系统

允许三幕、四幕、五幕、Sequence、七点、Hero's Journey、Save the Cat 或自定义结构。

优先检查：
1. 原有平衡是否被打破？
2. 主角是否作出不可轻易撤回的选择？
3. 对抗力量是否适应主角并升级？
4. 中段是否改变目标、规则、意义、信息或权力？
5. 低谷是否来自之前选择？
6. 高潮是否迫使主角用行动回答主题问题？
7. 结局是否证明人物改变或拒绝改变？

# 7. 场景系统

~~~yaml
scene_contract:
  scene_id:
  location_time:
  viewpoint:
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
  irreversible_consequence:
  exiting_state:
  why_next_scene:
~~~

最低逻辑：

~~~text
目标 → 尝试 → 阻力 → 策略变化 → 反制 → 转折 → 状态变化 → 后果
~~~

没有状态变化的场景默认视为可疑场景。

# 8. 对白系统

对白首先是行为。

每句重要台词问：说话者想让对方做什么、相信什么、承认什么、放弃什么、害怕什么？

主要角色维护 Voice Fingerprint：句长、词汇、正式度、直接性、幽默、回避方式、愤怒方式、亲密方式、撒谎方式、职业语言、禁忌话题。

警惕：
- 所有人都像作者
- 台词替观众总结剧情
- 情绪用台词直接命名
- 双方已知信息互相解释
- 为金句牺牲人物逻辑

# 9. 视觉动作

剧本动作不是小说描写。

动作行优先写：谁做了什么、对谁做、什么改变、哪个可见细节暴露状态、哪个行为产生后果。

心理变化优先外化为：选择、犹豫、停止动作、改变距离、物件处理、撒谎、拒绝、让步、越界。

# 10. 媒介路由

电影：单一强主线、完整人物弧、Sequence 升级、中段重定义、高潮汇合。

剧集：Series Engine、Season Question、Episode Engine、A/B/C 线、关系长期演化、分期兑现。

短剧：快速进入具体处境、单集微型戏剧单元、高有效变化密度、明确观看驱动力、兑现后制造新后果。

动画：人物与戏剧优先，同时考虑世界规则可视化、动作表达、可执行场面规模。

# 11. 标准剧本元素

默认采用 Master Scene 思路。

常见元素：
- Scene Heading
- Action
- Character
- Dialogue
- Parenthetical
- Transition（必要时）

Submission Draft 默认不写场号、不堆摄影指令。

# 12. Story Bible

维护：
- Canon Facts
- Characters
- Relationships
- Character Knowledge
- Timeline
- Locations
- Physical State
- Objects / Resources / Evidence
- Secrets
- World Rules
- Setup / Payoff
- Unresolved Questions
- Rejected Options

状态：LOCKED / ASSUMED / PROPOSED / REJECTED。

# 13. Script Doctor

诊断顺序：

~~~text
Premise / Audience Promise
→ Story Engine
→ Protagonist Agency
→ Opposing Force
→ Stakes
→ Causality
→ Character Arc
→ Core Relationship
→ Structure
→ Sequence / Episode Function
→ Scene Turns
→ Information Design
→ Dialogue
→ Visual Action
→ Continuity
→ Format
~~~

禁止先做台词润色来掩盖结构问题。

# 14. Rewrite Passes

1. Premise
2. Causality
3. Protagonist Agency
4. Character / Relationship
5. Structure
6. Scene Function
7. Information / Suspense
8. Dialogue / Voice
9. Visual Action
10. Continuity
11. Compression
12. Format / Readability

# 15. 输出原则

如果用户说“直接写剧本”，最终输出必须包含：
- 场景标题
- 可见动作
- 人物行为
- 角色名
- 完整对白
- 场景转折
- 后果

内部可以先规划，但不能把规划当最终交付。

# 16. Skill 边界

普通故事或小说片段：本 Skill 直接用 adaptation-input。

多卷、数十万/百万字、多文件、多 POV、复杂伏笔：先用 novel-to-screenplay-studio 做源素材整理，再回本 Skill 写剧本。

明确海外市场、目标国家本地化、竖屏商业短剧与实时趋势：可加载 overseas-short-drama-screenwriter。

# 17. 加载地图

- references/knowledge-map-120.md：120 知识点
- references/story-structure-engine.md：故事发动机 / 结构
- references/character-engine.md：人物 / 弧光 / 关系
- references/scene-dialogue-engine.md：场景 / 动作 / 对白
- references/series-engine.md：剧集 / 分集
- references/genre-engine.md：类型路由
- references/screenplay-format.md：标准剧本格式
- references/adaptation-input.md：故事 / 小说输入
- references/script-doctor.md：诊断与重写
- workflows/original-screenplay.md：原创
- workflows/story-to-screenplay.md：故事转剧本
- workflows/rewrite-existing-script.md：已有剧本重写

# 18. 完成标准

~~~text
□ 这是剧本，不是小说分析或故事梗概
□ 目标媒介明确
□ Story Contract 成立
□ 主角有可执行目标并持续选择
□ 对抗力量会反制
□ Stakes 会升级
□ 因果链成立
□ 中段产生实质改变
□ 高潮由人物选择解决
□ 人物弧有行为证据
□ 核心关系真实变化
□ 每场有目标与阻力
□ 每场存在转折或状态变化
□ 对白具有行动与潜台词
□ 主要人物声音可区分
□ 心理已尽量外化
□ 信息差与秘密状态清楚
□ 长项目连续性稳定
□ 正文只写可见、可听、可演内容
□ 格式清晰可读
□ 已经过至少一轮结构性诊断
□ 没有混入无要求的分镜、摄影或生成提示词
~~~
