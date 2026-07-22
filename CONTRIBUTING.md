# Contributing

感谢你改进 CTO Skill。这个项目优先追求低摩擦、可理解和可验证，而不是增加更多流程。

## 开始之前

- 小型修正可以直接提交 Pull Request。
- 会改变状态流、Superpowers 交接或开发停止边界的修改，请先创建 Issue 说明使用场景和产品影响。
- 不要把 Grill With Docs、Superpowers 或其他第三方 Skill 文件直接复制进本仓库。

## 本地验证

```bash
python3 scripts/validate_repo.py
```

如果修改会改变行为，请在 Pull Request 中至少说明：

- 修改前的失败或摩擦；
- 修改后的预期行为；
- 用过的实际场景；
- 是否改变显式触发、交接、返回 CTO 或停止边界。

## Pull Request 要求

- 保持 `ctoskill/SKILL.md` 精简；详细规则放入按需读取的 `references/`。
- 不提交密钥、个人信息、本机路径、内部对话或未脱敏评测记录。
- 不把设计批准或计划批准解释成开发批准。
- 更新依赖关系时同步更新 README 和第三方声明。

提交贡献即表示你同意按照本项目的 MIT License 发布该贡献。
