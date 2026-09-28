# Workflow：Writer's Room 多阶段审稿

适用：

- 完成 Outline
- 完成 Episode Map
- 完成重要阶段 Draft
- 完成全剧 First Draft
- 大规模改编方案准备锁定

---

# Phase 0：冻结审稿版本

记录：

```yaml
review_snapshot:
  project:
  draft_version:
  reviewed_scope:
  locked_elements:
  adaptation_protected_core:
```

所有 Reviewer 必须审同一版本。

---

# Phase 1：Structure Review

读取：

- Story Bible
- Story Spine / Episode Map
- Setup / Payoff
- Draft（必要范围）

输出 P0 / P1 / P2。

如果发现 P0：

可提前进入 Executive Review。

---

# Phase 2：Character Review

重点检查：

- 主角是否主动
- 人物选择是否符合知识 / 压力
- 人物弧是否由选择证明
- 核心关系是否真实变化
- 对手是否适应
- 是否有功能重复角色

---

# Phase 3：Genre Review

读取：

- Genre Contract
- Story Bible
- 对应 Genre Profile
- 当前 Draft

检查：

- 类型核心承诺是否持续
- 阶段回报是否缺失或重复
- 是否出现无意识 Genre Drift
- 高潮与结局是否回应类型期待

---

# Phase 4：Adaptation Integrity Review

仅 Adaptation Mode。

对照：

- Source Analysis
- Adaptation Bible
- Protected Core
- 当前 Draft

检查：

- 原作为什么有效的部分是否仍在
- 改动是否让屏幕版更成立
- 是否出现“已经很好看，但已经不是这部作品”

---

# Phase 5：Medium Fit Review

检查目标媒介：

- Feature
- Series
- Short Drama
- Animation

重点：

- Engine
- 单元边界
- 时长
- 信息密度
- 节奏
- 制作复杂度

---

# Phase 6：Continuity Review

读取所有状态：

- Story Bible
- Timeline
- Knowledge State
- Secret Ledger
- Object / Resource State
- Setup / Payoff
- Handoff

这是独立硬逻辑扫描。

---

# Phase 7：Dialogue Review

只在上游无未解决 P0 后执行完整 Pass。

检查：

- 对白行动
- 潜台词
- Voice
- 说明性
- 重复
- Anti-AI

---

# Phase 8：Conflict Board

汇总所有 Review Issues。

相同根因合并。

相互冲突的建议进入：

`references/review-conflict-resolution.md`

---

# Phase 9：Executive Review

Lead Writer 做最终裁决。

输出：

- Protect
- Must Fix
- Should Fix
- Do Not Change
- Rewrite Order
- Re-review Plan

---

# Phase 10：Rewrite

进入：

`workflows/rewrite-orchestration.md`

禁止多个 Reviewer 各自直接重写同一场或同一集。

---

# Phase 11：验收

重写后：

- 重跑受影响 Pass
- 检查新修复是否制造回归
- 更新 Project State
- 更新 Draft Version
