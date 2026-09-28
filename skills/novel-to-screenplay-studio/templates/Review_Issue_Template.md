# Review Issue Template

所有 Review Pass 共用的最小问题格式。

```yaml
review_issue:
  id:
  pass:
  priority: P0 | P1 | P2
  location:
  symptom:
  evidence:
  root_cause:
  impact:
  protected_elements:
  proposed_direction:
  dependencies:
  confidence: high | medium | low
  status: open | accepted | rejected | merged | fixed | deferred
```

## 规则

- 不允许只有“感觉不好”。
- 必须有具体证据。
- 修复方向不自动等于正式正典。
- 相同根因的问题应合并。
