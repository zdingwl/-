# Workflow：统一重写编排

本流程把审稿意见转换为可控的重写计划。

核心原则：

> 一次从上游到下游修，不在多个层级同时乱改。

---

# 1. 汇总 Issues

先按根因聚类：

```text
Premise
Causality
Character
Adaptation
Structure
Episode
Scene
Information
Continuity
Dialogue
```

多个症状可能只有一个根因。

---

# 2. 生成 Rewrite Plan

```yaml
rewrite_plan:
  draft_from:
  target_version:

  protected_elements:

  changes:
    - order:
      priority:
      root_issue:
      change_layer:
      affected_units:
      required_repairs:
      re_review_passes:

  do_not_touch:
```

---

# 3. 重写顺序

推荐：

```text
P0 Premise / 正典
→ P0 因果
→ Adaptation Core
→ Character
→ Structure
→ Episode
→ Scene
→ Information
→ Continuity
→ Dialogue
→ Compression / Polish
```

---

# 4. 影响范围

每项修改必须写：

- 直接修改位置
- 上游依赖
- 下游依赖
- 伏笔影响
- Knowledge State 影响
- Relationship 影响
- Ending 影响

---

# 5. 单一主笔

正式 Rewrite 由一个 Lead Writer 统一执行。

Reviewers 只提供 Notes。

原因：

- 保护同一人物声音
- 避免局部最优互相冲突
- 保证正典统一

---

# 6. 局部重写

如果只涉及一场：

先确认问题真的是 Scene / Dialogue，而不是上游结构。

局部修改后更新：

- Handoff（如状态变化）
- Knowledge
- Setup / Payoff
- Decision Log（重大时）

---

# 7. 大规模重写

如果涉及：

- 主角目标
- 核心关系
- 中段
- 结局
- 关键 Reveal
- 人物合并

必须先修改：

Story Bible / Adaptation Bible / Structure

再写正文。

---

# 8. Rewrite Verification

每完成一项：

```text
原问题是否消失？
有没有破坏 Protected Element？
有没有产生新连续性问题？
下游场景还成立吗？
```

---

# 9. Re-review Matrix

```text
Premise 修改
→ Structure + Character + Continuity + Dialogue

Character Arc 修改
→ Structure + Continuity + Dialogue

Reveal 修改
→ Structure + Knowledge + Continuity + Dialogue

Scene 修改
→ Continuity + Dialogue

Dialogue 修改
→ Dialogue + 局部 Continuity（必要时）
```

---

# 10. Final Merge

所有修订完成后：

- 升 Draft Version
- 更新 Decision Log
- 更新 Project State
- 标记已解决 Review Issues
- 保留未解决风险
