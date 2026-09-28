# Screenplay Studio 中文使用手册

## 1. 从零原创

示例：

“用 screenplay-studio 帮我从零写一部 110 分钟悬疑电影。核心设定是……”

Skill 会先内部建立 Story Contract、人物和结构，最终进入完整场景正文。

## 2. 从故事写剧本

示例：

“我给你一个故事梗概，把它写成 8 集剧集。”

普通体量直接用 story-to-screenplay。

如果是几十万字 / 百万字小说，先让 novel-to-screenplay-studio 整理源素材，再回本 Skill 写剧本。

## 3. 直接写某一场

示例：

“这是前情，直接写第 12 场：女主第一次发现父亲在说谎。”

此时不需要重新输出全局大纲，只读取必要状态后写场景。

## 4. 重写已有剧本

示例：

“先做 Script Doctor，找 P0/P1 根问题，再给 Rewrite Plan，最后直接重写。”

默认先修结构和人物，不拿对白润色掩盖根问题。

## 5. 写短剧

示例：

“给我写 60 集都市复仇短剧。”

仍使用 screenplay-studio，但切到 short-drama 工作流。

如果明确要求海外国家市场、本地化与当前平台趋势，再加载 overseas-short-drama-screenwriter。

## 6. 三个 Skill 的边界

- screenplay-studio：真正写剧本
- novel-to-screenplay-studio：大体量小说/IP的源素材整理与改编设计
- overseas-short-drama-screenwriter：海外短剧市场、本地化与竖屏专项

## 7. 下游边界

默认不自动进入：
- 分镜
- 摄影镜头
- 生图提示词
- 视频提示词

用户明确要求后再进入下游 Skill。
