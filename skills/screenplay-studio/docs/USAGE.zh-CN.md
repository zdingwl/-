# Screenplay Studio 2.0 中文使用手册

## 1. 最简单的用法

你不需要先告诉它“用原创模式”或“用小说改编模式”。

直接说你的目标即可。

例如：

> 把这部小说改成 8 集流媒体剧，完整读取后直接做完。

或：

> 从零写一部 110 分钟犯罪悬疑电影，直接从概念开发到剧本正文。

Skill 会自动判断：

- 原创还是改编
- 素材规模
- 电影、剧集、短剧还是动画
- 当前需要开发、写正文还是重写
- 是否需要长篇 Source Ingestion

---

## 2. 小说 / 网文 → 剧本

### 普通体量

示例：

> 把下面这个 2 万字故事改成电影剧本。可以合并配角，但保留结局和母女关系。

Skill 会自动：

1. 提取 Story DNA
2. 做 KEEP / TRANSFORM / MERGE / MOVE / CUT / INVENT
3. 外化内心戏
4. 重建影视因果
5. 做结构和 Scene Map
6. 写完整剧本

### 长篇 / 百万字 / 多文件

示例：

> 我会给你一部长篇小说的全部章节。先完整读取，不要读前几章就开始改。建立 Source Index、人物关系、时间线、秘密、伏笔和 Story Bible，再改成 12 集剧集。

长篇模式会先执行：

~~~text
目录扫描
→ 分块读取
→ Source Index
→ Canon / Timeline / Knowledge State
→ 关键段深读
→ Story DNA
→ Adaptation Matrix
→ 影视结构
→ 剧本正文
~~~

不要要求“一章一集”。

---

## 3. 从零原创

示例：

> 从零写一部科幻悬疑电影。一个记忆修复师发现自己的童年记忆是客户的非法备份。

Skill 会内部完成：

- Project Contract
- Logline
- Audience Promise
- Story Contract
- 人物与关系
- Story Engine
- Ending State
- Sequence
- Scene Map

如果你说“直接写剧本”，它最终必须进入场景正文，不会只停在大纲。

---

## 4. 写剧集

示例：

> 设计并写一季 8 集都市犯罪剧。每集 45 分钟。

剧集模式重点维护：

- Series Engine
- Season Question
- Episode Function
- A/B/C Lines
- 人物长期关系
- 每集 End State
- Story Bible
- Character Knowledge

不是把一部长电影拆成 8 份。

---

## 5. 写短剧

示例：

> 写 60 集复仇短剧，每集 1–2 分钟，不要机械每集反转。

短剧模式强调：

- 快速进入具体处境
- 单集目标
- 反制
- 状态变化
- 小兑现
- 新后果
- 连续观看驱动力

如果你明确要求某个国家、平台、当前热门题材或商业趋势，再使用海外短剧专项与实时资料。

---

## 6. 只写一场戏

示例：

> 这是前情。直接写第 23 场：女主在父亲葬礼后第一次质问母亲。

Skill 不会强迫重新输出整部结构。

它会读取必要前情，建立当前 Scene Contract，然后直接写：

- Scene Heading
- Action
- Character
- Dialogue
- Turn
- Consequence

---

## 7. 重写已有剧本

示例：

> 这版剧本中段很拖。先找根因，然后直接重写相关场次。

默认诊断顺序：

~~~text
Premise
→ Story Engine
→ 主角主动性
→ 对抗
→ Stakes
→ 因果
→ 人物弧
→ 关系
→ 结构
→ 场景
→ 信息
→ 对白
→ 连续性
→ 格式
~~~

不会优先用“台词更漂亮”掩盖结构问题。

---

## 8. 如何指定忠实度

可以直接说：

- “高忠实改编，主要事件与结局不要动。”
- “功能忠实，保留人物、情绪和主线，允许合并支线。”
- “自由改编，只保留核心设定和关系。”

对应：

- high
- functional
- free

---

## 9. 如何让它少问问题

直接说：

> 非关键缺失你自己做合理假设并标记 ASSUMED，不要逐步确认，直接推进。

Screenplay Studio 2.0 本身也默认采用这个原则。

---

## 10. Level 2 深度模式

如果你觉得结果“表面都对，但就是不好看”，可以说：

> 用 Level 2 深度诊断，不要只按知识清单检查，找到根因。

此时 Skill 会按问题加载：

`references/knowledge-level2/`

每个知识点包含：

- 定义
- 机制
- 诊断
- 常见失败
- 修复动作

---

## 11. 最推荐的完整指令

### 长篇小说改剧集

> 使用 screenplay-studio。完整读取我提供的全部小说素材，不要根据前几章猜后文。先建立 Source Index、Timeline、Character Knowledge、Setup/Payoff、Story DNA 和 Adaptation Matrix，再设计 8 集结构并写完整剧本。非关键缺失自行合理假设并标记 ASSUMED，不要逐步向我确认。最后做一次结构、人物、场景、对白和连续性诊断后统一重写。

### 从零原创电影

> 使用 screenplay-studio。从这个概念直接开发成完整电影剧本。内部完成 Story Contract、人物弧、Story Engine、Sequence、Scene Map 和 Story Bible，但不要把中间规划当最终结果。最终必须给到标准场景正文和完整对白，并做一次 Script Doctor 后统一重写。
