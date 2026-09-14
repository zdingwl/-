# Market Research Protocol

Use this file whenever a project depends on current overseas short-drama, web-fiction, ranking, popularity, trend, audience, platform, or market information.

## Goal

The goal is not to copy chart leaders. The goal is to understand, from **current external evidence**:

- what audiences are consuming now
- which titles are currently ranking or rising
- which emotional promises repeat across successful titles
- which tropes are evergreen
- which elements are rising
- which combinations are saturated
- which signals are weakening
- where there may be a useful opportunity gap

---

# Gate 0 — Target country is mandatory

Before any overseas market research, concept generation, localization, or screenplay writing begins, the **target country must be known**.

If the user has not provided a country, stop the creative workflow and ask one concise question first:

> 你这部短剧准备主要面向哪个国家或地区？例如美国、英国、加拿大、澳大利亚、德国、法国、西班牙、巴西、日本等。

Do **not** silently default to the United States.

Do **not** interpret “海外”“国外”“英文市场”“欧美” as a specific country.

If the user answers with a broad region such as “欧美”“欧洲”“拉美” and the project requires country-level localization, ask them to choose the primary country.

If they intentionally want a multi-country regional project, record:

```yaml
market:
  primary_country:
  secondary_markets:
```

The primary country controls the first-pass research, local reality checks, institutions, money, occupations, social norms, and dialogue localization.

Only after the target country is established may the workflow continue.

---

# Gate 1 — Current data must come from live external research

This is a **hard rule**.

Whenever the request includes or implies any of the following:

```text
最新
当前
现在
近期
本周
本月
今年
榜单
排名
Top
热门
爆款
趋势
增长
下载
收入
市场份额
正在流行
最新小说
最新短剧
```

The system must perform **live external research during the current task** before making market claims or using those claims to choose a story direction.

## Model memory is prohibited as market evidence

The model's built-in knowledge, training data, cached general knowledge, prior assumptions, or remembered rankings may be used only for:

- terminology
- general screenwriting theory
- research methodology
- historical background clearly labeled as historical

They must **not** be used as evidence for:

- current rankings
- current top titles
- current platform popularity
- current genre popularity
- current trope frequency
- current audience preference
- current downloads / revenue / growth
- current market size
- current app performance
- current release status
- claims such as “现在最火的是……”

If no live source was checked in the current task, the system must not call the result “最新”“当前”“热门榜单” or equivalent.

---

# Gate 2 — Freshness window

Prefer sources in this order:

```text
0–7 days    → live charts, current releases, very recent changes
8–30 days   → current trend evidence
31–90 days  → sustained trend evidence
91–180 days → supporting context only when fresher evidence is insufficient
>180 days   → historical/background evidence, not proof of a current trend
```

For a request explicitly asking for the **latest ranking**, prioritize the newest available official ranking or page even if broader industry reports are older.

Do not use an old article merely because it appears high in search results.

When multiple sources conflict, prefer:

1. first-party current platform data
2. current app-store / chart data where relevant
3. recent reputable market intelligence / industry reporting
4. recent reputable trade press
5. secondary summaries only as support

---

# Gate 3 — Verify the date, not just the search result

A source appearing in a new search result does not mean the underlying information is new.

For every important source, inspect and record when available:

```yaml
evidence:
  source_name:
  page_or_report_title:
  url_or_reference:
  source_type: official | chart | report | trade_press | secondary
  published_at:
  updated_at:
  retrieved_at:
  target_country:
  claim_supported:
  freshness_class: 0-7d | 8-30d | 31-90d | 91-180d | historical
```

If a page has no publication date but is a live ranking page, label it as:

```text
live page / retrieval date verified
```

Do not invent publication dates.

---

# Gate 4 — Source hierarchy

## Short-drama research

Depending on country and current availability, prioritize live or first-party signals from platforms such as:

- ReelShort
- DramaBox
- GoodShort
- NetShort
- DramaWave
- ShortMax
- FreeReels
- official platform ranking/category pages
- Apple App Store / Google Play ranking signals where useful

Do not assume every platform is equally important in every country.

## Web-fiction research

Potential live sources include:

- GoodNovel
- WebNovel
- Wattpad
- Inkitt
- Galatea
- Radish
- Dreame
- Amazon Kindle genre charts where useful

Novel trends are upstream signals. Do not automatically assume a novel trope already performs as a short drama.

## Industry evidence

Use recent reputable market reports or trade reporting to validate:

- country growth
- platform share
- downloads
- revenue
- audience demographics
- category growth

Older annual reports can provide background but cannot override newer live signals.

---

# Gate 5 — Cross-source validation

Do not call something a market-wide trend because one platform promotes it.

A strong current signal should ideally be supported by two or more of:

- multiple current short-drama platforms
- current platform rankings plus recent industry data
- short-drama charts plus current web-fiction signals
- current charts plus recent app / market performance data

When only one reliable live source exists, label confidence accordingly.

Do not manufacture consensus.

---

# Gate 6 — Research sample size

For concept development, aim for:

```text
minimum useful sample: 20 titles
preferred sample: 30–60 titles
large exploratory sample: 60–100 titles
```

For a fast ranking check, a smaller sample is acceptable, but do not generalize beyond the evidence.

If live rankings are unavailable, reduce confidence rather than inventing data.

---

# Per-title Story DNA

Normalize relevant current titles into:

```yaml
title_sample:
  title:
  platform:
  country_signal:
  rank_or_signal:
  ranking_checked_at:
  release_or_update_recency:
  genre:
  visible_tags:
  protagonist_type:
  counterpart_type:
  central_relationship:
  inciting_incident:
  main_goal:
  core_obstacle:
  secret_or_identity_device:
  revenge_device:
  fantasy_device:
  status_device:
  opening_hook_family:
  primary_emotion:
  secondary_emotion:
  likely_payoff:
  evidence_source:
  notes:
```

Do not reproduce long copyrighted plot summaries. Capture high-level structural features only.

---

# Trend classification

Classify recurring elements as:

## Evergreen

Persistent across time and multiple current sources.

## Rising

Recent evidence shows increasing visibility, release frequency, chart presence, engagement, or investment.

## Saturated

Demand remains strong, but current supply is highly repetitive.

## Weak / declining

Current evidence is limited or weaker than earlier periods.

## Opportunity gap

There is evidence of audience demand, but fewer distinctive executions or less direct competition.

Every classification must be traceable to live evidence gathered in the current research pass.

---

# Emotional-engine analysis

Always translate surface trope labels into audience emotion.

Examples:

```text
Billionaire / high-status partner
→ security fantasy / status contrast / exclusivity / power imbalance

Revenge
→ injustice / delayed gratification / reversal / catharsis

Rejected mate
→ rejection pain / destiny / status reversal / pursuit

Secret identity
→ dramatic irony / underestimated protagonist / reveal payoff

Second chance
→ regret / nostalgia / unfinished intimacy / redemption
```

The emotional engine matters more than copying the surface trope.

---

# Opportunity matrix

Rate creative opportunities against:

```text
CURRENT DEMAND
x
CURRENT SATURATION
x
EMOTIONAL STRENGTH
x
LOCAL FIT
x
ORIGINALITY ROOM
```

Priority zone:

```text
current demand is evidenced
+
strong emotional engine
+
reasonable differentiation room
+
credible target-country fit
```

---

# Mandatory Evidence Ledger

Every market-led project must keep an Evidence Ledger.

Minimum format:

```text
Research date:
Target country:
Research window:

SOURCE 01
Source:
Page / ranking / report:
Published / updated:
Retrieved:
Current claim supported:
Freshness:
Confidence:

SOURCE 02
...
```

The final trend recommendation must be derivable from this ledger.

If the system cannot point to current external evidence, it must not describe a claim as current fact.

---

# Research output

Produce a compact Chinese report containing:

```text
1. 目标国家
2. 检索日期
3. 研究时间窗口
4. 本次实际查询的数据源
5. 当前榜单 / 当前头部样本
6. 高频题材与 Trope
7. 高频人物关系
8. 当前主要情绪价值
9. 上升信号
10. 饱和信号
11. 弱化 / 不确定信号
12. 市场机会
13. 本地文化备注
14. 3–5 个推荐创作方向
15. 数据可信度与局限
16. Evidence Ledger / 来源依据
```

Separate clearly:

```text
已验证的当前事实
vs.
基于当前数据做出的创作判断
```

Do not present an inference as a ranking fact.

---

# Failure behavior — never fill gaps with memory

If current information cannot be verified:

Say clearly:

```text
当前无法从可访问的实时来源确认这一排名 / 趋势。
```

Then either:

- use the freshest verified source and state its date, or
- mark the item as uncertain, or
- exclude the claim from decision-making.

Never do this:

```text
实时数据没查到
→ 用模型记忆中的旧榜单补上
→ 当成今天的数据继续写
```

That is a hard failure.

---

# Anti-copy rule

Never use one current title as the blueprint.

Good synthesis:

```text
current emotional pattern A
+
current relationship signal B
+
local social setting C
+
original protagonist D
+
new dramatic problem E
```

Bad synthesis:

```text
current Top 1 plot
+
new names
```

The purpose of live research is to identify current audience demand, not to clone a current hit.
