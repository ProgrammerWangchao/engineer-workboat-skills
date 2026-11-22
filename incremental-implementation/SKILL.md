---
name: incremental-implementation
description: "Implement software in small independently verifiable slices using a feature list, existing project conventions, actual checks, and evidence-backed completion states. This skill should be used for feature development, bug fixes, long coding tasks, resume-after-interruption work, and changes where unfinished items must not be reported as complete."
agent_created: true
---

# Incremental Implementation

## Purpose

每轮完成一个可独立验证的功能切片。让代码、检查结果和进度状态保持一致，避免一次性铺开整个项目或过早宣布完成。

## 1. 恢复并限定本轮工作

读取项目规则、产品规格、技术方案、现有功能清单、最近交接、Git 状态和相关源码。确认当前版本与未提交改动，不覆盖用户已有工作。

没有功能清单时，从已确认范围生成 `feature_list.json`，格式参考 [assets/feature_list.template.json](assets/feature_list.template.json)。每项包含稳定 `id`、`category`、`description`、可执行的 `steps`、初始为 `false` 的 `passes` 和空 `evidence`。先核对遗漏与超范围项，再开始修改。

在本 Skill 安装目录运行结构校验，或将脚本路径替换为实际安装路径：

```bash
python scripts/validate_feature_list.py path/to/feature_list.json
```

## 2. 小步实现

- 每轮选择一个清单项或一个紧密关联、可共同验证的小切片。
- 优先复用已有接口、组件、依赖和测试设施，不引入与当前项无关的重构。
- 保持改动可审查；发现需要新业务规则或扩大权限时暂停该项，继续其他不受阻项。
- 为修复的问题补充合适回归检查；测试应能在缺陷存在时失败。
- 不通过删弱断言、跳过用户路径或改写验收条件制造通过。

## 3. 实际自验并更新状态

1. 运行与改动相关的格式化、静态检查、单元测试、构建或端到端检查。
2. 用户可见功能按清单 `steps` 走真实入口；构建通过不能替代用户流程验证。
3. 仅在预期与实际一致且证据可回看时，将 `passes` 设为 `true`，并在 `evidence` 中记录实际命令、测试输出摘要或产物路径。
4. 未运行、工具不可用、结果不确定或仍失败的项保持 `false`。发现回归时将已通过项改回 `false` 并记录原因。
5. 再次运行结构校验；结构合法不代表功能通过。

## 4. 交接与独立复核

汇报本轮版本、改动文件、实际检查、功能入口、未通过项和阻塞点。最终用户流程交由独立验收复核，代码差异交由独立 Review；不要用实现者自评替代二者。

中断或换会话时留下可恢复状态。恢复后先检查实际文件、Git 历史和既有结果，再决定下一步，不重复外部动作。
