# WorkBuddy Skills

WorkBuddy `EngineerWorkBoat` 项目使用的开发流程 Skills 集合。

## 包含的技能

| 技能 | 用途 |
| --- | --- |
| `dev-flow-router` | 开发流程统一入口，按任务类型路由到对应技能 |
| `development-handoff` | 持久化与恢复可续接的开发交接上下文 |
| `evidence-verification` | 独立验证规格中的具体需求是否实现 |
| `incremental-implementation` | 小步增量实现软件变更 |
| `independent-code-review` | 对具体代码变更做独立审查 |
| `interactive-prototype` | 构建并验证轻量交互原型 |
| `product-spec` | 把模糊的软件想法转成产品规格 |
| `repository-knowledge` | 生成或修复仓库知识文档 |
| `technical-design` | 产出可落地的技术方案 |

## 安装

### 项目级（仅当前项目生效）

```bash
git clone https://github.com/ProgrammerWangchao/engineer-workboat-skills.git
cp -R engineer-workboat-skills/* <你的项目>/.workbuddy/skills/
```

### 用户级（所有项目生效）

复制技能目录到 `~/.workbuddy/skills/`（Windows：`C:\Users\<用户名>\.workbuddy\skills\`）。

## 说明

每个技能目录包含 `SKILL.md` 主文件，以及按需提供的 `references/`、`assets/`、`scripts/` 子目录。
