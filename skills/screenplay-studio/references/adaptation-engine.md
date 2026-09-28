# Adaptation Engine — 小说 / IP / 故事 → 影视剧本

改编不是压缩原文，而是把原作的功能、情绪、关系和因果重新编码成屏幕语言。

## 1. 先确定 Adaptation Contract

~~~yaml
adaptation_contract:
  source:
  target_medium:
  target_scope:
  fidelity: high | functional | free
  locked_characters:
  locked_relationships:
  locked_events:
  locked_ending:
  audience_promise:
  allowed_compression:
  allowed_invention:
  forbidden_changes:
~~~

忠实度不等于逐句保留。

- high：主要事件、核心人物、结局和识别度高度保留。
- functional：保留核心人物、情绪承诺、主题、主线因果与标志性关系；允许较大结构重排。
- free：保留少量核心 DNA，其余按目标媒介重建。

## 2. Story DNA

至少锁定：

~~~yaml
story_dna:
  protagonist:
  external_goal:
  internal_need:
  misbelief:
  inciting_event:
  dramatic_question:
  theme_question:
  core_relationship:
  opposing_force:
  stakes:
  primary_emotional_promise:
  central_secret:
  ending_state:
  signature_elements:
~~~

原作主线不清楚时，影视版必须建立更清楚的观众跟随线。

## 3. Adaptation Matrix

每个重要元素进入：

~~~yaml
adaptation_item:
  source_element:
  source_location:
  source_type:
  original_function:
  emotional_value:
  plot_dependency:
  recognizability:
  screenability:
  decision: KEEP | TRANSFORM | MERGE | MOVE | CUT | INVENT
  new_screen_function:
  affected_elements:
  risk:
~~~

### KEEP

只有高功能、高识别度或对后续因果不可替代时优先原样保留。

### TRANSFORM

保留功能，改变表达方式。

小说：
“她终于不再相信丈夫。”

影视：
她从共享账户中撤掉紧急联系人，然后把备用钥匙从钥匙圈上拆下来。

### MERGE

合并功能重复的：

- 消息传递者
- 相似竞争者
- 无独立弧配角
- 重复阻力事件
- 功能相同的地点

### MOVE

用于：

- 把更强的冲突提前
- 延后过早泄露的秘密
- 拆散回忆
- 让 Reveal 在更高代价时发生
- 调整观众知识与角色知识的先后

### CUT

删除前检查：

- 后续因果是否断裂？
- 人物动机是否消失？
- Setup 是否丢失？
- 核心关系是否变薄？
- 原作情绪承诺是否被损伤？

### INVENT

允许新增：

- 因果桥梁
- 决策场景
- 可见证据
- 必要对抗
- 屏幕动作
- 原作跳过但影视必须看到的后果

新增必须解决真实的影视问题。

## 4. 内心戏外化

优先顺序：

1. 选择
2. 行为
3. 策略变化
4. 道具
5. 空间距离
6. 信息控制
7. 对照动作
8. 第三对象
9. 声音
10. 有形式价值的旁白

判断标准：

> 观众如果听不到角色的思想，还能否从行为和后果知道他发生了变化？

## 5. POV 重建

~~~yaml
pov_map:
  sequence:
  audience_follows:
  audience_knows:
  protagonist_knows:
  antagonist_knows:
  intentionally_withheld:
  false_beliefs:
  dramatic_effect:
~~~

常用策略：

- 主观跟随：观众与主角基本同步。
- 优越信息：观众先知道危险，制造 suspense。
- 分裂信息：不同人物掌握不同碎片。

不要沿用小说 POV 只是因为原作这样写。

## 6. Reveal Ledger

~~~yaml
reveal:
  information:
  source_location:
  audience_learns:
  protagonist_learns:
  other_characters_learn:
  before_reveal_belief:
  after_reveal_change:
  consequence:
~~~

强 Reveal 必须改变至少一项：

- 目标
- 关系
- 策略
- 风险
- 权力
- 身份
- 对过去的解释

## 7. 时间线重构

重排信息时问：

- 现在给，观众会形成什么判断？
- 晚给，是悬疑还是困惑？
- 早给，是期待还是泄气？
- 它会改变谁的策略？
- 它是否让前文出现新的意义？

不要仅因“原作第 X 章才讲”而保留原位置。

## 8. 人物压缩

先记录功能：

~~~yaml
character_function:
  name:
  plot_function:
  conflict_function:
  information_function:
  emotional_function:
  theme_function:
  unique_relationship:
  arc_value:
~~~

可以合并：

- 功能重复
- 关系重复
- 只承担一次性任务
- 无独立后果

谨慎合并：

- 不同主题立场
- 不同社会力量
- 对主角产生完全不同的情感影响
- 后期分别承担关键因果

## 9. 支线压缩

一条支线至少应贡献多个价值：

- 主线
- 关系
- 人物弧
- 主题
- 秘密
- 资源
- 对抗
- Setup / Payoff
- 节奏
- 世界规则

如果只贡献“更多内容”，优先删、并或转化。

## 10. 章节不等于影视单元

禁止：

~~~text
第 1 章 = 第 1 集
第 2 章 = 第 2 集
~~~

正确顺序：

~~~text
完整因果
→ 大阶段
→ 不可逆节点
→ Sequence / Episode Function
→ Scene Boundaries
~~~

章节结束是阅读节奏；影视单元结束必须体现戏剧状态变化。

## 11. 标志性元素保护

识别：

- 标志性场景
- 标志性物件
- 核心关系
- 独特世界规则
- 关键台词概念
- 结局意象
- 粉丝识别度高的节点

不要为了套工业模板把作品磨成同一种形状。

## 12. 新增场景准入

新增场景必须回答：

- 修复哪个屏幕问题？
- 让哪条因果成立？
- 替代哪段不可影视化内容？
- 改变什么状态？
- 删除后会损失什么？

答不出来就不要新增。

## 13. Adapted Scene Map

~~~yaml
adapted_scene:
  id:
  source_origin:
  source_elements_used:
  purpose:
  character_goal:
  obstacle:
  tactic:
  turn:
  visible_externalization:
  reveal:
  relationship_change:
  consequence:
  adaptation_decision:
~~~

确保每场都能追溯“为什么存在”。

## 14. 改编完整性检查

~~~text
□ 原作核心情绪承诺仍在
□ 核心人物关系未被误删
□ 标志性元素得到保护
□ 影视版主角目标更清楚
□ 内心戏已外化
□ 人物与支线经过功能审查
□ 章节未机械对应集数/场次
□ POV 与 Reveal 重新设计
□ 新增内容解决真实影视问题
□ 删除内容未破坏后续因果
□ 高潮仍回应核心价值问题
□ 不读原作也能独立理解影视版
□ 改编后仍能认出这是同一个作品
~~~
