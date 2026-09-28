# 原创剧本引擎：概念 → 完整剧本

本文件用于没有完整原作时，从概念、人物、冲突、主题或一句话想法发展成完整剧本。

---

# 1. 从 Concept 到 Premise

Concept 可以很小：

- 一个职业 + 一个异常
- 一段关系 + 一个秘密
- 一个规则 + 一个破例
- 一个角色 + 一个不可能任务

但 Concept 不是 Story。

必须发展成：

```yaml
premise:
  protagonist:
  normal_state:
  inciting_event:
  external_goal:
  opposing_force:
  stakes:
  dramatic_question:
```

---

# 2. Logline

最低包含：

```text
谁
+
因为发生了什么
+
必须完成什么
+
面对什么阻碍
+
失败会失去什么
```

不要把 Logline 写成世界观简介。

---

# 3. Theme Question

把主题写成可冲突问题。

差：

> 真爱可以战胜一切。

更好：

> 当爱要求你牺牲尊严时，留下还是离开？

建立：

```yaml
theme:
  question:
  thesis_value:
  antithesis_value:
  protagonist_starting_belief:
  final_choice:
```

主题靠后果表达，不靠演讲。

---

# 4. 主角设计

```yaml
protagonist:
  external_goal:
  internal_need:
  misbelief:
  fear:
  wound:
  strength:
  flaw:
  contradiction:
  leverage:
  secret:
  start_state:
  irreversible_choice:
  ending_state:
```

主角必须能行动。

如果主角只能被动受苦：

- 给他可争取的目标
- 给他资源
- 给他可失败的选择
- 让他的策略制造后果

---

# 5. 对抗力量

对手不等于“坏人”。

```yaml
opposition:
  goal:
  why_it_conflicts:
  resources:
  leverage:
  adaptive_strategy:
  moral_logic:
  blind_spot:
  escalation_path:
```

强对手会根据主角行为换招。

---

# 6. Stakes

具体化：

- 会失去谁？
- 会失去什么身份？
- 会失去什么资源？
- 会承受什么法律 / 社会 / 道德代价？
- 关系会怎样不可逆？
- 主角会成为什么样的人？

代价升级不能只是“更危险”。

---

# 7. 核心关系

```yaml
core_relationship:
  character_a_wants:
  character_b_wants:
  mutual_need:
  mutual_threat:
  attraction_or_dependency:
  power_balance:
  shared_history:
  hidden_truth:
  rupture_point:
  final_state:
```

好的关系能自己产生戏。

---

# 8. Story Engine

问：

```text
为什么这个故事不会在 20 分钟内自然结束？
主角每次行动会制造什么新问题？
对手如何适应？
秘密如何分层揭露？
关系为什么会继续变化？
```

如果唯一发动机是“一个误会还没说开”，发动机太弱。

---

# 9. Ending-first

复杂项目优先先回答：

- 最终外部问题如何解决？
- 核心关系最终是什么状态？
- 主角最后必须做什么选择？
- 这个选择怎样证明 Arc？
- 观众最后看到的画面是什么？

然后反推：

```text
高潮需要什么能力 / 证据 / 关系？
↓
这些东西何时建立？
↓
哪些 Setup 必须更早出现？
```

---

# 10. Story Spine

```text
旧平衡
→ 异常变量
→ 主角回应
→ 第一次重大选择
→ 新局面
→ 对抗升级
→ 中段意义改变
→ 代价积累
→ 最严重失败
→ 最终策略
→ 高潮选择
→ 新平衡
```

结构节点必须来自因果。

---

# 11. Beat Sheet

每个 Beat 写成具体事件：

```yaml
beat:
  trigger:
  action:
  obstacle:
  result:
  state_change:
  setup_or_payoff:
  next_pressure:
```

禁止抽象占位：

- 主角遇到困难
- 两人关系升温
- 反派制造麻烦

必须写“发生什么”。

---

# 12. Scene List

把 Beat 转成可写场景：

```yaml
scene:
  id:
  location_time:
  participants:
  goal:
  obstacle:
  tactic:
  counter_tactic:
  turn:
  value_shift:
  consequence:
```

如果一个 Beat 无法转成可见场景，继续细化。

---

# 13. 信息设计

原创也必须维护：

- 观众知道什么
- 主角知道什么
- 对手知道什么
- 哪些误信在工作
- 哪些秘密等待揭开
- Reveal 后改变什么

悬念不是无限隐藏答案。

---

# 14. 类型模块

## 爱情

核心：吸引 + 阻碍 + 选择 + 代价 + 关系变化。

## 悬疑

核心：问题链 + 线索 + 假设更新 + 公平证据 + Reveal 后果。

## 惊悚

核心：威胁 + 限制 + 时间压力 + 策略 + 风险升级。

## 喜剧

核心：人物目标 + 错误策略 + 处境升级 + 角色逻辑。

## 高爽 / 复仇

核心：情绪债务 + 主动性 + 阶段回报 + 对手适应 + 新代价。

## 人物剧 / 慢燃

核心：事件可少，但关系、认知和选择不能静止。

---

# 15. 初稿纪律

第一遍：

- 保证完整
- 保证因果
- 保证角色目标
- 保证场景变化
- 保证结局

不要第一场就反复抛光。

第二遍再做：

- Scene Pass
- Dialogue Pass
- Continuity Pass
- Theme Pass
- Compression Pass

---

# 16. 原创项目质量检查

```text
□ Concept 已发展成 Premise
□ 主角目标具体
□ 主角有主动选择
□ 对抗力量会适应
□ Stakes 可感知
□ 核心关系能产生持续戏剧
□ 中段改变故事玩法或意义
□ 低谷来自选择后果
□ 高潮依赖前文积累
□ 结局回答戏剧问题
□ 主题通过行动表达
□ 场景可以直接写成可演内容
```
