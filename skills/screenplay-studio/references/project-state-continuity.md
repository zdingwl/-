# Project State & Continuity

长项目的稳定性依赖显式状态，而不是模型对前文的模糊记忆。

## 1. 四级状态

### LOCKED

用户明确确认、源文本已验证或项目已经正式采用的正典。

不得在后续生成中悄悄修改。

### ASSUMED

为了不中断推进而作出的合理临时假设。

后续出现更高置信信息时可以覆盖。

### PROPOSED

候选方案，尚未进入正典。

不得让人物在正文中把 PROPOSED 当成已发生事实。

### REJECTED

用户或项目已经否决的方案。

后续重写不得无意重新引入。

## 2. Project State

至少维护：

~~~yaml
project_state:
  project_contract:
  canon:
  assumptions:
  proposed:
  rejected:
  story_contract:
  character_states:
  relationship_states:
  timeline:
  locations:
  objects_resources_evidence:
  secrets:
  audience_knowledge:
  character_knowledge:
  setups_payoffs:
  adaptation_ledger:
  unresolved_questions:
  current_unit:
  completed_units:
  rewrite_history:
~~~

## 3. Character State

每个主要人物动态维护：

- 当前目标
- 当前策略
- 当前伤势/身体状态
- 拥有资源
- 失去资源
- 当前关系位置
- 当前秘密
- 已作出的不可逆决定
- 当前弧光阶段

人物小传是静态资料，不能替代 Character State。

## 4. Character Knowledge

~~~yaml
character_knowledge:
  character:
  knows:
  believes_true:
  falsely_believes:
  suspects:
  does_not_know:
  hiding:
  source_of_knowledge:
  last_updated_at:
~~~

角色只能根据自己在当前时间点实际拥有的信息行动。

任何 Reveal、偷听、调查、误导或坦白，都应更新 Knowledge State。

## 5. Audience Knowledge

同时维护观众：

- 已知事实
- 怀疑
- 误信
- 未解决问题
- 已获得但角色尚未知的优势信息

悬疑设计不能只维护“秘密是什么”，还要维护“谁在什么时候知道什么”。

## 6. Relationship State

重要关系记录：

~~~yaml
relationship_state:
  a:
  b:
  power:
  trust:
  dependency:
  debt:
  intimacy_risk:
  active_conflict:
  shared_secret:
  last_irreversible_event:
~~~

关系标签如“母女”“情侣”“同事”不代表当前关系状态。

## 7. Timeline

记录：

- 绝对时间（可知时）
- 相对时间
- 事件顺序
- 地点移动
- 伤势恢复
- 资源转移
- 信息获得时间
- 公开事件

任何重排 POV、回忆或 Reveal 都必须重新检查 Timeline 与 Knowledge State。

## 8. Objects / Resources / Evidence

关键物件记录：

- 当前持有者
- 最后出现位置
- 功能
- 谁知道它存在
- 是否已使用
- 是否仍可使用
- 是否构成 Setup / Payoff

避免证据、手机、钥匙、武器、合同、钱或伤势在场景间“瞬移”。

## 9. Setup / Payoff

~~~yaml
setup_payoff:
  setup:
  source_or_scene:
  apparent_function:
  actual_function:
  payoff:
  payoff_location:
  status: open | partial | paid | abandoned
~~~

重写删除 Setup 前，先检查所有下游 Payoff。

## 10. 每个单元完成后的更新

电影 Sequence、剧集 Episode、短剧 Arc Block 或重要场景完成后：

~~~text
新事实
→ Canon
→ Character State
→ Relationship State
→ Timeline
→ Objects / Resources / Evidence
→ Secrets
→ Character Knowledge
→ Audience Knowledge
→ Setup / Payoff
→ Unresolved Questions
~~~

下一单元必须从更新后的状态开始。

## 11. Rewrite Safety

重写前记录：

- 修改范围
- 被修改的上游事实
- 可能受影响的下游场景
- 受影响的 Knowledge State
- 受影响的 Setup / Payoff

重写后重新验证受影响的单元及其下游依赖。

不要把旧版本已删除的事实重新混回新稿。
