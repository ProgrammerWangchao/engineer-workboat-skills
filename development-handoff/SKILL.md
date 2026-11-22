---
name: development-handoff
description: "Persist and resume recoverable software-work state across sessions, agents, interruptions, and failures without copying the full conversation. This skill should be used at meaningful checkpoints, before context resets, after partial or failed work, and when a new session needs to continue from actual files, decisions, checks, and unresolved items."
agent_created: true
---

# Development Handoff

## Purpose

让下一次会话从仓库实际状态继续，而不是重新理解整段聊天或重复已完成动作。交接只保存有持续价值的状态、证据和下一步。

## 1. 写入交接

先读取现有进度与项目记录约定，沿用既有 MEMORY、handoff 或执行计划，避免重复维护。使用 [assets/handoff-template.md](assets/handoff-template.md) 记录：

- 当前目标、授权范围和版本标识。
- 实际完成内容及相关文件路径。
- 已确认决定与详细文档链接。
- 实际运行的命令、检查结果和证据位置。
- 未验证项、失败项、阻塞原因与待用户决策。
- 已产生的外部副作用，如分支、提交、PR、消息、服务或发布状态。
- 唯一下一步及应先读取的资料。

详细需求和技术方案只链接，不整段复制。未知命令、未运行检查和推测结果不得写成事实。遵循已有日志的追加规则，不重写历史。

## 2. 收尾前核对

1. 对照实际文件与 Git 状态，修正交接中的版本和改动范围。
2. 确认证据在清理后仍存在，临时进程和测试数据按授权处理。
3. 将未完成项保持未完成；不要把“已写代码”等同于“已验收”。
4. 仅记录恢复所需信息，不写密钥、短暂工具错误或无关聊天。

## 3. 从交接恢复

1. 先读项目入口、最近交接、相关规格和当前功能清单。
2. 再检查实际目录、版本、Git 历史、运行实例和外部结果，以现实状态为准。
3. 找出第一个未完成且不阻塞的事项，继承原授权；新增需求或超范围动作重新确认。
4. 重试前检查上次动作是否已经成功，避免重复提交、推送、消息或发布。
5. 从失败或中断恢复时，先运行最小诊断，再复用原验收步骤。

结束时简短说明将从哪里继续、仍需什么决策；没有阻塞时不制造额外问题。
