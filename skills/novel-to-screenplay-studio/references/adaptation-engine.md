# 改编引擎：小说 / IP / 素材 → 影视剧本

本文件处理“已有素材如何重新设计成能在屏幕上成立的剧本”。

核心判断：

> 改编不是压缩原文，而是把原作的功能、情绪和因果重新编码成影视语言。

---

# 1. 建立源素材索引

长篇素材不要直接从第 1 章开始改。

先建立：

```yaml
source_index:
  chapters_or_sections:
  timeline:
  major_events:
  characters:
  relationships:
  locations:
  world_rules:
  secrets:
  reveals:
  setups:
  payoffs:
  recurring_images:
  emotional_peaks:
```

目标是回答：

- 故事真正发生了什么？
- 谁导致了什么？
- 哪些事件只是文字篇幅，哪些是主因果？
- 哪些信息只有读者知道？
- 哪些东西在后文会回收？

---

# 2. Story DNA 提取

至少锁定：

```yaml
story_dna:
  protagonist:
  external_goal:
  internal_need:
  misbelief:
  inciting_event:
  dramatic_question:
  theme_question:
  core_relationship:
  opposing_force:
  stakes:
  primary_emotional_promise:
  central_secret:
  ending_state:
```

如果原作主线不清晰，不能机械忠实。

影视版必须找到一条更清楚的“观众跟随线”。

---

# 3. 改编尺度

## 3.1 高忠实

适合：

- 原作结构本身高度影视化
- 用户要求保留主要事件与结局
- IP 识别度高度依赖原有事件序列

允许调整：

- 场景顺序
- 信息释放
- 人物合并
- 内心戏外化
- 节奏压缩

## 3.2 功能忠实

保留：

- 核心人物
- 情绪承诺
- 主题问题
- 主线因果
- 标志性关系 / 转折

可以较大程度改变：

- 场景
- 支线
- 配角
- 时间顺序
- 揭密方式

## 3.3 自由改编

保留少数核心 DNA：

- 核心 premise
- 主题
- 关系
- 世界概念
- 关键意象

其余按目标媒介重建。

---

# 4. 改编决策矩阵

每个重要元素进入：

```yaml
adaptation_matrix:
  source_element:
  source_type: event | character | subplot | secret | location | motif | relationship
  original_function:
  emotional_value:
  plot_dependency:
  screenability:
  decision: KEEP | TRANSFORM | MERGE | MOVE | CUT | INVENT
  new_screen_function:
  affected_elements:
  risk:
```

## KEEP

只有当该元素同时具备高功能与高识别度时优先直接保留。

## TRANSFORM

保留功能，替换表达。

例：

小说：
> 她终于确认自己无法再相信丈夫。

影视：
- 她删除共享定位
- 把备用钥匙从钥匙圈拆下
- 在对方回家前换了门锁密码

## MERGE

合并功能重复元素：

- 两个消息传递者
- 两个相似竞争者
- 多个没有独立弧的亲属
- 重复承担阻力的事件

## MOVE

用于：

- 把后文最有力的冲突提前
- 延后过早暴露的秘密
- 把回忆拆散进入当前冲突
- 让某个 Reveal 在更高代价时发生

## CUT

删除后必须检查：

- 是否损伤核心关系？
- 是否破坏后续因果？
- 是否丢失 Setup？
- 是否让某个角色突然无动机？
- 是否失去原作情绪承诺？

## INVENT

允许新增：

- 因果桥梁
- 可见证据
- 决策场景
- 必要对抗
- 影视化动作
- 原作跳过但屏幕必须看到的后果

新增不是“乱加戏”，而是让影视版独立成立。

---

# 5. 内心戏外化工具箱

## 5.1 选择

最优先。

小说：
> 他已经不相信她。

影视：
> 她让他保管护照。他没接。

## 5.2 行为

变化通过反常或新的行为显示。

## 5.3 道具

常见：

- 戒指
- 钥匙
- 手机
- 合同
- 照片
- 药
- 钱
- 文件
- 衣物
- 旧物

重点不是“有象征”，而是人物如何使用它。

## 5.4 空间

- 坐近 / 坐远
- 进入 / 不进入
- 关门 / 留门
- 站在谁那边
- 谁拥有房间中心
- 谁被挡在外面

## 5.5 关系策略

心态改变会改变策略：

- 解释 → 试探
- 请求 → 交易
- 亲近 → 防御
- 服从 → 拒绝
- 隐瞒 → 主动暴露

## 5.6 对照

用“同一行为在前后两次不同”表达 Arc。

## 5.7 第三对象

当心理冲突太抽象，把它投射到：

- 孩子
- 病人
- 项目
- 共同财产
- 宠物
- 家族物件
- 一个必须共同完成的任务

## 5.8 声音

声音可以触发记忆和状态，但不要替代戏。

## 5.9 旁白

只有当旁白本身是形式策略时使用。

旁白不能承担：

> “因为我们不会把它戏剧化，所以让角色解释。”

---

# 6. POV 改编

小说可自由进入多人内心。

影视需要重新选择观众如何得到信息。

建立：

```yaml
pov_map:
  sequence:
  audience_follows:
  audience_knows:
  protagonist_knows:
  antagonist_knows:
  intentionally_withheld:
  dramatic_effect:
```

三种常见策略：

## 主观跟随

观众基本与主角同步。

优点：沉浸、悬疑。

风险：其他角色容易扁平。

## 优越信息

观众知道主角不知道的危险。

优点：制造 suspense。

## 分裂信息

不同人物掌握不同碎片。

优点：适合群像、悬疑、关系剧。

---

# 7. 时间线重构

小说可能：

- 多线并行
- 大量回忆
- 章节跳时
- 先果后因

影视版重排时问：

```text
这个信息现在给，观众会做出什么判断？
如果晚给，会产生悬疑还是困惑？
如果早给，会产生期待还是泄气？
它改变谁的策略？
```

不要只因“原作这里才讲”而保留位置。

---

# 8. 开篇重构

小说前若主要是：

- 世界观
- 家族史
- 童年
- 氛围
- 日常
- 解释

可以从更靠后的“不可忽视异常”进入。

但新开篇必须仍然属于这部作品，不得为了强刺激加入与核心无关的大事件。

开篇至少建立：

- 谁
- 当前处境
- 想要什么
- 哪里不对
- 为什么要继续看

---

# 9. 人物合并

合并前列出角色功能：

```yaml
character_function:
  name:
  information_function:
  emotional_function:
  conflict_function:
  plot_function:
  theme_function:
  unique_relationship:
```

可以合并：

- 功能重复
- 关系重复
- 只出现一次完成任务
- 没有独立后果

不能轻易合并：

- 承担不同主题立场
- 同时代表不同社会力量
- 对主角产生完全不同情感影响
- 后期各自承担关键因果

---

# 10. 支线压缩

一条支线至少应贡献多个价值：

```text
主线
关系
人物弧
主题
秘密
资源
对抗
Setup / Payoff
节奏
世界规则
```

如果只贡献“更多内容”，优先删或并。

---

# 11. 信息释放重构

建立 Reveal Ledger：

```yaml
reveal:
  information:
  source_version_location:
  audience_learns:
  protagonist_learns:
  other_characters_learn:
  before_reveal_belief:
  after_reveal_change:
  consequence:
```

强 Reveal 至少改变一项：

- 目标
- 关系
- 策略
- 风险
- 权力
- 身份
- 对过去的解释

---

# 12. 章节 → 影视结构

禁止：

```text
第 1 章 = 第 1 集
第 2 章 = 第 2 集
```

正确顺序：

```text
提取完整因果
→ 找大阶段
→ 找不可逆节点
→ 重建段落 / 集结构
→ 再决定场景边界
```

章节结束往往是阅读节奏；
场景和集结束必须是戏剧状态变化。

---

# 13. 事件“影视化强度”判断

高优先：

- 决策
- 公开冲突
- 关系变化
- 身份暴露
- 证据出现
- 资源得失
- 权力变化
- 可视化动作
- 不可逆后果

低优先：

- 重复心理
- 纯解释
- 无影响日常
- 功能重复对话
- 不改变主线的支线

---

# 14. 标志性元素保护

如果原作具有：

- 标志性场景
- 标志性物件
- 核心台词概念
- 独特关系
- 独特世界规则
- 结局意象

不要为了“更标准”轻易抹平。

改编的目标不是把所有作品变成同一种工业模板。

---

# 15. 新增场景规则

新增场景必须回答：

```text
它修复了哪个屏幕问题？
它让什么因果成立？
它替代了哪段不可影视化文字？
它改变了什么？
如果删掉，会损失什么？
```

如果答不出来，不新增。

---

# 16. 改编 Scene Map

```yaml
adapted_scene:
  id:
  source_origin:
  source_elements_used:
  purpose:
  protagonist_goal:
  obstacle:
  turn:
  visible_externalization:
  reveal:
  relationship_change:
  consequence:
  adaptation_decision:
```

这样可以追溯：

> 影视版这一场为什么存在，它来自原作的什么功能。

---

# 17. 改编完整性检查

```text
□ 原作最重要的情绪承诺还在
□ 核心人物关系没有被误删
□ 影视版主角目标更清楚
□ 内心戏已被外化
□ 角色数量经过功能审查
□ 支线经过价值审查
□ 章节没有机械对应场次/集数
□ 信息释放经过重新设计
□ 新增内容解决真实影视问题
□ 删除内容没有破坏后续因果
□ 高潮仍回应原作核心
□ 影视版即使不读小说也能独立理解
```

最终判断：

> 既不能“忠实得不能看”，也不能“好看但已经不是这部作品”。
