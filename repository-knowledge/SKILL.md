---
name: repository-knowledge
description: "Create or repair a concise repository knowledge entry such as AGENTS.md and map product specs, design documents, execution plans, references, and handoffs. This skill should be used when starting work in a new repository, when agents cannot find project rules or documents, or when repository knowledge has become duplicated or stale."
agent_created: true
---

# Repository Knowledge

## Purpose

把仓库知识组织成可发现、可恢复的记录系统。让 `AGENTS.md` 成为短索引，而不是堆积全部历史、需求与临时讨论。

## 1. 先调查再修改

1. 读取现有 `AGENTS.md`、README、架构说明、文档目录、进度记录和项目级规则。
2. 检查 Git 状态与当前工作区改动，保留用户已有工作。
3. 识别已有 MEMORY、Resources、Wiki 或其他知识组织方式，优先沿用并说明映射，避免维护两份同一内容。
4. 已有 `AGENTS.md` 时先给出具体调整范围；覆盖或重组前取得确认。
5. 没有 Git 仓库时说明拟初始化的位置并等待确认；不要自动创建分支、提交、推送或连接远程。

## 2. 建立短入口

使用 [assets/AGENTS.template.md](assets/AGENTS.template.md) 作为结构参考，只保留实际有用的部分：

- 项目目标与当前产品边界。
- 少量长期适用的工程规则。
- 真实存在的规则、规格、设计、计划和交接位置。
- 不同任务应先读取哪些资料。
- 后续文档的存放约定。

只链接真实存在的文件。未来位置写成约定，不伪装成已有链接，也不批量创建空目录和空文档。详细内容放入对应资料，不复制进 `AGENTS.md`。

## 3. 保持来源与状态清晰

- 将原始资料保持原样，整理结果保留来源链接。
- 将已确认决定、临时建议和待确认问题分开。
- 将详细需求放入产品规格，技术取舍放入设计文档，执行进度放入计划或交接。
- 不写入密钥、账号口令、个人敏感信息或短暂工具输出。
- 不在知识整理阶段顺手确定技术框架、支付、账号、部署等未确认方案。

## 4. 验证入口

1. 逐个检查入口中的相对链接和路径是否存在。
2. 检查新旧文档是否重复或相互矛盾；发现冲突时指出，不擅自选择权威版本。
3. 模拟一次冷启动：仅从入口能否找到当前目标、规则、最近交接和相关源码。
4. 汇报实际创建或修改的文件、未创建的资料位置，以及下一任务应从哪里开始。
