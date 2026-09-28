# Genre Engine

类型不是标签，而是观众进入作品时的一组“体验承诺”。

本文件用于把通用 Story DNA 转成类型专属 Story Engine。

---

# 1. 类型路由

```yaml
genre_contract:
  primary_genre:
  secondary_genre:
  audience_promise:
  central_question:
  required_payoffs:
  acceptable_delays:
  forbidden_shortcuts:
  climax_expectation:
  ending_expectation:
```

主类型决定核心承诺，次类型只能增强，不能把主承诺吞掉。

---

# 2. 类型模块

按需要读取：

- Romance → `genres/romance.md`
- Mystery → `genres/mystery.md`
- Thriller / Horror → `genres/thriller-horror.md`
- Comedy → `genres/comedy.md`
- Crime / Legal → `genres/crime-legal.md`
- Family / Emotional Drama → `genres/family-drama.md`
- Fantasy / Sci-Fi → `genres/fantasy-scifi.md`
- Revenge / High-satisfaction → `genres/revenge-high-satisfaction.md`
- Action / Adventure → `genres/action-adventure.md`

---

# 3. 类型承诺不是固定模板

例如 Romance 不等于：

> 两个人必须误会三次。

Mystery 不等于：

> 每集最后必须突然出现新线索。

Comedy 不等于：

> 不停讲笑话。

类型模块定义的是：

- 观众期待什么变化
- 什么信息可以延迟
- 什么必须阶段兑现
- 高潮必须回答什么

---

# 4. 混合类型

最多锁定：

```text
Primary Genre
+
Secondary Genre
+
可选 Tone
```

示例：

```text
Primary: Mystery
Secondary: Family Drama
Tone: restrained
```

不是把五种类型规则全部叠加。

---

# 5. Genre Drift

每个大阶段检查：

```text
观众最初为什么来看？
现在仍然在得到这种体验吗？
如果承诺改变，是有意转型还是无意识漂移？
```

---

# 6. Genre Payoff Ledger

```yaml
genre_payoff:
  promise:
  setup:
  expected_window:
  partial_payoff:
  major_payoff:
  final_payoff:
  status:
```

避免只不断承诺、不兑现。

---

# 7. 类型与人物

类型事件必须迫使人物选择。

差：

> 为了悬疑，加一个尸体。

好：

> 新尸体证明主角之前的判断可能害死了第二个人，迫使他改变策略。

---

# 8. 类型与改编

改编时区分：

- 原作类型标签
- 原作真实情绪发动机
- 目标影视媒介下的类型承诺

如果原作名义是爱情，真正驱动力却是身份秘密与复仇，不要机械只加载 Romance。

---

# 9. 类型验收

最终检查：

- 类型承诺是否清楚
- 关键阶段是否有回报
- 高潮是否属于这个类型
- 结局是否回答观众最核心期待
- 是否为了“类型感”加入无因果事件
