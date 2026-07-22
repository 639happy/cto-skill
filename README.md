# CTO Skill

给不会编程、但想用 AI 做小程序、网页工具或轻量产品的人使用。

它不会一上来就给你一大份看不懂的技术方案，而是先用几个关键问题把想法问清楚，再把确认好的内容交给 Superpowers 完成设计和开发计划。

> A plain-language planning skill for non-technical builders using skills-compatible AI agents.

## 不会安装？复制这段话给你的 Agent

无论你使用 Codex、Claude Code、Cursor、Windsurf、WorkBuddy 或其他 Agent，都可以先把下面整段话复制给它：

```text
请帮我安装并使用这个开源项目：https://github.com/639happy/cto-skill 。先阅读项目说明，自动判断我现在使用的 Agent 产品，把 CTO Skill 安装到正确位置；如果已经有旧版本，请先备份。完整使用还需要 Superpowers：如果当前平台支持，请检查它是否已经安装并启用；如果没有，请直接帮我安装，遇到必须由我点击或授权的步骤时再告诉我。如果当前平台不能完整支持，请如实说明，不要假装安装成功。最后请实际检查 CTO Skill 能否被识别，并用一句简单的话告诉我以后怎样开始使用。未经我明确同意，不要开始写代码或部署产品。
```

你不需要先学会命令行，也不用自己判断文件应该放在哪里。Agent 应该先告诉你它准备做什么；遇到登录、安装插件、覆盖文件或其他需要授权的操作时，再由你确认。

## 它能帮你做什么

CTO Skill 只做三件事：

1. **把想法问清楚**：一次只问一个真正影响产品的问题，并给出推荐答案。
2. **提前发现关键坑**：只检查这个项目确实会遇到的费用、权限、第三方服务、上线或合规问题。
3. **把下一步接好**：把已确认内容交给 Superpowers 完成设计和开发计划，做完再回来检查。

通常只需要回答 3–5 个问题。它不会为了显得专业而增加很多表格和流程，也不会在你没有明确同意时开始写代码或部署。

## 使用过程

```text
先看你已有的材料
  → 一次问一个关键问题
  → 你确认这次到底要做什么
  → 只检查已经出现的风险
  → Superpowers 完成设计
  → CTO Skill 帮你检查设计
  → Superpowers 写开发计划
  → CTO Skill 做开工前检查
  → 停止，等你决定是否开始开发
```

你不需要理解技术架构。遇到必须解释的技术选择时，CTO Skill 应该告诉你它会怎样影响产品体验、费用、上线和以后维护。

## 不是 Codex 专用

CTO Skill 的核心采用开放的 [Agent Skills 格式](https://agentskills.io/specification)：一个 `SKILL.md` 加上少量按需读取的参考文件。支持这种格式的 Agent 产品，原则上都可以读取同一份核心 Skill。

但要区分两件事：

- **CTO Skill 能安装**：平台能读取这份 Skill，并完成需求梳理和风险检查。
- **完整流程能跑通**：同一平台还安装了 Superpowers，并且能继续调用它的设计和计划 Skill。

当前兼容情况：

| 平台 | CTO Skill 核心 | 与 Superpowers 完整接力 | 当前结论 |
|---|---|---|---|
| Codex App / CLI | 支持 | 支持 | 已在本机验证 |
| Claude Code | 支持 | 支持 | 官方支持 Agent Skills 和 Superpowers；本仓库已做格式验证 |
| Cursor | 支持 | 支持 | 官方已支持 Agent Skills，Superpowers 也提供 Cursor 安装方式；待本项目实机回归 |
| Windsurf | 支持 | 尚未确认 | 官方支持同一类 `SKILL.md`；当前只承诺 CTO 核心兼容 |
| WorkBuddy | 可导入 Skill 包 | 尚未确认 | 官方支持上传本地 Skill；当前仍需实机验证本包和 Superpowers 接力 |

参考：[Claude Code Skills](https://code.claude.com/docs/en/slash-commands)、[Cursor Skills](https://cursor.com/changelog/2-4)、[Windsurf Skills](https://docs.windsurf.com/zh/windsurf/cascade/skills)、[WorkBuddy Skills](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[Superpowers 安装说明](https://github.com/obra/superpowers#installation)。

## 与 Grill With Docs、Superpowers 的关系

CTO Skill 是在两个优秀开源项目之上做的一层简化和连接：

- [Grill With Docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) 擅长把模糊需求问清楚、统一容易混淆的词语，并谨慎记录重要决定。CTO Skill 已经吸收这些核心做法，用户不需要另外安装它。
- [Superpowers](https://github.com/obra/superpowers) 负责完成产品和系统设计、编写开发计划，并在之后支持开发过程。要运行完整流程，需要在同一个 Agent 产品里安装并启用 Superpowers。

CTO Skill 不复制或重新发布这两个项目的 Skill 文件，也不是它们的官方版本。第三方许可证和署名见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 适合谁

适合：

- 不会编程，想用 AI 做自己的小工具；
- 产品经理、独立创作者或刚开始 Vibe Coding 的用户；
- 小程序、网页工具、内部工具和轻量 SaaS；
- 希望先把需求想清楚，又不想使用重型研发流程的人。

不适合：

- 只想马上写代码、修 Bug 或直接部署；
- 用它替代正式的法律、合规或安全审查；
- 没有安装 Superpowers，却要求自动完成后续设计和开发计划。

## 安装

先从 [最新版本页面](https://github.com/639happy/cto-skill/releases/latest) 下载 `ctoskill.zip` 并解压。里面就是可以安装的完整 Skill 文件夹。

### Codex App / CLI

把整个 `ctoskill` 文件夹复制到：

- macOS / Linux：`~/.codex/skills/ctoskill`
- Windows：`%USERPROFILE%\.codex\skills\ctoskill`

然后新建一个 Codex 任务，让 Skill 列表重新加载。完整流程还需要从 Codex 插件市场安装 **Superpowers**。

### Claude Code

把整个 `ctoskill` 文件夹复制到：

- 个人使用：`~/.claude/skills/ctoskill`
- 只给当前项目使用：`.claude/skills/ctoskill`

完整流程还需要在 Claude Code 官方插件市场安装并启用 **Superpowers**。

### Cursor

在 Cursor 设置的 Skills 区域导入 Agent Skill，或把 `ctoskill` 文件夹放入当前项目的 `.cursor/skills/`。安装后确认它出现在 `/` 命令菜单中。

完整流程还需要在 Cursor Agent 对话中安装 Superpowers：

```text
/add-plugin superpowers
```

### Windsurf

可以在 Cascade 的 **Customizations → Skills** 中创建或管理 Skill，也可以把 `ctoskill` 文件夹复制到：

- 当前项目：`.windsurf/skills/ctoskill`
- 所有项目：`~/.codeium/windsurf/skills/ctoskill`

Windsurf 也会读取 `.agents/skills/ctoskill`。目前没有核验 Superpowers 的完整接力，所以只把需求梳理部分视为已兼容。

### WorkBuddy

打开 **技能 → 添加技能 → 上传技能**，选择发布页中的 `ctoskill.zip`。WorkBuddy 官方支持上传本地 Skill 包，但本项目还没有完成 WorkBuddy 实机验证；如果导入失败，请提交 Issue 并附上脱敏后的提示信息。

## 怎样开始使用

不同平台的手动调用方式可能不同：

- Codex：`使用 $ctoskill 帮我……`
- Claude Code / Cursor：`/ctoskill 帮我……`
- Windsurf：`@ctoskill 帮我……`
- WorkBuddy：在对话中明确说“使用 CTO Skill 帮我……”

例如：

```text
使用 CTO Skill 帮我规划一个上传图片后生成相似提示词的小程序。
```

CTO Skill 会先读现有材料，再逐个问关键问题。完成设计和开发计划检查后，它会停下来，不会自动进入开发。

## 文件为什么这么少

```text
ctoskill/
├── SKILL.md                         # 所有平台共用的核心说明
├── agents/
│   └── openai.yaml                 # Codex 的显示名称和手动调用设置
└── references/
    ├── context-and-adr.md           # 项目记录规则
    ├── cto-brief-template.md        # CTO 需求卡模板
    ├── risk-triggers.md             # 只在需要时读取的风险检查表
    └── superpowers-handoff.md       # 不同平台怎样接到 Superpowers
```

其他平台会读取 `SKILL.md` 和 `references/`；看不懂 `agents/openai.yaml` 也没有关系，它只是 Codex 的补充信息。这样可以保持一份核心文件，不为每个平台复制一套容易过期的版本。

## 维护者验证

```bash
python3 scripts/validate_repo.py
```

验证会检查 Skill 文件是否齐全、核心格式是否通用、引用是否有效，以及公开仓库里有没有误放个人路径、密钥或内部评测材料。

## 贡献与安全

- 改进方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 安全问题见 [SECURITY.md](SECURITY.md)。
- 本项目采用 [MIT License](LICENSE)。
