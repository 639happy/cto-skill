# Superpowers 接力规则

不同 Agent 产品显示 Skill 的方式不完全一样。目标不是记住某一条命令，而是找到 Superpowers 提供的两个 Skill：`brainstorming`（完成设计）和 `writing-plans`（写开发计划）。

## 先确认当前平台里有什么

1. 查看当前平台已经安装并启用的 Skills。
2. 确认这两个 Skill 来自 Superpowers，不要只凭相似名称判断。
3. 使用平台实际显示的名称。常见形式包括 `superpowers:brainstorming`、`/superpowers:brainstorming`、`superpowers:writing-plans` 和 `/superpowers:writing-plans`，但不要把这些例子当成所有平台都通用的固定命令。

## 平台可以直接启动下一个 Skill

请 Superpowers 读取：

- 当前对话；
- CTO 需求卡；
- `CONTEXT.md` 和重要决定记录；
- 已发现的风险和小验证结果；
- 设计或计划应该保存到哪里。

进入 `brainstorming` 时要说明：已经确认的内容不要重新定义或重复询问；只解决剩余的设计问题；分段请用户确认；完成设计后不要开发，回到 CTO Skill 做设计检查。

进入 `writing-plans` 时要说明：只根据已批准设计写开发计划；不要开始执行；完成后回到 CTO Skill 做开工前检查。

## 平台不能自动启动下一个 Skill

先把当前进度和相关文件写入 CTO 需求卡，再给用户一条可以直接复制的指令。不要只说“请调用下一个 Skill”。

设计阶段可使用：

```text
请使用当前平台中 Superpowers 提供的 brainstorming Skill。读取当前对话和 CTO 需求卡里链接的文件，把已经确认的内容当作不能擅自修改的前提，只解决剩余设计问题。分段让我确认，确认后保存设计；不要开发。完成后继续使用 CTO Skill 做设计检查。
```

计划阶段可使用：

```text
请使用当前平台中 Superpowers 提供的 writing-plans Skill。读取已批准的设计、CTO 需求卡和其中链接的文件，生成可以逐步执行和验收的开发计划；不要开始开发。完成后继续使用 CTO Skill 做开工前检查。
```

## 找不到 Superpowers

暂停并告诉用户：缺少的是 Superpowers 本身、某个具体 Skill，还是 Skill 被关闭。提供当前平台适用的安装或启用方法；如果没有可靠方法，就明确说当前平台只验证了 CTO Skill 的需求梳理部分，不能声称完整流程已经可用。
