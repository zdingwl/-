# Story / Novel Input Adapter

## 定位

只负责把“非剧本叙事素材”转成可以进入 screenplay-studio 的戏剧信息。它不是主流程。

## 输入

小说、网文、故事梗概、人物小传、真实事件、新闻素材、口述经历、世界观设定、旧版本故事。

## 第一步不是缩写

先提取：

~~~yaml
source:
  protagonist:
  wants:
  obstacles:
  irreversible_events:
  key_relationships:
  secrets:
  reversals:
  emotional_highs:
  thematic_conflicts:
  ending:
  must_keep:
~~~

## 元素决策

~~~yaml
decision:
  element:
  source_function:
  screen_function:
  status: KEEP | TRANSFORM | MERGE | MOVE | CUT | INVENT
  reason:
  consequence:
~~~

## 内心戏

优先转成可见选择、行为反差、谎言、犹豫、对话策略、物件处理、关系距离、对照场景和后果，而不是自动变旁白。

## 人物合并

多个配角功能重复时允许合并；判断是否提供相同信息、推动同一层欲望、删除后情感价值是否几乎不变。

## 时间重排

影视版可以改变揭露顺序，优先服务戏剧问题、信息差、人物主动性、关系升级、悬念和情绪兑现。

## Chapter != Scene != Episode

~~~text
章节内容
→ 戏剧功能
→ 因果事件
→ Sequence
→ Episode / Act
→ Scene
~~~

## 大体量小说

多卷、数十万/百万字、多文件、多 POV、大量伏笔、复杂时间线：先调用 novel-to-screenplay-studio 做 Source Index / Story Bible / Adaptation Matrix，再回 screenplay-studio 写剧本。
