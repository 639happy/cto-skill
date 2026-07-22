# CTO Skill

一个面向 Vibecoding 和中小型软件项目的轻量 CTO 工作流：先把需求问清楚，只在风险触发时补充技术护栏，再把设计和实施计划交给 Superpowers，最后回到 CTO 审查并在开发前停止。

> A lightweight CTO workflow for Codex: clarify requirements, trigger risk-based guardrails, orchestrate Superpowers for design and planning, then stop before implementation.

## 为什么做这个 Skill

很多小型项目并不需要一套庞大的研发流程，但仍然需要避免三个常见问题：

- 需求没有真正说清楚就开始开发；
- 关键能力、成本、安全或合规风险没有提前验证；
- 设计和计划完成后直接进入开发，缺少一次面向产品结果的 CTO 复核。

CTO Skill 把这些检查压缩成一个显式调用、低摩擦的入口。它不会为了显得专业而生成大而全的文档，也不会未经批准自动写代码或部署。

## 工作流程

```text
检查项目事实
  → Grill With Docs 式轻量需求澄清
  → 用户确认需求
  → 仅处理已触发的风险
  → Superpowers brainstorming
  → CTO 设计复核
  → Superpowers writing-plans
  → CTO 实施准备度复核
  → 停止，等待用户另行批准开发
```

核心原则：

- 一次只问一个真正影响设计的问题，并给出推荐答案；
- 优先读取项目文件，不重复询问已经确认或可以查到的事实；
- 术语确认后更新 `CONTEXT.md`；
- 只有难以逆转、存在真实取舍且未来难以理解的决定才创建 ADR；
- 外部 AI、API 或平台能力没有证据时，先做 Phase 0 能力验证；
- 设计批准、计划批准和开发批准是三个不同的授权。

## 与 Grill With Docs、Superpowers 的关系

CTO Skill 是一个独立的轻量编排层，建立在两个优秀开源项目的思想与能力之上：

- [Grill With Docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)：CTO Skill 吸收其需求追问、术语澄清、`CONTEXT.md` 沉淀和谨慎创建 ADR 的核心方法。该能力已经内置，不要求用户另行安装 Grill With Docs。
- [Superpowers](https://github.com/obra/superpowers)：CTO Skill 调用 `superpowers:brainstorming` 和 `superpowers:writing-plans`，并在交接前后增加风险检查、质量门槛和返回 CTO 的机制。Superpowers 是当前版本的运行依赖。

CTO Skill 不替代或重新发布这两个项目，也不是它们的官方分支。本项目与 Matt Pocock、Superpowers、Prime Radiant 或 OpenAI 均无官方从属关系。第三方许可证和署名见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 适用范围

适合：

- 非技术背景的产品经理或独立创作者；
- Vibecoding、小程序、Web 工具和轻量 SaaS；
- 需要把模糊想法推进到已批准设计和实施计划的项目；
- 希望保留 CTO 风险门槛，但不想引入重型流程的团队。

不适合：

- 直接要求写代码、修 Bug 或执行部署；
- 替代正式的法律、合规或安全审计；
- 没有安装 Superpowers，却期望完整运行设计和计划交接。

## 前置条件

- Codex App 或 Codex CLI；
- 已从 Codex 插件市场安装 [Superpowers](https://github.com/obra/superpowers)；
- 当前版本在 Superpowers `6.1.1` 上完成验证。

Superpowers 安装方式：

- Codex App：打开侧边栏的 **Plugins**，在 Coding 分类中安装 **Superpowers**；
- Codex CLI：运行 `/plugins`，搜索 `superpowers` 并选择安装。

## 安装 CTO Skill

### 方式一：下载并复制

1. 下载本仓库 ZIP 并解压。
2. 将仓库里的整个 `ctoskill` 文件夹复制到：
   - macOS / Linux：`~/.codex/skills/ctoskill`
   - Windows：`%USERPROFILE%\.codex\skills\ctoskill`
3. 新建一个 Codex 任务，让 Skill 列表重新加载。

### 方式二：命令行

```bash
git clone https://github.com/639happy/cto-skill.git
mkdir -p ~/.codex/skills
cp -R cto-skill/ctoskill ~/.codex/skills/ctoskill
```

如果目标位置已经存在旧版本，请先自行备份，不要直接覆盖。

## 使用

CTO Skill 只接受显式调用。示例：

```text
使用 $ctoskill 帮我规划一个上传图片后生成可复现近似提示词的小程序。
```

它会先读取现有项目，再逐个澄清关键问题。完成需求、风险、设计和计划复核后，它会停止，不会自动进入开发。

## 目录结构

```text
ctoskill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── context-and-adr.md
    ├── cto-brief-template.md
    └── risk-triggers.md
```

仓库根目录中的 README、贡献说明、验证脚本和 GitHub 配置只服务于开源项目维护，不会被安装进 Skill 的运行上下文。

## 验证

```bash
python3 scripts/validate_repo.py
```

验证会检查 Skill 结构、显式触发配置、引用文件、敏感信息模式和仓库发布边界。

## 贡献与安全

- 贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 安全问题见 [SECURITY.md](SECURITY.md)。
- 本项目采用 [MIT License](LICENSE)。
