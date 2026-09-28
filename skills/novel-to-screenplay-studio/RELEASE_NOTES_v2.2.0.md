# v2.2.0 Release Notes

## Novel To Screenplay Studio 2.2

2.2 的重点是把“剧本医生”升级为真正可控的 Writer's Room 审稿系统。

## 为什么需要多阶段 Review

单一 Reviewer 同时检查结构、人物、改编、连续性和对白时，常出现：

- 根问题被表面问题淹没
- 多个层级建议互相冲突
- Reviewer 越权直接重写正典
- 为了修对白破坏结构
- 为了提速破坏人物弧

2.2 将审稿拆成独立 Pass，再由 Lead Writer 统一裁决。

## 标准审稿顺序

```text
Structure Review
→ Character Review
→ Adaptation Integrity Review（改编项目）
→ Medium Fit Review
→ Continuity Review
→ Dialogue Review
→ Executive Review
→ Unified Rewrite
```

## 新增：Review Stop Condition

如果 Structure / Character 等上游层出现 P0：

- 暂停完整 Dialogue Polish
- 先进入 Executive Review
- 解决根问题后再继续下游审稿

## 新增：Review Conflict Resolution

不同 Reviewer 意见冲突时：

```text
用户 LOCKED
→ 正典
→ 改编 Protected Core
→ Story DNA
→ 因果 / 人物
→ 媒介
→ 类型承诺
→ 场景 / 对白
```

按优先级裁决。

不采用“各改一半”的平均主义。

## 新增：Lead Writer 单一主笔

Reviewers 只负责：

- 问题
- 证据
- 根因
- 影响
- 修复方向

正式 Rewrite 由一个 Lead Writer 统一执行。

这样保护：

- 人物声音
- 正典
- Story Bible
- 改编方向
- 全剧一致性

## 新增：Re-review Matrix

修改不同层级后，只重跑受影响 Pass 和下游依赖。

例如：

```text
Premise 修改
→ Structure + Character + Continuity + Dialogue

Reveal 修改
→ Structure + Knowledge + Continuity + Dialogue

Dialogue 修改
→ Dialogue + 必要局部 Continuity
```

## 新增模板

- Structure Review
- Character Review
- Adaptation Integrity Review
- Medium Fit Review
- Continuity Review
- Dialogue Review
- Executive Review
- Review Issue
- Review Conflict

## 新增工作流

- `workflows/writers-room-review.md`
- `workflows/rewrite-orchestration.md`

## 推荐入口

主 Skill：

`skills/novel-to-screenplay-studio/SKILL.md`

Writer's Room：

`skills/novel-to-screenplay-studio/workflows/writers-room-review.md`
