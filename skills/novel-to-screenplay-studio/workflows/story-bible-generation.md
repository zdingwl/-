# Workflow：从源素材自动收敛 Story Bible

适用于：已经完成 Source Index 的长篇改编项目。

核心原则：

> Story Bible 不是章节摘要集合，而是“当前可验证正典 + 戏剧功能”的压缩模型。

---

# Phase 1：汇总可验证事实

从 Source Index 提取：

- 人物身份
- 时间
- 地点
- 世界规则
- 关系
- 秘密
- 物件
- 资源
- Setup / Payoff

去重、合并别名。

冲突事实不得直接二选一，先标记：

`CONFLICT / NEEDS_VERIFICATION`

---

# Phase 2：人物收敛

为主要角色建立：

- 外在目标
- 内在需求
- Misbelief
- 资源
- 秘密
- 核心关系
- 关键选择
- Arc 状态

注意：

这些字段必须来自“事件证据”，不是只从作者介绍推断。

---

# Phase 3：关系收敛

读取：

`references/relationship-extraction.md`

把互动日志压成：

- 起点
- 关键转折
- 当前状态
- 终局状态（若源素材已完结）

---

# Phase 4：时间线收敛

统一：

- 绝对日期
- 相对日期
- 回忆
- 跳时
- 平行线

发现冲突：

- 记录冲突
- 回源素材复核
- 不擅自修正原作

---

# Phase 5：秘密与知识收敛

分别建立：

```text
Secret Ledger
+
Knowledge State
```

同一秘密不能只记录“是否揭露”，还要记录：

- 谁知道
- 谁怀疑
- 谁误信
- 谁尚不知道
- 观众知道多少

---

# Phase 6：Story DNA 推导

只有完成前五步后，才推导：

- 主角
- 主目标
- 核心关系
- 戏剧问题
- 主题问题
- 对抗
- Stakes
- 情绪承诺
- Ending State

每项写“证据来源”。

---

# Phase 7：正典层级

源素材明确事实：

LOCKED

根据证据高度可信但未完全验证：

ASSUMED

改编建议：

PROPOSED

用户否决或已淘汰：

REJECTED

---

# Phase 8：Bible 压缩

最终 Story Bible 不保存所有章节细节。

只保留：

- 会影响后续写作的事实
- 会影响人物选择的事实
- 会影响因果的规则
- 会影响 Reveal 的知识
- 会影响结局的 Setup

---

# Phase 9：更新策略

后续每个正式剧本单元完成后：

```text
正文变化
→ Handoff
→ Continuity
→ Story Bible 必要字段
```

不需要每次重建整个 Bible。
