---
name: technical-design
description: "Produce an implementation-ready but not over-specified technical design from a confirmed product spec and existing code, covering architecture choices, data and trust boundaries, dependencies, trade-offs, failure handling, and verification strategy. This skill should be used before non-trivial implementation or when requirements and current architecture conflict."
agent_created: true
---

# Technical Design

## Purpose

在编码前解决会影响系统结构和外部依赖的关键选择，同时避免过早写死字段名、文件数和所有实现细节。

## 1. 对齐事实与冲突

读取项目规则、产品规格、原型、现有架构、相关源码和依赖清单。先总结对首版范围与主要流程的理解。规格、原型和代码冲突时列出具体冲突与影响，不擅自决定哪个优先。

优先复用仓库已有模式、接口、测试工具和服务。推荐新依赖前确认维护状态、许可证、适用版本和接入成本；不确定的事实查官方资料并记录来源。

## 2. 只讨论关键决策

围绕具体用户流程说明各部分如何配合，至少覆盖：

- 前端、服务端、数据库或本地存储是否确有必要。
- 内容、状态与文件由谁维护，读写路径是什么。
- 身份、权限、支付等关键规则在哪一层执行。
- 外部服务、网络、凭据和信任边界在哪里。
- 失败、重试、超时、重复请求和中断恢复如何处理。
- 如何用单元、集成、端到端或真实操作验证关键行为。

给出推荐方案、备选方案、选择理由、主要代价和限制，不只列框架名称。每次只向用户提出会改变方案的关键决策；需要新业务功能才能成立的方案先退回产品规格。

## 3. 控制详细程度

将稳定的方向、高层模块关系、数据所有权和验证策略写入方案。将实现期间可安全调整的细节留给代码。对尚未验证的兼容性、性能或外部能力标记验证步骤，不写成既成事实。

使用 [assets/design-doc-template.md](assets/design-doc-template.md) 整理文档，分开记录已确认决定、建议、开放问题和来源。按项目约定保存并更新索引。

本阶段默认不修改业务代码、不安装依赖、不启动服务。获得实施授权后另走实现阶段。
