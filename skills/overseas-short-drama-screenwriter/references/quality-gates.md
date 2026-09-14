# Quality Gates

Run these gates before calling a screenplay complete.

## Gate 0 — 最新市场数据必须来自本次实时检索

这是市场驱动项目的最高优先级硬性 Gate。

如果任务包含“最新、当前、近期、榜单、排名、热门、爆款、趋势、增长、市场”等要求，必须满足：

```text
□ 本次任务中实际进行了外部实时检索
□ 没有用模型训练数据 / 内置知识代替当前榜单
□ 目标国家已经明确
□ 检索日期已经记录
□ 重要来源有可追溯出处
□ 重要来源的发布时间 / 更新时间 / 检索时间已核对（能获取时）
□ 最新排名优先采用当前官方榜单或当前页面
□ 当前趋势至少有多个当前来源交叉验证，或明确标注证据不足
□ 180 天以上资料只作为历史背景，不单独证明“当前热门”
□ 无法验证的当前数据没有被模型记忆补齐
□ 研究报告明确区分“当前已验证事实”和“基于数据的创作判断”
```

Hard fail conditions:

> 没有联网/外部检索，却声称“这是目前最火的题材”。

> 实时资料不足，于是用模型记忆中的旧榜单补成“最新排名”。

> 使用旧报告证明今天的榜单，却没有检查更近期数据。

> 没有来源或日期依据，却给出精确的当前排名、下载、收入或市场份额。

如果 Gate 0 失败：

```text
不得进入“根据最新市场生成创意”的正式流程；
不得把结果标记为当前市场结论；
必须重新检索，或明确说明无法确认最新数据。
```

---

## Gate 1 — Market fit

```text
□ target country is explicit
□ target language is explicit when it materially affects localization
□ current market evidence was researched when required
□ the concept is not based on one title only
□ the emotional promise matches the intended audience
□ saturated tropes have a meaningful differentiator
```

Fail condition:

> The story is described as “popular overseas” without current evidence or without defining which overseas market.

## Gate 2 — Originality

Compare against research samples:

```text
□ title is distinct
□ protagonist combination is distinct
□ inciting incident is not copied
□ central secret is not copied
□ major reveal sequence is not copied
□ climax is not copied
□ ending is not copied
□ distinctive set pieces are not copied
```

Fail condition:

> The project can be summarized as “existing title with changed names.”

## Gate 3 — Story engine

```text
□ protagonist has a concrete goal
□ opposing force has a concrete goal
□ stakes are clear
□ central relationship has a conflict engine
□ external story exists beyond a single misunderstanding
□ secrets / reveals can escalate rather than repeat
□ the story can sustain the requested episode count
```

Fail condition:

> One honest conversation in Episode 3 would permanently solve the series.

## Gate 4 — Protagonist agency

```text
□ protagonist makes consequential decisions
□ protagonist sometimes causes their own problems
□ protagonist changes tactics after failure
□ protagonist earns major wins
□ climax depends on protagonist choice
```

Fail condition:

> The lead only suffers, waits, and gets rescued.

## Gate 5 — Episode function

For every episode:

```text
□ opening contains a current dramatic question
□ protagonist wants something now
□ an obstacle appears
□ conflict escalates or changes
□ at least one meaningful turn occurs
□ audience receives information or emotional value
□ ending creates a specific next question
□ episode state differs from opening state
```

Fail condition:

> Episode exists only to repeat a conflict from the previous episode.

## Gate 6 — Scene function

For every scene:

```text
□ someone wants something
□ someone / something blocks them
□ the scene contains behavior, not pure explanation
□ at least one value changes
□ new information or consequence appears
□ deleting the scene would damage the story
```

Merge or delete scenes that fail repeatedly.

## Gate 7 — Causality

For each major beat:

```text
□ the event has a cause
□ the character's choice fits their knowledge
□ the choice fits their personality and pressure
□ the consequence follows logically
□ a simpler solution has been considered
□ the script explains why that simpler solution is unavailable
```

Fail condition:

> “Because the plot needs it.”

## Gate 8 — Escalation

```text
□ conflict changes level or meaning
□ antagonist adapts
□ victories create consequences
□ setbacks are not identical
□ later episodes cost more than early episodes
```

Fail condition:

> The same humiliation / misunderstanding / argument is replayed with different wording.

## Gate 9 — Relationship progression

```text
□ relationship states visibly change
□ attraction and conflict both have causes
□ trust is earned or damaged through action
□ betrayal has setup
□ reconciliation has cost
□ final relationship state answers the story promise
```

Fail condition:

> Characters alternate between love and hate only to stretch runtime.

## Gate 10 — Information control

```text
□ character knowledge is tracked
□ audience knowledge is intentionally managed
□ no character knows unlearned information
□ reveals change behavior
□ secrets are neither forgotten nor repeated endlessly
```

## Gate 11 — Setup / payoff

```text
□ major setup ledger is current
□ important objects have purpose
□ promises are paid off
□ abandoned setups are intentionally removed or resolved
□ final climax uses earlier setup where appropriate
```

## Gate 12 — Localization

```text
□ setting is geographically coherent
□ names fit the target market
□ occupations are plausible
□ family power has a believable mechanism
□ money and status symbols fit
□ marriage / inheritance / legal assumptions are checked when important
□ institutions behave plausibly
□ target-language dialogue sounds native
□ culture is specific without becoming stereotype
```

## Gate 13 — Dialogue

```text
□ major characters sound different
□ dialogue has objectives
□ exposition is embedded in conflict
□ lines are speakable
□ repeated information is cut
□ emotional statements are not duplicating visible action
□ target-language idiom is natural
```

## Gate 14 — Screenplay format

```text
□ scene headings are consistent
□ action is filmable
□ internal thought is converted to action / dialogue where needed
□ parentheticals are used sparingly
□ screenplay is not polluted with storyboard / camera / generation prompts
```

## Gate 15 — Continuity

Check:

```text
time
location
injuries
clothing only when plot-relevant
possessions
money
relationships
secrets
identities
legal constraints
pregnancy / age / dates where relevant
supernatural rules
```

Fail condition:

> A later scene contradicts locked story facts without explanation.

## Gate 16 — Ending

```text
□ central dramatic question is answered
□ external plot is resolved or intentionally opened
□ central relationship reaches a meaningful final state
□ protagonist's final choice proves the arc
□ climax is earned from prior setup
□ ending is not solved by a new coincidence
```

## Gate 17 — 中文主稿与外语对白翻译

这是强制 Gate。

```text
□ 市场分析与策划说明默认中文
□ 人物设定默认中文
□ 分集大纲默认中文
□ 正式剧本场景标题为中文
□ 正式剧本动作描述为中文
□ 正式剧本人物说明为中文
□ 英文对白后逐句附中文翻译
□ 其他外语对白后逐句附中文翻译
□ 中文翻译准确表达原句语义
□ 中文翻译保留语气、情绪和潜台词
□ 没有遗漏大段纯外语内容
□ 没有把全部翻译集中放到剧本最后
```

Fail condition:

> 中文团队需要自己翻译外语对白才能完整理解剧本。

除非用户明确要求纯外语发行稿，否则本 Gate 不允许跳过。

## Scoring rubric

Score out of 100:

```text
Premise / concept strength       8
Market / audience fit            8
Original differentiation        8
Protagonist agency              10
Character consistency            8
Relationship engine             10
Causality                       10
Episode architecture            10
Scene efficiency                 8
Dialogue                         8
Localization                     5
Continuity                       4
Setup / payoff                   3
-------------------------------
Total                          100
```

推荐阈值：

```text
90–100  strong final draft candidate
82–89   usable but revise weak categories
75–81   structural revision required
<75     do not call final
```

注意：

- 即使总分超过 90，如果 Gate 0 失败，不得声称创意基于“最新市场”。
- 即使总分超过 90，如果 Gate 17 失败，也不得标记为最终中文交付稿。
