# Source Ingestion — 长篇 / 多卷 / 多文件小说读取

适用于几十万字、百万字、多卷、多文件、系列小说与复杂 IP。

核心原则：

> 先建立可检索的全局事实模型，再做改编判断。不要边读前文边正式改写。

## 1. 三层读取

### Layer 1：目录扫描

先获得：

- 文件
- 卷
- 章节
- 顺序
- 体量
- 可用元数据

输出 Source Manifest。

### Layer 2：功能索引

每章/每段提取：

- POV
- 剧中时间
- 地点
- 出场人物
- 重大事件
- 人物选择
- 后果
- 关系变化
- 新信息
- 秘密状态
- Setup / Payoff
- 情绪价值
- 新资源/证据/伤势

写入 Source Index。

### Layer 3：关键段深读

根据索引二次深读：

- 触发事件
- 关键关系转折
- 不可逆选择
- 中段
- 重大 Reveal
- 高潮
- 结局
- 人物弧证明
- 重复意象与物件
- 后文重解释前文的位置

## 2. Chunk 不是故事单元

分块只是上下文管理。

禁止：

- 每块单独总结后直接拼接总纲
- 每读一块就锁定一个影视集
- 前几章没读完就猜结局
- 忽视后文对前文的推翻
- 把章节标题误当戏剧功能

每完成一个 Chunk，只更新全局状态。

## 3. 增量合并

~~~text
新事实
→ 去重
→ 与 Canon 冲突检查
→ 更新时间线
→ 更新人物状态
→ 更新关系
→ 更新秘密
→ 更新 Character Knowledge
→ 更新 Setup / Payoff
→ 标记待验证假设
~~~

待验证内容只能标记 ASSUMED。

## 4. Character Knowledge

每个关键人物维护：

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

这一步决定悬念、误解与对话是否成立。

## 5. Relationship Events

重要互动记录：

~~~yaml
interaction:
  a:
  b:
  event:
  a_goal:
  b_goal:
  power_before:
  power_after:
  trust_before:
  trust_after:
  dependency_change:
  conflict_change:
  secret_involved:
~~~

不要根据“亲属 / 情侣 / 同事”标签直接推断实际关系状态。

## 6. Setup / Payoff

~~~yaml
setup_payoff:
  setup:
  source_location:
  apparent_function:
  actual_function:
  payoff:
  payoff_location:
  status: open | partial | paid | abandoned
~~~

若后文证明某伏笔是假线索，也要记录其真实功能。

## 7. 全局收敛条件

满足后才进入 Adaptation Design：

~~~text
□ 主线因果可追踪
□ 主要角色功能已知
□ 结局已读取
□ 核心秘密与 Reveal 顺序已知
□ 时间线无重大空白
□ 关键 Setup / Payoff 已索引
□ 后文是否重解释前文已检查
□ 核心情绪承诺可说明
□ 主要人物 Knowledge State 可追踪
~~~

否则继续读取源素材。

## 8. 读取完成后的交接对象

不要输出“章节总结堆”。

应形成：

- Source Manifest
- Source Index
- Canon Ledger
- Timeline
- Character Function Map
- Relationship Map
- Character Knowledge
- Setup / Payoff Ledger
- Reveal Ledger
- Emotional Peaks
- Story DNA 候选
- Adaptation Risks

这些才是下一步改编设计的可靠输入。
