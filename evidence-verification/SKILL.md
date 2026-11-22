---
name: evidence-verification
description: "Independently verify a specific software or deliverable version by executing real user paths or deterministic checks and returning passed, failed, or blocked results with evidence. This skill should be used for acceptance testing, regression verification, UI and API validation, report or media checks, and retesting fixes; it is not a code-only review."
agent_created: true
---

# Evidence Verification

## Purpose

拿实际交付版本逐条对照事先约定的标准。通过真实执行与可回看的证据判定，不从代码存在、构建成功或实现者描述推断功能完成。

## 1. 固定版本与验收输入

读取项目规则、验收标准、功能地图、交接和运行说明。记录实际版本、环境、入口、测试数据和工具权限。版本无法确认时标记受阻，不继续给出通过结论。

优先独立上下文执行，保持实现代码不变。确认运行实例由本轮管理，避免双开驱动同一用户会话或污染共享数据。功能地图与证据规则见 [references/function-map-and-evidence.md](references/function-map-and-evidence.md)。

## 2. 把要求变成会失败的检查

每项写清前置条件、真实入口、操作、预期和证据：

- 网页或桌面产品实际点击、输入、刷新、重新打开并检查副作用。
- API 或服务发送真实请求并核对状态、响应与持久化结果。
- 报表从明细重算，保留公式、口径、单位与差额。
- 文件、设计和媒体逐个打开，用工具检查格式、尺寸、透明通道、时间码等客观属性。
- 主观体验、品牌和叙事判断交人工复核，不伪造确定性结论。

优先项目已有测试与操作工具。仅在本轮授权范围内使用测试数据、测试模式和隔离环境；外部写入或破坏性操作必须先取得授权。

## 3. 按证据判定

仅使用三种状态：

- `passed`：在该版本实际执行，预期与实际一致，证据可打开或重跑。
- `failed`：检查成功执行但结果不满足标准；给出最小复现、实际结果和证据。
- `blocked`：环境、权限、版本或工具使检查无法完成；说明卡在哪一步和解锁条件。

修复后使用同一输入、步骤和标准复测，同时检查相关流程未回归。不删除失败历史，追加新轮次结果。

## 4. 验证检查本身

新增自动检查或关键人工流程时，尽可能运行一份已知正确的正样例和一份带已知错误的负样例。正样例应通过，负样例必须因预期原因失败；两者都通过说明检查无效。无法构造时明确记录这一验证缺口。

## 5. 交付结构化报告

使用 [assets/verification-report.template.json](assets/verification-report.template.json) 记录版本、用例、实际结果与证据。在本 Skill 安装目录运行报告校验，或将脚本路径替换为实际安装路径：

```bash
python scripts/validate_verification_report.py path/to/report.json --check-files
```

脚本只验证报告结构和文件证据存在性，不把 JSON 合法误判为产品通过。最终报告列出失败复现、受阻解锁条件、未覆盖范围和需人工复核项。
