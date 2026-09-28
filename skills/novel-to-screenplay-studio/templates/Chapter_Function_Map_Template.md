# Chapter Function Map Template

本模板用于判断原作章节在影视版中的功能，而不是直接映射集数。

```yaml
chapter_function:
  source_chapter:
  pov:
  primary_function:
    - plot
    - character
    - relationship
    - world
    - mystery
    - setup
    - payoff
    - transition
  major_event:
  irreversible_choice:
  information_value:
  emotional_value:
  visual_value:
  dependency_on_previous:
  dependency_on_later:
  removable_without_damage: true | false
  merge_candidates:
  screen_decision: KEEP | TRANSFORM | MERGE | MOVE | CUT
  target_sequence_or_episode:
```

## 映射规则

影视单元由“戏剧功能和因果”决定，不由章节编号决定。
