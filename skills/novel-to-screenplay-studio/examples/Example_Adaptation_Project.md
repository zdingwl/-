# Example Project：长篇小说 → 8 集 Limited Series

## 用户输入

```text
我有一部长篇家庭悬疑小说。
双时间线，12 个主要人物。
核心是母女关系和二十年前的一桩失踪案。

改成 8 集流媒体剧。
必须保留母女关系和最终真相，
其他角色与支线可以调整。
```

---

## Skill 应做的路由

```yaml
entry_mode: adaptation
source_type: novel
target_medium: series
project_scale: limited_series_8
adaptation_fidelity: functional
```

---

## Stage 1：Source Index

先抽取：

- 当前时间线
- 二十年前时间线
- 12 个角色的功能
- 母女关系关键节点
- 失踪案证据链
- 谁知道什么
- 关键物件
- 原作 Reveal 顺序
- 结局真相

---

## Stage 2：Story DNA

示意：

```yaml
protagonist: 成年女儿
external_goal: 查明母亲隐瞒的失踪案真相
internal_need: 停止把亲密关系等同于控制和欺骗
core_relationship: 女儿 / 母亲
dramatic_question: 她能否查明真相而不彻底毁掉与母亲的关系
primary_emotional_promise: 真相揭开与母女关系重构
ending_state: 真相公开，但两人以新的边界重新建立关系
```

---

## Stage 3：Adaptation Matrix

示例：

| 原作元素 | 决策 | 原因 |
|---|---|---|
| 母女主线 | KEEP | 核心情绪承诺 |
| 两位功能重复的警探 | MERGE | 减少角色数量 |
| 前 6 章童年回忆 | MOVE + TRANSFORM | 分散进入现在时冲突 |
| 一条远房亲属支线 | CUT | 不改变主线与主题 |
| 女儿大量第一人称内心 | TRANSFORM | 变成选择、调查动作与关系策略 |
| 后半部关键证据 | MOVE | 提前成为中段意义转折 |

---

## Stage 4：8 集结构

不按章节切。

示意：

```text
E1 失踪案重新被触发，女儿发现母亲撒谎
E2 调查进入家族旧关系
E3 一份旧证据改变“受害者是谁”的理解
E4 中段：女儿发现自己童年的记忆并不可靠
E5 母亲主动阻止调查，关系彻底破裂
E6 旧案与当前事件汇合
E7 真凶范围收窄，但母亲的真正动机曝光
E8 真相 / 高潮选择 / 母女关系新平衡
```

---

## Stage 5：Scene Contract

每一场不只是“交代线索”。

例如：

```yaml
scene_id: E1-S08
goal: 女儿逼母亲承认当年去过失踪现场
obstacle: 母亲只承认部分事实
tactic: 女儿先假装已经拿到监控资料
counter_tactic: 母亲反问证据来源，识破试探
turn: 母亲说出一个女儿从未知道的旧名字
value_shift: 女儿从占优势变成意识到自己知道得更少
consequence: 她决定私下寻找这个人
```

---

## 最终标准

完成后应同时满足：

- 原作核心仍然存在
- 8 集可以独立观看
- Reveal 顺序为影视重新设计
- 角色数量可管理
- 内心戏已外化
- Knowledge State 无冲突
- 每集都有自身变化
