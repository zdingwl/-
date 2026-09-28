# 方法来源与设计取舍

本文件用于维护 Skill 的设计依据。运行普通项目时不必加载。

---

# 1. OpenAI Skills 结构

OpenAI 对 Skills 的产品说明把 Skill 定义为可复用工作流，可包含：

- instructions
- examples
- supporting resources
- code / reusable steps（需要时）

因此本 Skill 使用：

```text
SKILL.md
+
references/
+
workflows/
+
evaluations/
```

而不是把所有知识塞进一个超长提示词。

---

# 2. 本仓库既有海外短剧 Skill

参考：

`../overseas-short-drama-screenwriter/`

继承的成熟部分：

- Story DNA
- 人物主动性
- Story Engine
- Narrative Momentum
- Scene Value Shift
- Dialogue as Action
- Voice Fingerprint
- Knowledge State
- Story Bible
- Script Doctor
- 独立质检
- 回归测试

本 Skill 的新增重点：

- 通用小说 / IP 改编
- 改编尺度
- Adaptation Matrix
- POV 重构
- 内心戏外化
- 人物 / 支线合并
- 时间线与 Reveal 重排
- 电影 / 剧集 / 短剧 / 动画媒介配置
- 通用原创剧本入口

---

# 3. 剧本格式的基础原则

采用通用行业共识：

- 场景标题标识内/外景、地点、时间
- 动作只写屏幕上可感知的内容
- 不把小说式心理叙述直接放进动作栏
- 人物名、对白、动作格式保持一致

格式只是可读性基础，不把任何一种软件排版规则当成戏剧质量本身。

---

# 4. 公开编剧 Skill 的既有融合

本仓库原有：

`../overseas-short-drama-screenwriter/references/craft-sources.md`

已经记录过多套公开编剧 Skill 的融合取舍，包括：

- 完整剧本流水线
- Story Structure
- Scene Craft
- Dialogue / Subtext
- Story Bible
- Continuity
- Critic → Rewrite
- Sound-off Test
- Anti-AI
- 长篇串行写作

本 Skill 不重复复制这些项目，而是把通用原则重新组织成“改编 + 原创”的统一系统。

---

# 5. 核心设计取舍

当不同方法冲突时：

```text
1. 用户明确要求
2. 已锁定正典
3. 原作核心情绪 / 功能（改编项目）
4. 因果与人物选择
5. 目标媒介
6. 场景与对白工艺
7. 结构模板
```

任何结构理论都只是工具。

---

# 6. 为什么不把 120 知识点全写进 SKILL.md

因为运行时最重要的是“阶段正确”。

如果每次同时加载：

- 改编
- 原创
- 电影
- 剧集
- 短剧
- 动画
- 场景
- 对白
- 连续性
- Script Doctor

模型容易：

- 规则互相打架
- 过度展示方法
- 机械套模板
- 忽略当前任务

因此：

```text
knowledge-map-120.md = 覆盖地图
SKILL.md = 路由
workflows/ = 执行顺序
references/ = 专项知识
evaluations/ = 防退化
```
