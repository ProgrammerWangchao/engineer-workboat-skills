---
name: independent-code-review
description: "Review a concrete code change against requirements and actual behavior in a fresh, read-only context, returning severity-ranked findings with file and line locations, triggers, impact, and verification status. This skill should be used for pre-merge review, independent review after implementation, regression risk analysis, and validating another reviewer's comments."
agent_created: true
---

# Independent Code Review

## Purpose

从实现上下文之外发现缺陷、需求遗漏和验证缺口。默认只读，不把 Review 变成另一轮实现。

## 1. 建立独立审查范围

读取项目规则、产品规格、功能清单、技术方案、交接和实际差异。确定基线、待审版本和变更文件；没有 Git 基线时按交接列出的文件集合审查，并明确限制。

不依赖实现者总结判断正确性。先查看已有检查和验收证据，再用实际源码核对；证据不足不等于代码有错，但要列为残余风险。详细规则见 [references/review-protocol.md](references/review-protocol.md)。

## 2. 沿行为和风险审查

优先检查：

- 核心用户流程、业务规则、权限判断和数据一致性。
- 空状态、边界输入、错误处理、重试、并发和中断恢复。
- 需求遗漏、超范围改动、兼容性与迁移风险。
- 测试是否真正覆盖触发条件，是否会在缺陷存在时失败。
- 安全与隐私问题，以及外部副作用是否受授权约束。

避免无项目依据的风格偏好、与本次改动无关的大规模建议和不可执行的抽象评价。

## 3. 核实发现

每条发现给出：

1. 严重级别：阻塞、高、中、低。
2. 文件与最小行号范围。
3. 触发条件和影响。
4. 代码依据；能够安全验证时给出实际复现或测试结果。
5. 最小修复方向和需要的回归检查。

区分“已验证”和“静态推断”。对另一位 Reviewer 的意见先按触发条件核实，不因意见听起来合理就直接修改。Review 中发现需要产品决策的问题应单列，不替用户决定。

## 4. 输出结论

先按严重程度列发现，再列测试缺口和残余风险。没有发现时明确写“未发现可确认的问题”，同时说明实际检查范围和未验证部分，不宣称绝对正确。

修复由授权的实现阶段完成；修复后用原触发条件复测并运行受影响检查。除非用户明确要求，本 Skill 不修改代码、不提交、不推送。
