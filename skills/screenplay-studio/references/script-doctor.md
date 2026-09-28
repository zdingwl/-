# Script Doctor

## 目标

~~~text
症状 → 根因 → 影响范围 → 修复优先级 → 最小有效改动
~~~

## P0：项目根问题

Premise 不成立、主角无目标、Story Engine 无法持续、类型承诺错位、结局无法回答核心问题。

P0 存在时不进入对白精修。

## P1：结构

因果断裂、主角长期被动、中段重复、对手不反制、低谷随机、高潮不来自人物选择。

## P2：人物与关系

人物弧无行为证明、配角只有功能、核心关系长期静止、人物行为与知识冲突、对手降智。

## P3：场景

无目标、无阻力、无策略变化、无状态变化、只负责解释。

## P4：对白

同声同气、直接说情绪、双方已知信息互相解释、潜台词缺失、金句压过人物。

## P5：连续性与格式

时间冲突、知识状态冲突、道具/证据消失、伤势重置、场景标题不一致、格式影响阅读。

## Evidence First

诊断必须引用具体场景或剧情证据，不只说“节奏不好”。

## Root Cause

对白啰嗦可能是场景没有目标。修复场景目标优先于删句子。

## Rewrite Order

1. Premise
2. Story Engine
3. 主角主动性
4. 因果
5. Stakes
6. 人物弧
7. 核心关系
8. 结构
9. Sequence / Episode
10. Scene
11. Information
12. Dialogue
13. Visual Action
14. Continuity
15. Format

## Revision Report

~~~yaml
issue:
  id:
  priority: P0 | P1 | P2 | P3 | P4 | P5
  evidence:
  symptom:
  root_cause:
  affected_range:
  repair_strategy:
  risk:
  verify_after_rewrite:
~~~

优先寻找最小有效改动：调整顺序、合并场景、改变一个选择、提前信息、删除重复功能、让既有后果持续生效。
