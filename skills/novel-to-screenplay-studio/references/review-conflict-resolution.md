# Review Conflict Resolution

多个 Reviewer 的建议可能相互冲突。本文件定义主编剧如何裁决。

---

# 1. 冲突类型

## 结构 vs 人物

Structure Review：
> 提前揭露秘密可以加快节奏。

Character Review：
> 提前揭露会破坏人物仍然相信谎言时的关键选择。

不能简单选一个。

需要问：

> 哪个功能对核心戏剧问题更重要？是否存在第三种 Reveal 方式？

## 改编忠实度 vs 媒介适配

Adaptation Review：
> 该支线是原作重要情绪组成。

Medium Review：
> 电影时长无法完整承载。

解决方法通常不是“保留全部 / 全删”，而是：

- MERGE
- TRANSFORM
- MOVE
- 用一场承担多个功能

## 连续性 vs 新创意

新创意如果违反已锁定时间线或 Knowledge State：

默认连续性优先。

除非 Lead Writer 明确批准 Retcon，并完成所有下游修复。

---

# 2. 裁决优先级

```text
1. 用户明确 LOCKED 要求
2. 正典 / 连续性硬事实
3. 改编 Protected Core
4. 核心 Story DNA
5. 因果与人物选择
6. 目标媒介
7. 类型承诺
8. 场景与对白优化
9. 单纯个人偏好
```

---

# 3. 冲突记录

```yaml
review_conflict:
  id:
  issue:
  reviewer_a:
  reviewer_b:
  shared_evidence:
  disagreement:
  protected_elements:
  options:
    - option:
      gains:
      losses:
      downstream_changes:
  lead_decision:
  reason:
  affected_units:
  status:
```

---

# 4. 最小修复原则

当两个建议都成立时：

优先找：

> 能解决根问题，同时改动最少正典与已成立内容的方案。

不要为了修一个局部问题重写整部作品。

---

# 5. 根因优先

例如：

- Dialogue Reviewer 认为台词解释太多
- Structure Reviewer 发现观众缺少必要信息

不能单纯删台词。

真正问题可能是：

> 信息没有被事件化。

应回到场景 / 结构层修复。

---

# 6. 不做平均主义

不要把两个冲突建议“各采一半”。

如果两种方向本质互斥，Lead Writer 必须作出明确选择。

---

# 7. Decision Log

裁决后：

- 更新 Decision Log
- 更新受影响 Story Bible
- 标记需要重写的单元
- 标记需要重新 Review 的 Pass

---

# 8. Re-review

重大结构修复后：

```text
只重跑受影响 Pass
+
所有下游依赖 Pass
```

例如：

结构改动：
→ Character / Continuity / Dialogue 可能需要重跑。

仅台词修改：
→ 通常不需要重跑 Structure。
