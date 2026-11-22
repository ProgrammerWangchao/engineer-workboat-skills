---
name: interactive-prototype
description: "Build and exercise a lightweight clickable UI prototype from an agreed product specification using sample data and explicit demo boundaries. This skill should be used to validate page structure, visual direction, and primary interactions before production implementation, especially for websites, mobile interfaces, dashboards, and admin tools."
agent_created: true
---

# Interactive Prototype

## Purpose

在正式开发前，用可点击原型验证信息层级和主要操作，而不是用静态描述猜测用户体验。

## 1. 确认输入和演示边界

读取项目规则、已确认产品规格与视觉参考。列出本轮页面、核心交互、目标屏幕尺寸和设计方向；沿用项目已有设计系统与 Skill。文档和原型冲突时先指出，不自行增加功能。

默认采用轻量 HTML、CSS 和 JavaScript，使用示例数据，不接真实后端或数据库。覆盖已有原型、启动服务、安装依赖或连接外部服务前，按任务授权取得确认。

## 2. 制作可操作的页面

- 将核心用户流程串起来，让入口、详情、主要操作和返回路径真正可点击。
- 使用明确标识的示例内容，保持文本可读、按钮含义清晰、状态反馈一致。
- 适配约定的桌面和手机尺寸，处理空状态、无效操作和演示边界。
- 未接通的支付、下载、提交、分享等行为明确标为“演示”或“未接通”，不得用成功提示冒充真实副作用。
- 将原型放在项目约定的演示目录，不污染正式业务入口。

## 3. 实际操作并留证

1. 使用可用浏览器打开本次原型，确认预览对应刚生成的版本。
2. 按核心用户流程实际点击、输入和返回，检查控制台错误与可见状态。
3. 在约定尺寸下检查溢出、遮挡、键盘操作和主要交互。
4. 保存必要截图或操作记录，逐项给出通过、失败或受阻；工具不可用时说明阻塞点，不把代码审阅当作交互实测。
5. 仅清理本轮启动的实例和临时状态，保留证据。

交付预览方式、实际测过的流程、未验证项和需要确认的设计问题。本阶段不开始正式业务开发，不提交、推送或部署。
