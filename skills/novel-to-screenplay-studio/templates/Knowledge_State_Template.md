# Knowledge State Template

```yaml
knowledge_state:
  - character:
    current_unit:
    knows:
      - fact:
        learned_at:
    does_not_know:
      - fact:
    falsely_believes:
      - belief:
        source:
    suspects:
      - suspicion:
        confidence:
    newly_learned:
      - fact:
        learned_at:
    cannot_know_yet:
      - fact:
        reason:
```

## 核心规则

角色只能依据自己当时已知、误信或怀疑的信息行动。
