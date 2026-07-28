# WorkFn 自定义 GPT 配置包

本目录用于把 WorkFn 的 51 个 Codex Skill 转换为一个可在 ChatGPT 中配置的自定义 GPT。

## 包含内容

- `GPT_CONFIG.md`：GPT 名称、描述、对话开场白和能力建议
- `GPT_INSTRUCTIONS.md`：粘贴到 GPT 编辑器 Instructions 的完整内容
- `knowledge/`：上传到 GPT 编辑器 Knowledge 的 10 个分类知识文件

## 配置步骤

1. 在 ChatGPT 网页端打开 GPT 编辑器。
2. 创建一个新 GPT，并切换到配置界面。
3. 按 `GPT_CONFIG.md` 填写名称、描述和对话开场白。
4. 将 `GPT_INSTRUCTIONS.md` 的正文完整粘贴到 Instructions。
5. 将 `knowledge/` 下的 10 个 Markdown 文件全部上传到 Knowledge。
6. 暂不配置 Actions；WorkFn 当前只提供判断、分析和文本输出。
7. 在 Preview 中运行 `GPT_CONFIG.md` 给出的验收问题。
8. 确认路由、停止条件和事实边界符合预期后再保存或分享。

## 重要说明

- 自定义 GPT 不会像 Codex 一样逐个“安装”51个本地 Skill。
- 本包通过一份统一 Instructions 和10份分类 Knowledge 文件复现 Skill 选择与执行逻辑。
- Knowledge 文件是参考资料；路由流程、事实边界、参数检查和停止规则写在 Instructions 中。
- 当前未配置外部 API、数据库、自动执行、邮件发送或平台提交。
- 上传到 Knowledge 的内容可能被 GPT 在回答中使用，请勿加入未脱敏客户资料或公司机密。

## 更新方式

当 WorkFn 源 Skill 更新后，应重新生成 `knowledge/` 文件，并在 GPT 编辑器中替换旧知识文件。更新 Instructions 时应重新执行 Preview 测试。
