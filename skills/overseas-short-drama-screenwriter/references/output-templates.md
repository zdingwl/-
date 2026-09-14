# 输出模板（中文主稿）

本文件统一规定所有可见交付物的默认语言和格式。

## 0. 强制语言规则

默认交付语言：**中文**。

即使目标市场是美国、英国、加拿大、澳大利亚等英语市场，以下内容仍默认用中文：

- 市场分析
- 创意方案
- 故事梗概
- 人物设定
- 人物关系
- 分集大纲
- 场景描述
- 动作描述
- 完整剧本正文

如果对白使用英语或其他外语，必须紧跟中文翻译。

禁止把“英文剧本”作为默认主稿。

---

## 1. 市场趋势摘要

```text
# 海外市场趋势摘要

目标国家：
目标语言：
目标平台：
目标观众：
研究日期：
研究周期：
数据来源：

## 当前头部作品 / 题材
- ...

## 高频题材与 Trope
- ...

## 高频人物关系
- ...

## 核心情绪价值
- ...

## 上升趋势
- ...

## 饱和趋势
- ...

## 潜在机会
- ...

## 本地文化注意事项
- ...

## 推荐创作方向
1. ...
2. ...
3. ...

置信度 / 数据限制：
...
```

## 2. Creative Brief

```yaml
creative_brief:
  target_country:
  target_language:
  target_platform:
  target_audience:
  genre:
  subgenre:
  tone:
  primary_emotion:
  secondary_emotion:
  audience_fantasy:
  current_market_signal:
  saturated_elements_to_avoid:
  opportunity_gap:
  protagonist_type:
  relationship_type:
  external_story_engine:
  differentiation:
  localization_notes:
  production_constraints:
  script_output_language: zh-CN
  dialogue_mode: chinese | bilingual | target-language-only
```

## 3. 创意池

```text
# 创意 01
中文暂定名：
英文暂定名：
类型：
目标观众：
一句话故事：
主角：
核心关系：
外部目标：
核心冲突：
核心秘密：
开篇 Hook：
最大反转：
情绪承诺：
连载发动机：
市场依据：
原创差异：
本地化优势：
评分：/100

# 创意 02
...
```

## 4. 项目 Bible

```text
# 项目基础

中文名：
英文名：
目标市场：
类型：
调性：
集数：
单集时长：

# Logline
...

# 核心戏剧问题
...

# 主题问题
...

# 观众情绪承诺
...

# 完整故事梗概
...

# 最终结局
...
```

## 5. 人物 Bible

```yaml
character:
  name_zh:
  name_original:
  age:
  nationality:
  city:
  profession:
  socioeconomic_position:
  public_identity:
  hidden_identity:
  external_goal:
  internal_need:
  fear:
  wound:
  flaw:
  strength:
  secret:
  leverage:
  false_belief:
  contradiction:
  opening_state:
  breaking_point:
  final_choice:
  ending_state:
  arc:
  speaking_style:
```

## 6. 人物关系 Bible

```yaml
relationship:
  character_a:
  character_b:
  surface_relationship:
  hidden_truth:
  what_a_wants:
  what_b_wants:
  attraction_or_dependency:
  power_balance:
  conflict_of_interest:
  unequal_information:
  breaking_point:
  transformation:
  final_state:
```

## 7. Story Engine

```text
# 关系发动机
...

# 外部目标发动机
...

# 秘密 / 信息发动机
...

# 反派发动机
...

# 为什么能够支撑目标集数
...
```

## 8. 全剧结构

```text
阶段 1 — 开篇扰动
涉及集数：
剧情功能：
重大事件：
关系状态：
信息状态：
阶段结尾：

阶段 2 — 被迫进入新局面
...

阶段 3 — 升级
...

阶段 4 — 重大反转
...

阶段 5 — 重大失败
...

阶段 6 — 反击
...

阶段 7 — 真相汇合
...

阶段 8 — 最终选择 / 高潮
...

阶段 9 — 情绪兑现
...
```

## 9. 分集大纲

```yaml
episode:
  number: 1
  title_zh:
  opening_state:
  opening_hook:
  protagonist_goal:
  obstacle:
  key_action:
  escalation:
  reveal_or_reversal:
  emotional_payoff:
  relationship_shift:
  cliffhanger:
  ending_state:
  next_question:
```

## 10. 单集 Beat Sheet

```text
# 第 XX 集

本集作用：
开篇 Hook：
核心戏剧问题：

Beat 1 — ...
原因：
行动：
结果：

Beat 2 — ...
原因：
行动：
结果：

Beat 3 — ...
...

情绪回报：
关系变化：
结尾 Cliffhanger：
连续性更新：
```

## 11. Scene List

```yaml
scene:
  id: E01-S01
  scene_heading_zh:
  characters:
  pov:
  goal:
  opposing_force:
  tactic:
  conflict:
  reveal:
  turn:
  value_before:
  value_after:
  result:
  exit_question:
```

## 12. 完整剧本 — 中文主稿（默认）

```text
第1集

场次 1
内景｜纽约 · 艾玛公寓｜夜

艾玛停在门口。

丹尼尔的皮鞋旁，放着一双陌生的红色高跟鞋。

卧室里传来女人压低的笑声。

艾玛
丹尼尔？

卧室里瞬间安静。

……

——第1集结束——
```

此格式为默认格式。

不要附加分镜、生图或视频提示词。

## 13. 完整剧本 — 中文主稿 + 英文对白对照

目标市场为英语国家、且项目需要英文对白时，使用：

```text
第1集

场次 1
内景｜纽约 · 艾玛公寓｜夜

艾玛停在门口。

一双陌生的红色高跟鞋，紧挨着丹尼尔的皮鞋。

艾玛（EMMA）
英文：Daniel?
中文：丹尼尔？

卧室门打开。

丹尼尔（DANIEL）
英文：Emma, I can explain.
中文：艾玛，我可以解释。

艾玛盯着他，没有进去。

艾玛（EMMA）
英文：Then start with her shoes.
中文：那就先解释一下她的鞋。
```

规则：

1. 场景标题用中文。
2. 动作描述用中文。
3. 人物说明用中文。
4. 英文对白先写符合当地口语习惯的自然英语。
5. 每句英文后立刻给中文翻译。
6. 中文翻译要准确传达情绪和潜台词，不要求逐词直译。
7. 不允许把整场英文对白集中到剧尾再翻译。
8. 不允许漏译任何外语台词。

## 14. 其他外语对白

如果目标语言是西班牙语、葡萄牙语、法语等，同样采用：

```text
角色名
西语：...
中文：...
```

或：

```text
角色名
葡语：...
中文：...
```

任何外语对白都必须有中文对照，除非用户明确要求纯外语发行稿。

## 15. Continuity Update

每集结束后维护：

```yaml
continuity_update:
  episode:
  current_time:
  character_locations:
  injuries:
  possessions:
  relationship_changes:
  new_information_by_character:
  secrets_revealed:
  setups_planted:
  setups_paid:
  unresolved_questions:
  legal_or_financial_changes:
  supernatural_rule_changes:
```

## 16. 修改报告

```text
# 剧本修改报告

总评分：/100

## 最强部分
- ...

## 最弱部分
- ...

## 结构问题
- ...

## 人物问题
- ...

## 单集 / 留存问题
- ...

## 对白问题
- ...

## 本地化问题
- ...

## 连贯性问题
- ...

## 原创风险
- ...

## 外语对白翻译遗漏
- ...

## 已完成修改
- ...

## 剩余风险
- ...
```

## 17. 完整项目交付包

默认：

```text
01 海外市场趋势摘要
02 Creative Brief
03 原创创意池
04 最终选题
05 完整故事梗概
06 人物 Bible
07 人物关系 Bible
08 Story Engine
09 全剧结构
10 完整分集大纲
11 Episode Beat Sheets
12 完整中文主剧本
13 英文 / 外语对白逐句中文对照（存在外语时）
14 Continuity Bible
15 修改 / 质量报告
```

用户如果只要求“完整剧本”，只交付完整剧本即可，不要强迫展示全部规划文档。

## 18. 权威版本规则

默认情况下：

> **中文主剧本是用户审阅和后续制作的权威版本。**

外语对白用于目标市场语言真实性，但必须保留中文翻译。

只有用户明确说“请给我纯英文最终发行稿”时，纯英文版本才可单独交付。
