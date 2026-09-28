# Genre Profiles

Genre Engine 主入口：

`../genre-engine.md`

当前模块：

- `romance.md`
- `mystery.md`
- `thriller-horror.md`
- `comedy.md`
- `crime-legal.md`
- `family-drama.md`
- `fantasy-scifi.md`
- `revenge-high-satisfaction.md`
- `action-adventure.md`

## 使用规则

1. 先锁 Primary Genre。
2. 必要时只加一个 Secondary Genre。
3. Tone 与 Genre 分开。
4. 不一次加载全部模块。
5. Genre 只定义观众承诺与 Story Engine，不取代人物、因果、媒介和正典。

示例：

```yaml
primary_genre: mystery
secondary_genre: family_drama
tone: restrained
```

此时 Mystery 控制核心问题链，Family Drama 强化关系与情绪，不把故事改成高爽或随机反转。
