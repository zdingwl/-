# Series & Episode Engine

## 剧集不是拉长的电影

剧集需要：

~~~text
Series Engine + Episode Engine
~~~

Series Engine：为什么这组人物能持续产生故事？
Episode Engine：为什么这一集本身值得存在？

## Season Contract

~~~yaml
season:
  season_question:
  protagonist_goal:
  opposing_force:
  relationship_engine:
  mystery_or_unknown:
  escalation_path:
  midpoint_shift:
  endgame:
  final_choice:
  next_season_residue:
~~~

## Episode Function

每集必须承担清晰职责，例如：建立异常、形成联盟、第一次胜利、代价反扑、秘密升级、关系破裂、目标改变、真相重定义、大失败、终局集结。

不要多集重复“继续调查”“继续误会”。

## A / B / C Story

A：核心外部剧情。
B：人物弧 / 核心关系。
C：世界、配角、主题或未来发动机。

多线应在阶段转折互相影响，而不是彼此平行不相干。

## Episode Arc

~~~text
开场状态
→ 当前问题
→ 人物行动
→ 阻力升级
→ 中段变化
→ 选择
→ 后果
→ 集尾新状态
~~~

## Cliffhanger

不是随便切黑。有效集尾来自本集后果：新事实改变意义、不可逆选择、危险启动、关系重定义、观众领先人物知道真相、目标实现但代价启动下一集。

## Information Design

~~~yaml
information:
  audience_knows:
  protagonist_knows:
  antagonist_knows:
  other_characters_know:
  false_beliefs:
  reveal_trigger:
  consequence_of_reveal:
~~~

悬念包括未知型和预期型。

## Escalation

升级可以是时间更少、资源更少、关系代价更高、道德代价更高、对手学习更快、选择更不可逆、秘密牵涉更多人。

## Continuity

每集结束更新人物知识、关系、身体状态、物件/证据/资源、时间、地点、秘密、Setup/Payoff。


## Long-Running Hook Architecture

长线连载至少区分：

- Episode Hook：本集结果直接产生的下一问题。
- Arc Hook：5–10 集阶段兑现后改变目标、规则、敌人或世界规模。
- Season Hook：本季主问题得到回答，但留下明确 Next Season Residue。
- Saga Hook：跨季解释的世界核心谜团。

~~~yaml
hook:
  id:
  planted_at:
  surface_question:
  hidden_question:
  audience_knows:
  protagonist_knows:
  status: open | partial | paid | abandoned
  planned_payoff:
  payoff_horizon: episode | arc | season | multi_season
  dependency:
  risk_if_revealed_early:
~~~

不要第一季烧完全部世界秘密。

## Escalation Is Not Just Bigger Enemies

长期升级可以来自：

- 资源更紧
- 责任范围扩大
- 组织政治复杂
- 信息可靠度下降
- 能力曝光
- 对手学习
- 伦理代价
- 世界规则变化
- 地理范围扩大
- 新秩序竞争

避免只靠“更大的怪物 / 更多敌人 / 更高数值”维持连载。

## Growth Creates Opposition

主角获得资源、基地、技术、秘密或社会影响力后，应问：

- 谁因此失去利益？
- 谁会觊觎新成果？
- 谁开始怀疑主角？
- 旧对手学到了什么？
- 主角需要为增长承担什么维护成本？

长期 Story Engine 优先：

~~~text
成长
→ 被看见
→ 被觊觎
→ 反制
→ 损失 / 代价
→ 再成长
~~~
