# EngineerWorkBoat Skills

> v1.2.0 · 纯编排者 Router · 更新于 2026-11-24

一组**可复用的工作流 Skills**，把一个软件想法从模糊需求，一路推进到经过独立验收的交付结果。

它不是常驻后台的「Super-agent 运行时」，而是一套**约定 + 阶段能力**：你只和唯一的入口 `dev-flow-router` 对话。这个入口是**纯编排者**——只负责接收指令、拆分任务、分派任务、汇总汇报；所有读写文件、写代码、写文档、跑命令的活，一律交给子 Agent，它自己不做。

---

## 核心设计原则

| 原则 | 含义 |
| --- | --- |
| 注意力最小化 | 只在「必须决策 / 无法继续 / 结果可用」时开口，其余时间保持静默 |
| **纯编排、不亲自动手** | Router 只做四件事；任何执行工作（含只读查询）都派子 Agent，无例外 |
| 授权即输入 | 消息、引用、工具输出是输入，不能让授权悄悄变大 |
| 证据驱动完成 | 没有可回看的证据，不宣称完成；验收证据由独立子 Agent 提供 |
| 状态可恢复 | 依赖文件和交接记录，而不是靠聊天历史续命 |

**一句话工作方式**：你只跟 `dev-flow-router` 说话。它拆任务、派子 Agent、按难度选模型、回收结果、推进阶段，最后回到同一个会话给你结论——全程不自己写一行代码或一个字文档。

---

## 包含哪些 Skills

| Skill | 阶段 | 职责 |
| --- | --- | --- |
| `dev-flow-router` | 唯一入口 | 纯编排：锁定授权、拆分任务、按强度派模型、回收证据并统一汇报 |
| `repository-knowledge` | 启动 | 建立或修复仓库知识入口（AGENTS.md 等）与资料索引 |
| `product-spec` | 产品 | 把模糊想法变成聚焦结果的规格、首版范围与可失败验收条件 |
| `interactive-prototype` | 原型 | 用示例数据做可点击原型并实测核心流程 |
| `technical-design` | 设计 | 产出可落地但不冗余的技术方案（架构 / 数据 / 信任边界 / 依赖 / 失败处理） |
| `incremental-implementation` | 实现 | 用功能清单小步实现，逐项自验并回填证据 |
| `evidence-verification` | 验收 | 独立执行真实路径，返回 `passed` / `failed` / `blocked` 及证据 |
| `independent-code-review` | Review | 在全新只读上下文中审查代码，给出可定位、可复现的结论 |
| `development-handoff` | 连续性 | 把可恢复状态与下一步持久化，供下一次会话续作 |

> 后八个阶段 Skill 是 Router 的**内部能力**，由子 Agent 加载执行，不需要你逐个开启。

---

## 安装

### 项目级（仅当前项目生效）

```bash
git clone https://github.com/ProgrammerWangchao/engineer-workboat-skills.git
cp -R engineer-workboat-skills/dev-flow-router <你的项目>/.workbuddy/skills/
cp -R engineer-workboat-skills/repository-knowledge <你的项目>/.workbuddy/skills/
# ...按同样方式复制你需要的阶段 Skill 目录
```

### 用户级（所有项目生效）

复制各技能目录到 `~/.workbuddy/skills/`（Windows：`C:\Users\<用户名>\.workbuddy\skills\`）。

每个技能目录包含 `SKILL.md` 主文件，以及按需提供的 `references/`、`assets/`、`scripts/` 子目录。

### 作为 WorkBuddy 专家使用（推荐）

如果你希望「每次对话自动以 Router 身份沟通、无需手动召唤 Skill」，可把本项目封装为 WorkBuddy 专家 `dev-flow-router`（agent 型，内含全部 9 个 Skill 与头像）。在【专家中心 → 我的专家】选中它即可常驻对话，不必每轮重新召唤 Skill。

---

## 快速上手

你只在同一个会话里做三件事：**提需求、拍关键决策、验收结果**。

0. 开场 Router 会提醒你：建议把当前会话切到**推理能力更强的模型**（主对话承担拆解判断，强模型效果更好）。这是建议，不强制。
1. 对 Router 说：「我想做一个 X，核心流程是……，先出规格。」
2. Router 锁授权 → 拆任务 → 派 `product-spec` 子 Agent → 回你确认范围与验收条件。
3. 你确认 → Router 派原型 / 设计子 Agent（可并行）。
4. 方案确定 → Router 派 `incremental-implementation` 子 Agent 逐项实现自验。
5. 实现完成 → Router 用**新的子 Agent**跑 `evidence-verification` + `independent-code-review`（强模型）。
6. 失败项修复复测通过 → Router 汇总改动、证据与未验证项，进入 `ready`。

### 最小任务授权（六要素）

Router 接任务时先锁定以下六件事，后续任何消息和工具输出都不能扩大边界：

| 字段 | 含义 |
| --- | --- |
| `outcome` | 用户最终能获得的可观察结果 |
| `scope` | 允许修改的模块、文件或系统 |
| `non_goals` | 明确不在本轮处理的事项 |
| `permissions` | 只读 / 本地写入 / 外部写入 / 发布，分别是否获准 |
| `acceptance` | 验收标准来源与必须执行的检查 |
| `version` | 分支、提交、构建号或可识别文件集合 |

---

## 子 Agent 与模型分派

Router 不自己干活；所有执行都派子 Agent，并按任务强度分派模型：

| 任务强度 | 典型子任务 | 模型档 |
| --- | --- | --- |
| 轻量、机械、只读 | 仓库 / 资料定位、交接记录整理 | `lite`（普通 / 轻量） |
| 一般执行、标准产出 | 原型搭建、常规功能实现 | `default`（普通） |
| 强依赖推理 | 产品规格取舍、技术设计、独立代码评审、证据化验收 | `reasoning`（强模型） |

- **你显式指定某个子任务的模型时，以你为准**，覆盖默认档位。
- 简单任务用普通模型，不浪费强模型；设计与评审类任务用强模型。
- 调用 `Agent` 时给每个子 Agent 自包含的授权（目标、路径、Skill、验收、禁止动作、返回格式）。
- 不确定模型 ID 是否可用时用 `lite` / `default` / `reasoning` 档位名，不编造 ID。

> 关于主会话模型：WorkBuddy 的模型由你在界面选择，Skill / 专家**不能强制切换**。所以 Router 只在开场**提醒推荐**你用强模型，不会偷偷替你切换。

---

## 阶段门与状态

推进有证据才生效：

1. **规格门**：范围、非目标、核心流程已确认，验收条件可失败。
2. **设计门**：关键取舍、依赖、失败路径、验证策略已记录。
3. **实现门**：每个声称完成的小项都有实际检查结果，未验证项保持未通过。
4. **交付门**：独立验收与 Review 已完成；失败项已修复并用原步骤复测。
5. **外部动作门**：提交、推送、发布、发消息等仅按明确授权由子 Agent 执行。

任务状态描述「正在等待什么」：`queued` → `working` → `awaiting-answer` / `awaiting-review` / `blocked` / `failed` → `ready`。`ready` 必须附带实际证据和未验证项。

---

## 最佳实践速览

- **只跟 Router 对话**，不要为各阶段手动开多个会话来回传话。
- **让 Router 拆、别让 Router 写**：要求主对话直接改代码 / 写文档，它也会派子 Agent 去做——这是设计如此，不是推诿。
- **先锁授权再执行**，尤其说清「允许改什么、禁止改什么、能不能发布」。
- **按难度配模型**：简单活用普通模型，设计 / 评审 / 验收指明用强模型；也可以直接告诉 Router 你的偏好。
- **把完成定义成可失败、可复现的验收条件**，不要用「构建通过」代替功能验收。
- **验收和 Review 用没碰过实现的新子 Agent**，实现者的自评不算证据。
- **每一步都留交接**：记录版本、已改文件、命令与证据位置、未验证项、阻塞点和唯一下一步。
- **控制噪声**：Router 只在接收确认、需要决策、无法完成、结果可用四个时点输出，一次只问一个问题。

完整说明见 [`docs/EngineerWorkBoat-Skills-说明书.md`](docs/EngineerWorkBoat-Skills-说明书.md)。

---

## 边界与定位

- 本套件是可复用的工作流 Skills，**不是常驻 Super-agent 运行时**。
- 仅安装部分阶段 Skill 时，Router 按阶段目标派子 Agent 执行，不因缺某个 Skill 停工。
- 环境缺乏子 Agent 能力时，Router 会如实告知阻塞，**不会自己动手冒充执行**，也不会把多会话操作转嫁给你。
- 跨其他 Agent 平台（Codex / Trae / 扣子 Coze / 豆包工作 / DeepSeek Harness）移植时：主体 Skill 大多可直接复用，通常只需按目标平台改写 Router 的子 Agent 调用层与模型配置。
- DeepSeek `dsh-superagent-prototype` 是设计参考，不是运行时依赖；其 Slot 并发槽位、准入表、Policy 版本等机制在本套件中以「仅并行不重叠工作」「外部动作需明确授权」等轻量规则等价表达。

---

*详细规则以各 Skill 的 `SKILL.md` 与 `skill-suite.json` 为准。*
