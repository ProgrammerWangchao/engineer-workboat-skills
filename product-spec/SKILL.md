---
name: product-spec
description: "Turn a vague software idea into a user-outcome-focused product specification with first-release scope, non-goals, core user journeys, observable acceptance criteria, failure cases, and open decisions. This skill should be used before implementation when requirements or completion criteria are unclear, or when a requested change expands the agreed scope."
agent_created: true
---

# Product Spec

## Purpose

先明确用户要获得的结果，再决定首版做什么。把讨论转化为可检查的产品规格，不把模糊愿望直接变成代码。

## 1. 从已有材料开始

读取项目规则、已有产品文档、原型、相关代码和最近交接。区分已确认事实、历史讨论、建议与待确认项；发现冲突时列出冲突，不静默选择版本。

优先从仓库可观察内容获得答案。仅询问会影响目标用户、首版范围、核心流程或验收标准的决策，每次只问一个最具体、最阻塞的问题。

## 2. 明确结果与边界

1. 写出目标用户、要解决的问题和最终可完成的结果。
2. 用一条端到端核心用户流程约束首版，不先铺开远期规划。
3. 分别列出首版范围内、明确不做和待确认事项。
4. 不自行增加账号、支付、后台、推荐、分析或其他扩展功能。
5. 技术选型留给技术设计，不用产品文档隐式锁死框架或服务。

## 3. 写出能失败的验收条件

为核心流程逐项记录：

- **前置条件**：数据、账号、环境或页面状态。
- **真实入口**：用户从哪里开始。
- **操作**：点击、输入、刷新、提交或调用等可复现步骤。
- **预期结果**：可观察的界面、输出或副作用。
- **证据**：截图、日志、响应、测试输出或记录。
- **失败情况**：空状态、无效输入、重复操作、权限不足和中断恢复。

避免“体验良好”“支持保存”“运行正常”等不可判定措辞。将主观体验列为人工复核项，不伪装成自动通过。更多示例见 [references/acceptance-criteria.md](references/acceptance-criteria.md)。

## 4. 整理并保存

按 [assets/product-spec-template.md](assets/product-spec-template.md) 组织草稿，将“已确认决定”“建议”和“待确认问题”分开。先核对是否存在理解偏差、遗漏或额外功能；取得所需确认后按项目约定保存，并更新已有资料入口。

交付时只说明规格、验收条件和未决问题。本阶段不开发正式业务代码、不安装依赖、不部署。
