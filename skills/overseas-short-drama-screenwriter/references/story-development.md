# 故事开发参考

用于：已经完成目标国家确认与最新市场研究，并选定创意之后；在正式逐集写剧本之前，建立能支撑完整短剧的故事结构、人物、关系、连续性和分集发动机。

本文件吸收多套成熟编剧 Skill 的共同优点，但不强迫故事服从某一种固定模板。核心原则是：**结构服务故事，人物选择制造剧情，场景必须产生变化。**

---

# 1. 先锁定故事脊柱

正式分集前必须锁定：

```yaml
foundation:
  logline:
  dramatic_question:
  theme_question:
  protagonist_external_goal:
  protagonist_internal_need:
  central_opposing_force:
  stakes:
  primary_emotional_promise:
  ending_state:
```

如果这些内容仍然模糊，不要急着写几十集分集大纲。

## 1.1 Logline 最低要求

至少包含：

```text
谁
+
发生了什么触发事件
+
必须完成什么目标
+
主要阻碍是什么
+
失败会失去什么
```

## 1.2 主题不是口号

不要写：

> 爱能战胜一切。

更适合写成一个贯穿故事的冲突问题：

> 当爱情与尊严冲突时，一个人应该牺牲哪一个？

再建立与主题相反的力量：

```text
主题命题
vs.
反命题 / 对立价值
```

最终通过人物选择和后果表达主题，不靠角色发表大道理。

---

# 2. 因果链优先于事件数量

故事必须能够写成：

```text
因为 A 发生
→ 主角选择 B
→ B 造成 C
→ 但是 C 引发 D
→ 主角被迫改变策略 E
→ E 又造成新的后果 F
```

警惕：

```text
然后发生 A
然后发生 B
然后突然发生 C
```

如果大量剧情只能用“然后”连接，而不能用“因为 / 所以 / 但是 / 因此”连接，说明结构缺乏因果。

## 因果审查

每个重大剧情点都问：

1. 为什么现在发生？
2. 是谁的行动造成？
3. 前面有什么铺垫让它成为可能？
4. 主角此刻知道什么、不知道什么？
5. 为什么主角会做这个选择？
6. 有没有更简单的解决办法？
7. 如果有，为什么人物不能使用？
8. 这个结果又制造了什么新压力？

如果只能回答“因为剧情需要”，重做。

---

# 3. 不固定套一种结构模板

可以参考：

- 三幕结构
- 四幕 / 五幕 / 六幕电视结构
- Save the Cat
- Hero's Journey
- 七点结构
- 自定义阶段结构

但它们只是诊断工具，不是硬模板。

对海外竖屏短剧，优先使用“全剧宏观阶段 + 单集微型戏剧单元”，而不是强行把电影 15 Beat 按比例切成几十集。

## 推荐的全剧宏观阶段

```text
1. 破局 / 异常发生
2. 被迫进入新关系或新局势
3. 第一轮行动与受挫
4. 第一次有效兑现
5. 更深秘密 / 更强对手出现
6. 关系或身份发生重大变化
7. 中段大反转
8. 暂时胜利
9. 重大损失
10. 主角改变打法并反击
11. 多条矛盾汇合
12. 最终选择
13. 高潮
14. 情绪与关系兑现
```

不要求每个项目恰好 14 段，但必须能看见压力不断改变，而不是原地重复。

---

# 4. 人物不是履历，而是行动系统

主要人物建立：

```yaml
character:
  name:
  age:
  nationality:
  city:
  profession:
  socioeconomic_position:
  public_identity:
  hidden_identity:
  external_goal:
  internal_need:
  false_belief:
  fear:
  wound:
  flaw:
  strength:
  secret:
  leverage:
  resources:
  limitations:
  line_they_will_not_cross:
  opening_state:
  breaking_point:
  final_choice:
  ending_state:
  arc:
```

## 4.1 Want 与 Need

`Want`：人物自己知道、会主动追求的东西。

`Need`：人物真正需要学会、承认或改变的东西。

二者最好存在张力。

## 4.2 压力下的人物

为核心人物提前定义：

```yaml
pressure_behavior:
  low_pressure:
  medium_pressure:
  high_pressure:
  breaking_point:
  strategy_change_trigger:
```

这样可以防止后期为了反转让角色突然降智或性格突变。

## 4.3 主角主动性测试

每 3–5 集检查：

- 主角做了什么主动决定？
- 这个决定造成了什么后果？
- 主角有没有因为失败改变策略？
- 主角是否只是不断被别人推动？

主角可以受害、被背叛、被羞辱，但不能长期只是等待别人救。

---

# 5. 对抗力量必须会适应

反派或主要阻力建立：

```yaml
opposition:
  goal:
  reason:
  moral_logic:
  resources:
  advantage_over_protagonist:
  vulnerability:
  escalation_strategy:
  strategy_if_exposed:
  final_pressure:
```

好的对手会根据主角行动改变策略。

不要出现：

```text
主角每次反击
→ 反派仍然用完全相同的办法
→ 再被打脸
→ 下一集继续重复
```

冲突必须升级层级或改变意义。

---

# 6. 关系发动机

核心关系不能只有“喜欢 / 不喜欢”。

建立：

```yaml
relationship:
  character_a:
  character_b:
  surface_relationship:
  hidden_truth:
  what_a_wants_from_b:
  what_b_wants_from_a:
  attraction_or_dependency:
  conflict_of_interest:
  unequal_information:
  unequal_power:
  shared_history:
  mutual_need:
  mutual_fear:
  trust_level_start:
  first_shift:
  breaking_point:
  repair_or_final_break:
  final_state:
```

关系必须经历可识别的状态变化，例如：

```text
陌生
→ 被迫合作
→ 产生吸引
→ 初步信任
→ 秘密造成裂痕
→ 权力倒置
→ 重大背叛
→ 真相揭露
→ 最终选择
```

禁止几十集只是“误会—和好—再误会”。

---

# 7. Series Engine：为什么第 3 集以后还能继续？

长短剧都必须回答：

> 如果核心误会现在就说清楚，故事还能不能继续？

稳定的系列发动机最好至少包含三层：

```text
关系发动机
+
外部目标发动机
+
秘密 / 信息发动机
```

还可以加入：

- 家族 / 商业竞争
- 法律或财务压力
- 复仇计划
- 生存目标
- 调查 / 悬疑
- 超自然规则
- 身份危机

如果一个诚实对话就能解决整部剧，发动机太弱。

---

# 8. A / B / C 故事线使用原则

海外短剧不需要机械模仿传统一小时美剧的 A/B/C 配比。

默认：

- **A 线**：主角核心关系或主要外部目标，必须占绝对主导。
- **B 线**：只有当它能给 A 线施压、制造对照或提供关键因果时才保留。
- **C 线 / Runner**：微短剧慎用，除非它能快速制造重复性期待或喜剧节奏。

判断标准：

> 删除 B/C 线后，A 线是否变得更弱、更扁或失去关键压力？

如果没有，删掉。

---

# 9. 分集结构

每集先建立 Episode Card：

```yaml
episode:
  number:
  opening_state:
  opening_hook:
  episode_goal:
  protagonist_goal:
  immediate_obstacle:
  key_action:
  escalation:
  reveal_or_reversal:
  emotional_payoff:
  relationship_shift:
  cliffhanger:
  ending_state:
  next_question:
```

竖屏短剧优先：

```text
HOOK
→ 目标
→ 阻力
→ 行动
→ 升级
→ 转折 / 小兑现
→ 后果
→ Cliffhanger
```

不是每集都必须完全同节奏，但每集都必须有**状态变化**。

---

# 10. Opening Hook 不是随机刺激

Hook 必须连接核心因果。

可以使用：

- 背叛正在发生
- 身份矛盾
- 关系破裂
- 公开羞辱
- 紧急危险
- 证据出现
- 不可能选择
- 婚姻 / 分手 / 求婚危机
- 地位反转
- 超自然异常
- 法律 / 财务压力

禁止为了抓眼球加入一件之后再也没用的“突然事件”。

第一集尤其必须尽快让观众明白：

```text
谁是主角
发生了什么
主角现在要什么
谁在阻止
为什么必须继续看
```

---

# 11. Cliffhanger 要改变下一集期待

可用类型：

- 危险已经启动
- 新身份信息
- 关系断裂
- 无法回避的选择
- 新证据
- 背叛被揭露
- 权力反转
- 意外人物出现
- 法律 / 财务后果
- 过去真相改变当前判断
- 超自然规则被打破
- 假胜利突然崩塌

弱：

> 一切才刚刚开始。

强：

> 她刚签完离婚协议，律师却把第二份结婚证推到她面前——上面的丈夫不是眼前这个男人。

好的 Cliffhanger 会产生一个明确问题，而不是只有情绪词。

---

# 12. Promise → Payoff → Bigger Question

短剧不能永远只拖。

周期性兑现：

- 主角第一次有效反击
- 某个谎言被证实
- 一段关系真正改变
- 反派失去筹码
- 身份秘密揭开一层
- 主角获得新资源
- 某个误判被推翻

推荐：

```text
承诺
→ 部分兑现
→ 产生后果
→ 更大的问题
```

---

# 13. Scene Contract：正式写场景前必须知道什么

每场至少明确：

```yaml
scene:
  id:
  location:
  time:
  characters:
  dramatic_question:
  protagonist_or_pov_goal:
  opposing_force:
  tactic:
  counter_tactic:
  reveal:
  turn:
  value_before:
  value_after:
  result:
  exit_question:
```

## 13.1 场景价值转折

场景前后至少有一种价值改变：

```text
信任 → 怀疑
安全 → 危险
优势 → 劣势
亲近 → 疏离
无知 → 知道
希望 → 绝望
猎人 → 猎物
```

如果场景结束后一切和开始时一样，优先删、合并或重写。

## 13.2 一场尽量承担两项以上任务

例如同时：

- 推剧情 + 改关系
- 给信息 + 制造新问题
- 回收伏笔 + 改变权力
- 展示人物 + 引出下一场行动

但不要为了“多功能”塞入无关信息。

---

# 14. Setup / Payoff 台账

```yaml
setup:
  id:
  planted_episode:
  planted_scene:
  visible_to_audience:
  known_by_characters:
  development_steps:
  intended_payoff:
  payoff_episode:
  status:
```

状态：

```text
PLANTED
DEVELOPING
PARTIALLY_PAID
PAID_OFF
ABANDONED_WITH_REASON
```

重大反转最好能回看前文找到证据。

---

# 15. Reveal Ladder：秘密不要只有开 / 关

重要秘密优先分层：

```text
第一层：出现异常
第二层：原有判断不成立
第三层：新的嫌疑对象出现
第四层：真正动机发生变化
第五层：主角发现自己也在因果链中
```

每次揭露必须至少改变：

- 认知
- 目标
- 策略
- 关系
- 风险

否则只是信息，不是戏剧转折。

---

# 16. 情绪曲线

不要一直最高强度。

推荐对比：

```text
压力
→ 短暂喘息
→ 亲密 / 希望
→ 新威胁
→ 小胜利
→ 更大代价
```

安静场也必须改变关系、信息或人物选择。

---

# 17. 长篇 / 多集生成规则

这是防止 AI 后半段失控的重要规则。

## 17.1 先锁整季，再逐集写

正确：

```text
完整故事线
→ 全集 Episode Map
→ 关键反转 / 伏笔 / 终局锁定
→ 第1集剧本
→ 更新连续性
→ 第2集剧本
→ 更新连续性
→ ……
```

不要：

```text
一句创意
→ 一次性自由生成 60 集正文
```

## 17.2 一次只正式写一集

长项目中，正式正文按一集一个写作单元处理。

如果两集连续性很强，必须串行写。

只有真正独立的单元集才允许并行构思，但最终仍要做统一连续性审查。

## 17.3 每集结束生成 Handoff State

```yaml
handoff_state:
  episode:
  story_time:
  character_locations:
  character_emotional_states:
  relationship_states:
  injuries_or_physical_state:
  possessions:
  new_information_by_character:
  secrets_revealed:
  setups_planted:
  setups_paid:
  unresolved_questions:
  antagonist_next_move:
```

下一集开始前必须读取上一集 Handoff State。

---

# 18. Story Bible 只保存“正典事实”

维护：

```text
世界规则
人物卡
人物关系
时间线
地点
关键物件
已公开秘密
未公开秘密
人物各自知道什么
伏笔 / 回收
伤势和身体状态
金钱 / 资源
法律 / 制度约束
当前剧情状态
```

禁止把临时 brainstorm 当成已确定正典。

区分：

```text
LOCKED = 用户或已确认剧情锁定
ASSUMED = 为了继续创作暂时补全
PROPOSED = 只是候选方案
```

后续不能把 `PROPOSED` 自动变成 `LOCKED`。

---

# 19. 结构诊断顺序

当故事不好看时，不要先修台词。

按顺序检查：

```text
1. Premise 是否有戏？
2. 主角目标与代价是否明确？
3. Story Engine 能否持续？
4. 因果链是否断裂？
5. 中段是否只是重复？
6. 关系是否真正变化？
7. 反转是否改变策略？
8. 单集是否有状态变化？
9. 场景是否有价值转折？
10. 最后才修对白和措辞。
```

结构问题不能靠更漂亮的对白解决。

---

# 20. 结局设计

结局至少兑现三层：

## 外部剧情

主角是否完成、失败或重新定义目标？

## 核心关系

这段关系最终是什么状态？为什么？

## 人物弧

主角最后做了什么选择，证明他已经改变或拒绝改变？

高潮最好来自：

```text
人物长期积累的选择
+
前面建立的能力 / 资源
+
前面埋下的 Setup
```

不要用最后一分钟突然出现的新人物、新证据或巧合解决核心矛盾。
