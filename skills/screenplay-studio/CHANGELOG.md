# Changelog

## 2.0.0 — 2026-09-28

重大升级：把 screenplay-studio 收敛为唯一通用编剧主入口。

### Unified Routing

- 原创、小说/IP改编、已有剧本重写、单场写作统一进入 screenplay-studio。
- 新增 source_scale 自动判断。
- 长篇/多卷/多文件小说不再要求用户手动切换 Skill。

### Long-form Adaptation

新增：

- references/source-ingestion.md
- references/adaptation-engine.md
- workflows/long-novel-to-screenplay.md
- Source Index
- Character Knowledge
- Setup / Payoff Ledger
- Reveal Ledger
- Adaptation Matrix
- 长篇全局收敛门槛

### Knowledge Level 2

新增 120 个知识点逐条深度解析层：

- 定义
- 作用机制
- 诊断问题
- 常见失败
- 修复动作

采用按问题加载，而不是一次加载全部知识。

### Workflow

强化：

- Project State
- Story Bible
- LOCKED / ASSUMED / PROPOSED / REJECTED
- Scene Contract
- Output Contract
- Root-cause Script Doctor
- 用户要求“直接做完”时连续推进

### Skill Architecture

依据 OpenAI Skills 官方结构原则：

- SKILL.md 保持主路由与执行规则
- references/ 承载深层知识
- workflows/ 承载专项流程
- templates/ 承载状态与项目模板

### Installability & Validation

- 压缩主 `SKILL.md` 为调度器式入口，详细规则按需加载。
- 新增 `references/project-state-continuity.md`。
- 新增 `docs/INSTALL.zh-CN.md`。
- 新增确定性单 Skill ZIP 打包脚本 `scripts/package_skill.py`。
- 强化 `scripts/validate_skill.py`：检查唯一 SKILL.md、引用路径、120 点完整性、文件数量与单文件大小。
- GitHub Actions 每次主分支更新都会实际构建并打开 ZIP 做烟雾测试。
- 当前验证包：59 个文件，Level 2 为 120/120。

## 1.0.0 — 2026-09-28

首次建立 screenplay-studio 通用编剧主 Skill。
