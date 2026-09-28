# Story Bible、连续性与长篇状态管理

长篇项目的核心问题不是“会不会写”，而是“能否持续保持同一部作品”。

---

# 1. 正典层级

```text
LOCKED   已确认正典
ASSUMED  为推进暂定
PROPOSED 候选方案
REJECTED 已否决
```

PROPOSED 不得自动进入正文。

REJECTED 不得在后续重新出现。

---

# 2. Project State

```yaml
project_state:
  title:
  entry_mode:
  target_medium:
  current_stage:
  current_unit:
  draft_version:
  locked_decisions:
  assumptions:
  proposals:
  rejected:
  next_action:
```

状态只保存结论，不保存长篇推理。

---

# 3. Character Bible

```yaml
character:
  canonical_name:
  aliases:
  age:
  identity:
  occupation:
  external_goal:
  internal_need:
  misbelief:
  core_relationships:
  secrets:
  resources:
  injuries:
  current_location:
  current_status:
  voice_fingerprint:
  arc_state:
```

---

# 4. Knowledge State

这是长篇最重要的表之一。

```yaml
knowledge_state:
  character:
  knows:
  does_not_know:
  falsely_believes:
  suspects:
  learned_this_unit:
```

原则：

> 角色只能根据自己当时能知道的信息行动。

---

# 5. Secret Ledger

```yaml
secret:
  content:
  holders:
  suspects:
  audience_knows:
  protagonist_knows:
  public_status:
  reveal_plan:
  reveal_consequence:
```

揭开后必须更新状态。

---

# 6. Timeline

记录：

- 日期
- 星期（必要时）
- 时间跨度
- 旅行时间
- 伤势恢复
- 医疗过程
- 法律程序
- 怀孕 / 年龄
- 学期 / 工作周期
- 节日 / 季节

不要只记“过了几天”。

---

# 7. Location State

```yaml
location_state:
  character:
  current_location:
  arrived_at:
  can_reach_next_location_by:
  travel_constraint:
```

避免瞬移。

---

# 8. Object Ledger

关键物件：

```yaml
object:
  name:
  owner:
  holder:
  last_seen:
  condition:
  information_carried:
  setup:
  payoff:
```

尤其：

- 证据
- 手机
- 钥匙
- 文件
- 武器
- 药
- 钱
- 首饰
- 数据设备

---

# 9. Resource State

跟踪：

- 钱
- 股权
- 权限
- 职位
- 账户
- 交通
- 住所
- 人脉
- 法律身份
- 公开声誉

资源变化要产生后果。

---

# 10. Relationship State

```yaml
relationship:
  a:
  b:
  public_relation:
  private_relation:
  trust:
  power_balance:
  dependency:
  unresolved_conflict:
  last_change:
```

不要用“感情升温”这种模糊状态。

---

# 11. Setup / Payoff Ledger

```yaml
setup:
  item:
  planted_at:
  audience_notice_level:
  intended_payoff:
  payoff_target:
  status: open | paid | abandoned
```

若 abandoned，必须确认不会形成假承诺。

---

# 12. Adaptation Ledger

改编项目额外维护：

```yaml
adaptation_ledger:
  source_element:
  decision:
  replacement:
  new_location:
  downstream_changes:
  status:
```

避免被删除的角色或事件重新混回。

---

# 13. Decision Log

只记录重大变更：

```yaml
decision:
  date:
  item:
  old:
  new:
  reason:
  affected_units:
  required_repairs:
```

重大变更包括：

- 核心身份
- 结局
- 关键秘密
- 人物死亡
- 关系终局
- 世界规则
- 集数
- 时间线
- 关键证据

---

# 14. Handoff State

每个正式单元完成后：

```yaml
handoff:
  unit:
  story_time:
  character_locations:
  current_goals:
  relationship_changes:
  injuries:
  objects:
  resources:
  knowledge_changes:
  secrets_revealed:
  setups_planted:
  payoffs_completed:
  unresolved_questions:
  antagonist_next_move:
  next_unit_must_address:
```

---

# 15. 修改回溯

改一个大设定后：

```text
找受影响人物
→ 找受影响集 / 场
→ 找知识状态
→ 找 Setup / Payoff
→ 找结局影响
→ 更新正典
```

不要只改当前场。

---

# 16. 状态恢复

继续项目时优先读取：

1. 当前阶段
2. LOCKED
3. 最近 Decision Log
4. Handoff
5. Knowledge State
6. Open Setup / Payoff
7. 当前未解决问题

不必每次重新读整部剧。

---

# 17. 连续性扫描

```text
□ 年龄 / 日期
□ 地点 / 移动
□ 人物知道什么
□ 关系状态
□ 伤势
□ 物件
□ 钱 / 权力 / 职位
□ 秘密
□ 世界规则
□ Setup / Payoff
□ 改编决策
```

---

# 18. 核心目标

> 下一次继续写时，不重新发明这部剧。
