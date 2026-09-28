# Review Pass System

本文件定义“独立审稿 + 主编剧裁决”的 Writers' Room 审稿体系。

核心原则：

> Review Pass 负责发现问题，不负责各自直接重写整部剧。最终修改权属于统一的 Lead Writer / Executive Review。

---

# 1. 为什么要拆 Review Pass

如果同一个 Pass 同时检查：

- 结构
- 人物
- 改编
- 连续性
- 对白
- 媒介

常见结果是：

- 根问题被表面问题淹没
- 不同层级建议互相冲突
- 一处修改破坏另一处已经成立的东西
- Reviewer 越权重写作品

因此拆成独立只读审稿。

---

# 2. 标准 Review Pass

## Structure Review

检查：

- Premise
- 因果
- Story Spine
- 中段
- 高潮
- 结局
- 分集 / 段落功能
- Setup / Payoff

不负责：

- 润色对白
- 改角色说话方式

## Character Review

检查：

- 主角主动性
- Want / Need / Misbelief
- 行为是否符合知识和压力
- 人物弧
- 核心关系
- 对手策略
- 角色功能重复

不负责：

- 重新设计全剧结构，除非人物问题直接暴露结构根因

## Adaptation Integrity Review

仅改编项目。

检查：

- 原作核心情绪是否保住
- 标志性人物关系是否被削弱
- 改编取舍是否有功能理由
- CUT / MERGE 是否造成因果缺口
- INVENT 是否破坏原作核心
- 影视版是否独立成立

## Medium Fit Review

检查：

- 电影 / 剧集 / 短剧 / 动画是否匹配
- Story Engine 与时长 / 集数是否匹配
- 信息密度
- 单元边界
- 节奏
- 重复资产 / 制作规模（适用时）

## Continuity Review

检查：

- 人物知识
- 时间
- 地点
- 物件
- 资源
- 伤势
- 关系状态
- 秘密
- 世界规则
- Setup / Payoff

## Dialogue Review

最后执行。

检查：

- Dialogue as Action
- Subtext
- Voice Fingerprint
- 重复信息
- 说明性对白
- 人工智能腔
- 节奏和自然度

不允许用漂亮对白掩盖结构问题。

---

# 3. Review 输出格式

每个问题必须包含：

```yaml
review_issue:
  pass:
  priority: P0 | P1 | P2
  location:
  symptom:
  evidence:
  root_cause:
  impact:
  protected_elements:
  proposed_direction:
  dependencies:
  confidence: high | medium | low
```

---

# 4. P0 / P1 / P2

## P0

不修则故事、正典或改编本身不成立。

例如：

- 人物使用未知信息
- 高潮无前置因果
- 改编删掉核心关系
- 结局与锁定设定冲突

## P1

严重降低观看体验。

例如：

- 中段重复
- 主角长期被动
- 分集无功能
- Reveal 不改变任何东西

## P2

精修。

例如：

- 台词过长
- 轻微节奏
- 动作表达
- 格式

---

# 5. Reviewer 证据规则

禁止：

> “感觉这里不够好。”

必须指出：

- 具体集 / 场 / Beat
- 当前状态
- 预期功能
- 实际问题
- 连带影响

---

# 6. Reviewer 不得越权

Reviewer 可以提出：

- 问题
- 根因
- 修复方向
- 影响范围

但不要直接把自己的方案当成正典。

所有建议先进入：

`Review Conflict Resolution`

再由 Lead Writer 裁决。

---

# 7. 审稿顺序

推荐：

```text
Structure
→ Character
→ Adaptation Integrity（适用）
→ Medium Fit
→ Continuity
→ Dialogue
→ Executive Review
```

如果 Structure 存在 P0，不要浪费时间做完整 Dialogue Pass。

---

# 8. Stop Condition

当某一上游 Pass 出现 P0：

- 记录其他明显问题
- 暂停下游精修
- 先进入 Executive Review 决定结构修复

---

# 9. Protected Elements

每个 Pass 都必须尊重：

- LOCKED
- 用户明确要求
- 改编 Protected Core
- 已验证正典

如果建议需要改动 Protected Element，必须明确标记：

`REQUIRES_USER_OR_LEAD_OVERRIDE`

---

# 10. Review 的目标

> 不是让每个 Reviewer 都“写得更像自己”，而是帮助同一部作品更稳定地成为它本来应该成为的版本。
