# Project State Template

> 只保存项目当前结论，不保存长篇推导。

```yaml
project_state:
  project_name:
  version:
  entry_mode: adaptation | original
  source_type:
  target_medium: feature | series | short_drama | animation
  target_scale:
  current_stage:
  current_unit:
  current_draft:
  last_updated:

  locked_decisions:
    - item:
      value:
      reason:

  assumed_decisions:
    - item:
      value:
      reason:

  proposed_decisions:
    - item:
      value:
      reason:

  rejected_decisions:
    - item:
      value:
      reason:

  current_goal:
  current_blocker:
  next_action:
```

## 使用规则

- LOCKED：不得擅改。
- ASSUMED：为了推进暂定，可后续修订。
- PROPOSED：候选，不进入正典。
- REJECTED：后续禁止重新混入。
- 每轮结束只更新发生变化的字段。
