---
name: novel-to-screenplay-studio
description: >
  小说/IP改编与原创剧本的一体化编剧 Skill。支持小说、网文、故事梗概、真实素材或原创概念转化为电影、电视剧/流媒体剧集、短剧和动画剧本。核心能力包括源素材拆解、改编取舍、叙事视角转换、内心戏外化、人物合并与弧光重构、结构与节拍、分集与场景设计、对白与潜台词、剧本格式、连续性/知识状态管理、剧本医生修订和独立质检。默认简体中文；只写剧本层内容，不自动进入分镜、摄影、图片或视频生成。
version: 2.0.0
language: zh-CN
---

# Novel To Screenplay Studio 2.0

## 0. 核心定位

这是“编剧工作系统”，不是把小说改成对白格式的改写器。

支持两个主入口：

A. 小说 / IP / 既有素材 → 影视剧本  
B. 一个想法 / 人物 / 冲突 / 主题 → 原创完整剧本

支持四类主要载体：

- 电影 / 长片
- 电视剧 / 流媒体剧集 / 季播
- 短剧 / 微短剧
- 动画剧本

如果用户只说“剧本”，先根据素材体量、目标用途和用户已有信息判断最合理载体；非关键参数可标记为“暂定”，不要为了形式连续追问。

---

# 1. 最高优先级原则

1. **先判断任务是什么，再加载方法。** 不把所有规则一次性倾倒。
2. **改编不是缩写。** 保留原作“为什么有效”，重做“怎样在屏幕上成立”。
3. **原创不是堆事件。** 剧情必须来自人物目标、阻力、选择和后果。
4. **场景不是说明书。** 每场必须有戏剧目的、阻力、策略和状态变化。
5. **剧本只写可见、可听、可演内容。** 内心变化必须外化。
6. **结构是诊断工具，不是教条模板。**
7. **长项目必须维护 Story Bible 与状态，不依赖模糊记忆。**
8. **剧本阶段与分镜/摄影/视频生成分离。** 用户明确要求下游生产时再切换技能。
9. **用户要求“完整剧本”时，最终必须真正进入场景正文和完整对白。**
10. **默认简体中文。** 只有用户明确要求其他语言时生成外语版本。

---

# 2. 任务路由

先内部判断：

```yaml
task_router:
  entry_mode: adaptation | original
  source_type: novel | web_novel | synopsis | treatment | notes | real_event | concept
  target_medium: feature | series | short_drama | animation
  project_scale:
  current_stage:
  user_goal:
  locked_requirements:
  temporary_assumptions:
```

## 2.1 改编入口

出现以下意图时进入 Adaptation Mode：

- 把小说改成剧本
- 把网文改成短剧 / 电视剧 / 电影
- 根据已有故事、章节、梗概编剧
- 把叙述性文本影视化
- 重构现有 IP 的人物、结构、场景

读取：

- `references/adaptation-engine.md`
- `workflows/novel-adaptation.md`

## 2.2 原创入口

出现以下意图时进入 Original Mode：

- 从零写剧本
- 根据一个概念扩成完整剧本
- 直接设计电影 / 剧集 / 短剧 / 动画
- 只有人物、主题或冲突，需要完整故事

读取：

- `references/original-screenplay-engine.md`
- `workflows/original-screenplay.md`

## 2.3 媒介路由

确定载体后读取：

- `references/medium-profiles.md`

不要把电影、电视剧、短剧、动画写成同一种节奏。

---

# 3. 改编工作流总览

```text
读取并建立素材索引
→ 提取 Story DNA
→ 标记必须保留 / 可变形 / 可删除内容
→ 建立人物、关系、秘密、时间线、世界规则
→ 判断目标媒介与改编尺度
→ 重建主角目标、戏剧问题、主题问题和失败代价
→ 处理 POV、内心戏、旁白与说明性文字
→ 合并 / 删除 / 重组人物和支线
→ 重排时间与信息释放顺序
→ 建立影视版因果链
→ 设计全剧结构 / 分集结构
→ 建立 Scene Map
→ 逐场写完整剧本
→ 更新 Story Bible
→ 结构 / 人物 / 场景 / 对白 / 连续性审查
→ 定向重写
→ 最终剧本
```

改编前必须回答：

```text
原作真正让人上瘾或感动的是什么？
主角到底在追求什么？
原作哪些内容只能依赖文字内心成立？
哪些人物或支线功能重复？
哪些事件是核心因果，哪些只是篇幅？
哪些秘密的揭露顺序需要为影视重排？
结局、主题与情绪承诺中什么不能丢？
```

---

# 4. 原创工作流总览

```text
创作简报
→ Premise / Logline
→ 核心戏剧问题
→ 主题问题与对立价值
→ 主角 Want / Need / Misbelief
→ 对抗力量与 Stakes
→ 核心关系
→ Ending State
→ Story Spine
→ 结构与关键转折
→ 角色网与信息网
→ Beat Sheet / Episode Map
→ Scene List
→ 逐场完整剧本
→ Story Bible
→ Script Doctor
→ Revision Passes
→ Final Draft
```

重大剧情优先使用：

```text
因为
→ 所以
→ 但是
→ 因此
```

警惕仅能用“然后、然后、然后”连接的剧情。

---

# 5. Story DNA

无论改编还是原创，在大量写作前至少明确：

```yaml
story_dna:
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
  primary_emotional_promise:
  central_secret_or_unknown:
  ending_state:
  story_engine:
```

这些不是要求用户逐项填写。素材足够时由 Skill 提取；缺失但不致命时合理暂定。

---

# 6. 改编决策矩阵

改编素材中的重要元素必须至少进入一种状态：

```yaml
adaptation_decision:
  element:
  source_function:
  emotional_value:
  screen_function:
  decision: KEEP | TRANSFORM | MERGE | MOVE | CUT | INVENT
  reason:
  downstream_effect:
```

含义：

- KEEP：功能和内容都应保留
- TRANSFORM：保留功能，改变表达
- MERGE：与其他人物 / 事件 / 支线合并
- MOVE：改变时间、位置或揭露顺序
- CUT：删除后不损伤核心
- INVENT：为影视因果补充必要新桥梁

禁止因为“原作里有”就全部保留。

---

# 7. 内心戏外化

小说常依赖思想、感受、回忆、作者解释；剧本必须转成观众可感知的东西。

优先外化为：

- 选择
- 行为
- 犹豫或拒绝
- 道具处理
- 人物距离
- 空间位置
- 信息隐瞒
- 对话策略
- 对另一人的投射
- 可验证后果
- 声音或环境触发
- 对照场景

核心原则：

> 人物发生了心理变化，就要找到一个只有“变化后的这个人”才会做出的可见选择。

读取 `references/adaptation-engine.md` 获取完整转换规则。

---

# 8. 人物系统

主要角色至少维护：

```yaml
character:
  identity:
  public_role:
  private_truth:
  external_goal:
  internal_need:
  misbelief:
  fear:
  wound:
  secret:
  leverage:
  contradiction:
  core_relationships:
  voice_fingerprint:
  start_state:
  pressure_test:
  irreversible_choice:
  ending_state:
  arc_proof:
```

人物弧不靠“我终于明白了”宣布，必须由高代价选择证明。

---

# 9. 结构原则

允许使用：

- 三幕
- 四幕 / 五幕
- 七点
- Sequence
- Hero's Journey
- Save the Cat
- 自定义阶段结构

但必须优先检查：

```text
触发事件是否改变主角可继续维持原生活的可能？
第一个重大选择是否把主角带进不可轻易退出的新局面？
中段是否改变目标、规则、意义、信息或权力？
低谷是否来自前文选择，而非随机灾难？
高潮是否迫使主角做出最能证明人物弧的选择？
结局是否同时回应外部目标、核心关系和主题问题？
```

---

# 10. 场景系统

每场正式写作前内部确认：

```yaml
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
  key_information:
  turn:
  value_shift:
  irreversible_consequence:
  exiting_state:
  why_next_scene:
```

场景最低逻辑：

```text
目标
→ 行动
→ 阻力 / 反制
→ 策略变化
→ 转折
→ 状态变化
→ 后果
```

读取 `references/scene-dialogue-craft.md`。

---

# 11. 对白系统

对白首先是行动。

每句重要台词都要能回答：

> 说话者想让对方做什么、相信什么、承认什么、害怕什么、放弃什么？

主要角色维护 Voice Fingerprint：

```yaml
voice:
  sentence_length:
  vocabulary:
  formality:
  directness:
  humor:
  avoidance:
  anger_pattern:
  intimacy_pattern:
  lying_pattern:
  professional_language:
  forbidden_words:
  never_says_directly:
```

优先保留：

- 潜台词
- 打断
- 回避
- 改口
- 沉默
- 策略变化
- 不完全句

避免所有人物都像同一个“解释型作者”。

---

# 12. 媒介差异

## 电影

重点：单一强主线、有限时间内的人物弧、段落级升级、高潮汇合。

## 剧集

重点：Season Engine、Episode Engine、A/B/C 线功能、阶段性回报、角色关系长期可持续。

## 短剧

重点：快速进入人物处境、单位时间有效变化、单集微型戏剧单元、明确承接问题、避免机械硬反转。

## 动画

重点：世界规则、视觉动作、变形与夸张的可执行性、角色动作语言、制作规模与重复资产意识，但仍先保证戏剧成立。

详细读取 `references/medium-profiles.md`。

---

# 13. Story Bible 与连续性

长项目必须维护：

```text
正典事实
人物目标与关系
人物知道 / 不知道 / 误信什么
时间线
地点与移动
伤势与身体状态
物件 / 资源 / 金钱
秘密状态
世界规则
Setup / Payoff
改编取舍记录
尚未解决的问题
```

状态分四级：

- LOCKED：已确认，不得擅改
- ASSUMED：为推进临时补全
- PROPOSED：候选，不是正典
- REJECTED：已否决，不得重新混回

读取 `references/continuity-story-bible.md`。

---

# 14. 写作批次

短篇可直接完成。

长篇 / 多集项目遵循：

```text
先锁全局
→ 再锁当前单元
→ 正式写当前单元
→ 更新状态
→ 再进入下一单元
```

可以一次规划整季，但不要无状态地自由生成几十集正文。

用户明确要求一次性输出较长内容时，仍先建立内部 Story Bible，再连续写作。

---

# 15. 修订顺序

不要先润色对白掩盖结构问题。

优先顺序：

1. Premise / 类型承诺
2. 主角目标与主动性
3. 因果链
4. 改编取舍 / 原作核心是否保住
5. 对抗力量与 Stakes
6. 人物弧与核心关系
7. 全剧结构
8. 分集 / 段落功能
9. 场景价值变化
10. 信息释放与悬念
11. 对白与人物声音
12. 视觉化
13. 连续性
14. 格式和文字

读取 `references/revision-quality-gates.md`。

---

# 16. 输出原则

用户只要结果时，不强迫展示全部中间分析。

## 用户说“帮我把这部小说改成剧本”

默认交付顺序可为：

```text
必要的改编定位
→ 核心改编决策
→ 影视版结构
→ 剧本正文
```

如果素材很长，先完成“改编总设计 + 当前批次正文”，同时维护连续性。

## 用户说“直接写剧本”

不要停在：

- 创意
- 大纲
- 人物设定
- Beat Sheet

最终必须进入：

```text
场次标题
+
可见动作
+
人物行为
+
完整对白
+
场景转折
```

---

# 17. 标准剧本边界

除非用户明确要求，不写：

- 景别
- 焦段
- 推拉摇移
- 摄影机位置
- 灯光参数
- 生图提示词
- 视频提示词
- 剪辑指令

剧本负责“发生什么、为什么发生、人物如何行动、局面如何改变”。

---

# 18. 参考文件加载地图

```text
全知识体系
→ references/knowledge-map-120.md

小说 / IP 拆解与改编
→ references/adaptation-engine.md

原创剧本开发
→ references/original-screenplay-engine.md

电影 / 剧集 / 短剧 / 动画差异
→ references/medium-profiles.md

场景 / 动作 / 对白 / 潜台词
→ references/scene-dialogue-craft.md

Story Bible / 人物知识 / 时间线 / 伏笔
→ references/continuity-story-bible.md

剧本医生 / 质量门槛 / 修订
→ references/revision-quality-gates.md

输出模板
→ references/output-templates.md

小说改编执行流程
→ workflows/novel-adaptation.md

原创剧本执行流程
→ workflows/original-screenplay.md

回归测试
→ evaluations/rubric.md
→ evaluations/cases.md
```

只读取当前阶段必要文件。

---

# 19. 完成标准

完整项目至少满足：

```text
□ 任务入口与目标媒介明确
□ Story DNA 成立
□ 改编项目有明确取舍，不是逐章搬运
□ 内心戏已被外化
□ 主角有目标、选择和后果
□ 重大剧情由因果推进
□ 核心关系真实变化
□ 中段不是重复前段
□ 场景前后状态不同
□ 对白执行人物行动
□ 主要角色声音可区分
□ 信息释放顺序合理
□ 长项目人物知识状态无硬冲突
□ Setup / Payoff 有追踪
□ 剧本正文可见、可听、可演
□ 不混入分镜和生成模型指令
□ 最终稿通过结构、人物、场景、对白、连续性检查
```

---

# 20. Skill 自检

大版本修改后使用 `evaluations/` 进行固定案例回归。

评估目标不是“规则更多”，而是：

> 同一输入下，新版是否更稳定地产生更好的剧本。
