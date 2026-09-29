# Changelog

## 2.1.0 — 2026-09-29

新增“生存灾难 / 重生 / 系统 / 长线连载”逻辑层，来源于实际第一季剧本重构中暴露出的上游问题。

### Speculative Survival Logic

- 新增 `references/speculative-survival-serial-engine.md`。
- 灾难默认按预警、城市功能停摆、供应链危机、社会冲突、生态异常、虚构机制显现、长期失守逐级演化。
- 明确现实科学与虚构突破的边界，禁止用模糊科学词直接解释极端快速变化。
- 强化重量、体积、采购、运输、仓储、消耗与维护检查。

### Rebirth & System Logic

- 重生必须提供可兑现的前期信息优势，同时限定知识来源。
- 新增 Future Knowledge 与 Timeline Divergence；改变过去后旧情报必须衰减。
- 战略能力默认隐藏，首次曝光必须有必要性与代价。
- 新增 Capability Ledger，禁止系统临时新增无前置救场能力。
- 升级必须由真实资源 / 模块 / 条件驱动，并增加维护成本或暴露风险。

### Opposition & Serial Logic

- 主角成长必须制造新的利益冲突与对手反制。
- 引入 Opposition Ladder，区分亲属小人、掠夺者、地方势力、战略组织与世界级对抗。
- 主角不能长期无损获胜，重大损失必须持续影响后续。
- 新增 Episode / Arc / Season / Saga 四层 Hook。
- 第一季不应一次解释系统来源、全部灾难真相和所有幕后势力。

### Project State

- 新增 `templates/Serial_Survival_State_Template.md`。
- Project State 增加 World Phase、Resource / Capability Ledger、Secrecy / Exposure、Faction Interest、Open Hooks、Future Payoffs、Season Residue。
- Script Doctor 与 Short Drama / Series 工作流同步增加对应检查。
- 校验脚本把新增 reference 与 template 列入必需文件。

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
