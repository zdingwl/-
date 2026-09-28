# Rewrite Existing Script Workflow

## 入口

适用于用户已经有完整或部分剧本，需要诊断、压缩、扩展、重构、改人物、改场景或改对白。

## 第一阶段：冻结原稿事实

先提取：
- 当前 Story Contract
- 主角目标
- 主要对抗
- 结构节点
- 人物弧
- 核心关系
- 每场功能
- 人物知识状态
- 连续性事实

## 第二阶段：Script Doctor

按 P0 → P5 诊断。

不要先润色台词。

## 第三阶段：Rewrite Plan

~~~yaml
rewrite:
  keep:
  delete:
  move:
  merge:
  invent:
  restructure:
  character_changes:
  scene_changes:
  information_changes:
  dialogue_pass:
~~~

## 第四阶段：Lead Rewrite

由一个统一写作者执行所有修复，避免多个审稿意见分别重写造成版本分裂。

## 第五阶段：验证

只重跑受影响层级及其下游：

- 改 Premise → 全部重检
- 改人物目标 → 结构、场景、对白重检
- 改信息释放 → 场景、悬念、连续性重检
- 只改对白 → 场景功能与人物声音重检

## 完成门槛

修订后必须能说明：
- 根问题是否消失
- 是否引入新连续性问题
- 是否改变类型承诺
- 是否让主角更主动
- 场景是否更少但更有功能
