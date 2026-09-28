# 人物关系网络抽取

目标：从长篇源素材中的真实互动生成关系网络，而不是只根据身份标签推断。

---

# 1. 关系边（Edge）来自事件

每次重要互动记录：

```yaml
relationship_event:
  unit:
  character_a:
  character_b:
  context:
  a_goal:
  b_goal:
  action:
  counter_action:
  power_before:
  power_after:
  trust_before:
  trust_after:
  dependency_added:
  conflict_added:
  secret_involved:
  irreversible_change:
```

---

# 2. 关系不是身份

“母女 / 情侣 / 同事 / 敌人”只是标签。

真正要追踪：

- 信任
- 权力
- 依赖
- 欲望
- 债务
- 秘密
- 恐惧
- 共同目标
- 利益冲突

---

# 3. 多次互动合并

相同人物对出现多次时：

```text
按时间排序事件
→ 标记关键转折
→ 删除重复无变化互动
→ 形成关系弧
```

输出：

```yaml
relationship_arc:
  a:
  b:
  start_state:
  key_turns:
  midpoint_state:
  rupture_or_peak:
  final_state:
  unresolved_tension:
```

---

# 4. 关系重要度

优先级参考：

```text
是否影响主线
是否改变主角选择
是否承担主题
是否持有核心秘密
是否制造持续阻力
是否决定结局
```

不按“出场次数”机械判断重要度。

---

# 5. 合并角色前使用关系网

如果两个配角拟合并，先检查：

- 是否分别连接主角不同价值体系
- 是否分别掌握不同秘密
- 是否分别承担不同关系功能
- 合并后是否制造不可能的知识状态

---

# 6. 输出到 Relationship Map

最终只保留：

- 当前关系状态
- 关键历史
- 转折事件
- 权力变化
- 信任变化
- 未解决冲突
- 最终状态

不要把每次聊天都写进关系图。
