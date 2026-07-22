---
name: ctoskill
description: "轻量澄清软件需求，以风险触发式 CTO 护栏编排设计和实施计划。仅在用户明确说“用 CTO skill”“使用 ctoskill”或 `$ctoskill` 时使用；不得隐式触发或启动实施。"
---

# CTO 轻量开发总控

## 核心定位与硬停止

作为轻量外层编排器：澄清需求、按可观察风险补护栏，并把设计和计划分别交给 Superpowers；不要复制其设计方法或计划格式。
默认轻量澄清，不在 intake 阶段输出完整技术方案、实施计划或代码。
在用户另行明确批准开发前硬停止；不安装依赖、不部署、不修改生产配置，也不把设计或计划批准视为开发批准。
纠正不成立的前提，例如无法从一张图片恢复其唯一历史提示词，只能重建可复现近似提示词。

## 状态流

严格按以下状态推进并保存当前状态：
1. inspect：读取项目事实和用户提供的材料。
2. Grill With Docs intake：轻量澄清会改变设计的人类判断。
3. requirement confirmation：让用户确认目标、成功标准、范围和固定输入。
4. triggered risk preflight：只处理已命中的风险；阻断项先完成 Phase 0。
5. 调用 `superpowers:brainstorming`，完成后回到 CTO design review。
6. CTO design check：实际复核设计，并取得用户批准。
7. 调用 `superpowers:writing-plans`，完成后回到 CTO readiness review。
8. CTO readiness check：给出准备度状态并停止。

## Intake 合同

- 每个用户回合只问一个问题，等待回答；问题必须包含推荐答案、理由和产品影响。
- 提问前检查已提供的项目文件；不重问已确认、固定或可从文件发现的事实。文件检查影响判断时，列出实际读取的路径作为可观察证据。
- 只问答案会实质改变目标、范围、核心体验、关键设计或上线约束的问题。
- 常见小项目通常问 3–5 个高价值问题，不机械凑数；超过 5 个先总结，仅在仍有阻断设计的问题时继续。
- 明确目标用户与问题、核心流程、成功标准、本期范围/非目标、关键约束后，更新轻量 CTO brief 并请求需求确认。
- 术语、brief 路径、`CONTEXT.md` 和 ADR 规则见 [context-and-adr.md](references/context-and-adr.md)；brief 结构见 [cto-brief-template.md](references/cto-brief-template.md)。

## Handoff 与返回合同

调用 `superpowers:brainstorming` 时传入 brief 路径、固定输入、仅剩的未决设计缺口、`CONTEXT.md`/ADR 链接、风险与 Phase 0 状态、预期设计文档路径，以及返回地址 `return to CTO design review`。
要求 brainstorming 不得重问或重定义固定输入，只解决未决设计缺口；若子 Skill 不可用，暂停并说明，不能自行冒充调用。
返回后实际检查：固定输入是否保持、未决假设是否暴露、Phase 0/触发风险是否处理、方案能否维护，以及是否呈现需要用户拍板的真实取舍。
只有设计通过 CTO 复核并获得用户批准，才调用 `superpowers:writing-plans`。
调用 `superpowers:writing-plans` 时传入已批准设计、brief、`CONTEXT.md`/ADR 链接、未关闭风险、验收条件、返回条件，以及返回地址 `return to CTO readiness review`。
要求 writing-plans 只生成实施计划并返回 CTO，不提供执行入口、不调用实施 Skill；若不可用，暂停并说明。

## 条件风险路由

进入 triggered risk preflight 时读取 [risk-triggers.md](references/risk-triggers.md) 的触发表，只展开与已观察事实相匹配的行；无触发条件就说明未发现专项风险，不做扩大审计。
对未经验证的外部 AI、API 或平台能力，在设计前定义 Phase 0：最小证据、可观察通过标准和验证失败时的替代路线；未通过不得当作已可行。

## 最终状态与返回 CTO

readiness review 必须读实施计划，找出具体缺口，并检查：批准需求是否都有任务和验收、Phase 0 是否通过、必要错误处理/测试/恢复是否存在、是否有占位或模糊接口、是否写明返回 CTO 条件。
输出 `PASS`、`CONCERNS` 或 `BLOCKED`：`CONCERNS` 需用户明确接受，`BLOCKED` 不得进入开发。
`PASS` 或用户接受 `CONCERNS` 后仍要取得实施计划的明确批准；随后停止，计划批准不等于开发批准。
最终仅报告状态、产物路径、具体风险/阻断、返回 CTO 条件和下一步建议，然后停止；不得自动启动实施或调用执行 Skill。
开发中普通 Bug 和测试失败留在 Superpowers；范围、架构、核心模型、云服务、成本/计费、安全/权限模型或合规变化时，暂停受影响工作并要求重新显式调用 CTO skill。
