---
name: screenplay-studio
description: >
  统一影视编剧主 Skill。用户要从零原创电影、电视剧/流媒体剧集、短剧、动画，或把小说/网文/故事/IP改成剧本，或诊断重写已有剧本时使用。普通素材与超长/多文件小说都在本 Skill 内自动路由；长篇先建立 Source Index、Story DNA、Adaptation Matrix、Story Bible 与 Knowledge State，再进入影视结构和剧本正文。最终默认交付可见、可听、可演的场景、动作与完整对白，而不是停在分析、大纲或小说式叙述。
---

# Screenplay Studio 2.0

## 0. 核心使命

这是一个“真正把故事写成戏”的主 Skill。

它必须同时处理两类核心任务：

1. 从已有小说、网文、故事、IP、真实素材中重建影视剧本。
2. 从概念、人物、类型、世界观或一句话创意直接开发原创剧本。

也支持：

- 已有剧本诊断与重写
- 单场戏重写
- 对白与潜台词
- 电影、剧集、短剧、动画
- 长篇/多卷/多文件项目的连续性管理

用户只需要提出创作目标，不需要自己判断该加载哪套编剧 Skill。

---

# 1. 自动任务路由

先在内部建立：

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
  supplied_material:
  missing_but_nonblocking:
  assumptions:
~~~

## 1.1 Original

用户没有必须忠实的源故事，或明确要求从零写。

读取：

- references/story-structure-engine.md
- references/character-engine.md
- references/scene-dialogue-engine.md
- workflows/original-screenplay.md
- 对应媒介 workflow

## 1.2 Adaptation

用户提供小说、网文、故事、IP、真实经历或其他叙事素材。

短/中等素材：

- references/adaptation-input.md
- references/adaptation-engine.md
- workflows/story-to-screenplay.md

长篇、多卷、多文件、数十万字/百万字：

- references/source-ingestion.md
- references/adaptation-engine.md
- workflows/long-novel-to-screenplay.md

长篇改编仍由本 Skill 完成，不要求用户切换到另一个 Skill。

## 1.3 Rewrite

已有剧本需要诊断或重写。

读取：

- references/script-doctor.md
- workflows/rewrite-existing-script.md
- 必要时加载 Level 2 对应知识模块

## 1.4 Scene Only

用户只要求写或改一场戏时，不重新输出整部项目开发文档。

先读取用户给出的必要前情与当前 Story Bible 状态，然后直接建立 Scene Contract 并写正文。

---

# 2. 渐进式加载，而不是规则倾倒

主 SKILL.md 负责：

- 路由
- 阶段控制
- 状态管理
- 输出标准
- 质量门槛

深层知识只在当前任务需要时读取。

## Level 1

快速工作知识：

- references/knowledge-map-120.md
- references/story-structure-engine.md
- references/character-engine.md
- references/scene-dialogue-engine.md
- references/series-engine.md
- references/genre-engine.md
- references/screenplay-format.md
- references/script-doctor.md

## Level 2

深度诊断、复杂项目、反复修订时读取：

- references/knowledge-map-level2.md
- references/knowledge-level2/

不要无差别加载 120 个深层条目。

---

# 3. 项目状态

中长项目必须维护内部 Project State。

~~~yaml
project_state:
  project_contract:
  canon:
  assumptions:
  proposed:
  rejected:
  story_contract:
  character_states:
  relationship_states:
  timeline:
  locations:
  objects_resources_evidence:
  secrets:
  audience_knowledge:
  character_knowledge:
  setups_payoffs:
  adaptation_ledger:
  unresolved_questions:
  current_unit:
  completed_units:
  rewrite_history:
~~~

状态标签：

- LOCKED：用户或文本已确认的正典
- ASSUMED：为了推进而临时补全
- PROPOSED：候选方案
- REJECTED：已否决，不得重新混入

不要用“模型记得大概”替代 Story Bible。

---

# 4. 原创剧本总流程

~~~text
需求解析
→ Project Contract
→ Premise / Logline
→ Audience Promise / Genre Contract
→ Dramatic Question / Theme Question
→ Protagonist Want / Need / Misbelief
→ Opposing Force / Stakes / Core Relationship
→ Story Engine
→ Ending State
→ Global Structure
→ Sequence / Episode Design
→ Scene Map
→ Scene Contracts
→ Draft
→ Story Bible Update
→ Script Doctor
→ Rewrite Passes
→ Final Draft
~~~

当用户说“直接写”，内部仍可完成必要规划，但最终交付不能停在规划层。

---

# 5. 小说 / IP 改编总流程

改编不是把原文压短，也不是把叙述改成对白。

核心流程：

~~~text
Source Ingestion
→ Source Index
→ Canon / Timeline / Character Knowledge
→ Story DNA
→ Adaptation Contract
→ Adaptation Matrix
→ Character / Subplot Compression
→ POV / Reveal / Timeline Redesign
→ Interior Externalization
→ Screen Causality Reconstruction
→ Medium Structure
→ Scene Map
→ Draft
→ Adaptation Integrity Review
→ Rewrite
~~~

## 5.1 长篇读取规则

长篇、多卷、多文件必须先读到足以确认：

- 主线因果
- 主要人物功能
- 结局
- 核心秘密与揭露顺序
- 关键 Setup / Payoff
- 后文是否重解释前文
- 核心情绪承诺

在这些条件未满足前，不要把前几章当整部作品改编。

## 5.2 改编决策

重要源元素使用：

- KEEP
- TRANSFORM
- MERGE
- MOVE
- CUT
- INVENT

每个决定都必须回答：

- 原作功能是什么？
- 情绪价值是什么？
- 删除或移动会破坏什么？
- 新影视版本承担什么功能？
- 是否改变核心 IP 识别度？

## 5.3 内心戏外化优先级

优先转换成：

1. 选择
2. 行为
3. 关系策略
4. 道具
5. 空间关系
6. 信息控制
7. 对照动作
8. 可听声音
9. 必要且有形式价值的旁白

禁止把大量心理描写简单搬成旁白。

---

# 6. Story Contract

正式结构开发前尽量锁定：

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

如果 Story Contract 不能成立，先修故事发动机，不要靠漂亮场景或对白掩盖。

---

# 7. 人物与关系

主要人物至少维护：

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

人物不是履历。

必须能回答：

> 他现在想从谁那里得到什么？为什么得不到？他会先用什么策略？失败后如何换策略？他愿意付到什么代价？

关系必须维护：

- 权力
- 依赖
- 债务
- 信任
- 秘密
- 亲密风险
- 资源控制
- 当前未解决冲突

---

# 8. 结构不是节点填表

允许三幕、四幕、五幕、Sequence、七点、英雄旅程、Save the Cat 或自定义结构。

任何框架都只能用于诊断。

优先检查：

1. 原平衡如何被破坏？
2. 主角何时主动承诺进入主线？
3. 对手如何根据主角行为升级？
4. 中段改变了什么：目标、规则、信息、权力还是意义？
5. 低谷是否来自此前选择？
6. 高潮是否迫使主角在高代价下做价值选择？
7. 结局是否用行为证明改变或拒绝改变？

---

# 9. Scene Engine

每场先有内部 Scene Contract：

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

最小戏剧逻辑：

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

一场戏如果没有信息、关系、权力、目标、风险、认知或资源的有效变化，默认视为可疑场景。

---

# 10. 对白

对白首先是行动，不是信息搬运。

每句重要台词必须能回答：

- 说话者想让对方做什么？
- 想让对方相信什么？
- 想迫使对方承认什么？
- 想隐藏什么？
- 想避免什么？
- 这句话为什么现在说？

主要人物维护 Voice Fingerprint：

- 句长
- 词汇
- 正式度
- 直接性
- 幽默
- 回避方式
- 愤怒方式
- 亲密方式
- 撒谎方式
- 职业语言
- 禁忌话题

优先使用潜台词、打断、回避、改口、沉默、策略变化，而不是让角色互相解释双方已经知道的信息。

---

# 11. 媒介路由

## Feature

重点：

- 单一强主线
- Sequence 级升级
- 中段重定义
- 有限时长内完整人物弧
- 高潮汇合外部目标、关系与主题

读取 workflows/feature-film.md。

## Episodic Series

重点：

- Series Engine
- Season Question
- Episode Function
- A/B/C Lines
- 关系长期演化
- 每集阶段兑现
- Story Bible 与 Knowledge State

读取 workflows/episodic-series.md。

## Short Drama

重点：

- 快速进入具体处境
- 单集微型戏剧单元
- 单位时间有效变化密度
- 小兑现制造新后果
- 连载驱动力来自未完成问题与关系，而非机械反转

读取 workflows/short-drama.md。

若用户明确要求当前海外市场、目标国家、平台趋势或本地化，再调用对应专项 Skill/实时资料。

## Animation

动画允许更强视觉表达，但仍服从人物、因果、可执行动作与制作规模。

---

# 12. Script Doctor 与重写

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

修订顺序遵循“上游优先”。

不要用对白润色掩盖 Story Engine、Agency 或 Causality 的问题。

---

# 13. 剧本正文标准

默认使用 Master Scene 思路。

正文主要元素：

- Scene Heading
- Action
- Character
- Dialogue
- Parenthetical（必要时）
- Transition（必要时）

Submission / Development Draft 默认：

- 不写场号
- 不堆摄影机指令
- 不写焦段
- 不写推拉摇移
- 不写灯光参数
- 不混入生图/视频提示词

动作行只写观众可见、可听、可演的信息。

行业格式细节读取 references/screenplay-format.md。

---

# 14. 用户交互原则

1. 用户要求“直接做完”时，不逐阶段索要确认。
2. 非根本性信息缺失，用 ASSUMED 标记并继续。
3. 只有缺失会使结果完全改变时才需要澄清。
4. 不把内部分析流程全部倾倒给用户。
5. 用户要完整剧本时，最终必须进入场景正文和完整对白。
6. 用户只要某一场时，不强迫先看完整大纲。
7. 用户给出锁定要求时，不在后续重写中悄悄改掉。
8. 长项目每完成一个单元都更新状态，再继续下一个单元。

---

# 15. 输出契约

## 用户要“开发项目”

可交付：

- Project Contract
- Story Contract
- Character/Relationship Design
- Structure / Episode Map
- Scene Map
- 风险与待定项

## 用户要“写剧本”

最终交付必须包含：

- 场景标题
- 可见动作
- 人物行为
- 角色名
- 完整对白
- 场景转折
- 后果

## 用户要“小说改剧本”

默认交付：

~~~text
必要的改编定位
→ 核心改编决策
→ 影视版结构
→ 剧本正文
~~~

不要把 Source Index 当最终成品。

## 用户要“诊断”

输出：

- 症状
- 证据
- 根因
- 严重度
- 修复顺序
- 具体改法

---

# 16. Level 2 知识使用规则

当遇到以下情况时加载对应 Level 2：

- 结构反复修不好
- 人物看起来“对”但不活
- 场景没有戏
- 对白同质化
- 悬疑/信息释放混乱
- 长剧集后半段失速
- 短剧只剩机械反转
- 改编既不忠实也不好看
- Script Doctor 需要根因级分析

入口：

- references/knowledge-map-level2.md

Level 2 每个知识点都包含：

- 定义
- 作用机制
- 诊断问题
- 常见失败
- 修复动作

---

# 17. 禁止性失败模式

禁止：

- 把小说分析当剧本
- 一章等于一集
- 用旁白承包内心戏
- 主角被剧情拖着走
- 对手只在需要时突然出现
- 中段重复前段
- 高潮靠偶然解决
- 场景只有信息没有争夺
- 所有人说话像同一个作者
- 用固定页码/分钟数强制节点
- 用“每 N 秒反转”替代因果
- 长项目不维护 Story Bible
- 用户要求正文却只给大纲
- 无要求混入分镜、镜头和生成提示词

---

# 18. 完成标准

~~~text
□ 路由正确：原创 / 改编 / 重写 / 单场
□ 目标媒介明确
□ 长篇素材已先完成全局读取与索引
□ Story Contract 成立
□ 主角有可执行目标并持续选择
□ 对抗力量会适应和反制
□ Stakes 具体并升级
□ 重大剧情有因果
□ 中段产生实质改变
□ 高潮来自人物高代价选择
□ 人物弧有行为证据
□ 核心关系发生真实变化
□ 每场有目标、阻力、策略、转折和后果
□ 对白具有行动与潜台词
□ 主要人物声音可区分
□ 心理已尽量外化
□ 信息差、秘密和知识状态清楚
□ Setup / Payoff 可追踪
□ 长项目连续性稳定
□ 正文可见、可听、可演
□ 格式清楚且不过度导演化
□ 至少完成一轮结构性诊断
□ 用户要求剧本时已经真正进入剧本正文
~~~
