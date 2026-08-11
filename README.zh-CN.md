# WorkFn 职场函数库

> 把职场判断，封装成可复用的 Skill。

## WorkFn 是什么

WorkFn 是一组职责明确、可以分别调用的职场 Skill。它把判断标准、思考步骤和执行流程封装成可重复使用的函数式能力。

本项目不是万能沟通生成器。每个 Skill 只解决一个明确问题。Skill 先做参数检查、证据检查和风险判断，再决定是否生成结果。

WorkFn 中的每个 Skill 都先执行参数解析和完整度检查。Skill 不会直接生成答案，而会先判断用户已经提供哪些参数、缺少或冲突哪些参数，以及当前信息是否足以支持可靠分析。详见 [SKILL_RUNTIME_PROTOCOL.md](SKILL_RUNTIME_PROTOCOL.md)。

## 统一命名

每个 Skill 都有清晰职责、输入、边界和输出。文件夹名、正式 Skill ID 和 UI 展示名称统一使用小写 `zayn-*` 格式。

每个 WorkFn Skill 都包含三层名称：

1. 正式 Skill ID，例如 `zayn-reply`
2. UI 展示名称，例如 `zayn-reply`
3. 中文名称，例如“客户回复”

每个正式 `SKILL.md` 必须以 YAML front matter 开头，并包含 `name` 和 `description`。Codex 使用这些字段进行 Skill 识别、卡片展示和调用发现。

正式 Skill ID 用于 GitHub、WorkBuddy 或其他平台发布，并体现 Zayn 的个人品牌；这不代表当前已经兼容任何具体平台。每个 Skill 的末级文件夹名称现已与正式 `zayn-` Skill ID 保持一致。

## 与普通提示词合集的区别

普通提示词合集往往直接要求生成内容；WorkFn 要求先诊断输入、证据、风险和人工判断边界，并允许在信息不足或风险过高时不生成成品。

## Skill 如何工作

1. 确认适用场景。
2. 检查必填参数和可选参数。
3. 按优先级核验证据。
4. 执行判断规则和风险检查。
5. 尊重人工确认的事实与判断。
6. 输出符合约定的结构，或明确说明信息不足。

## 当前开发状态

当前版本为 `v0.1.0` 本地骨架。当前共有 12 个编号分类和 82 个已登记 Skill，并已加入项目级路由与编排、通用与行业专用能力分流、产品理解与技术判断分类以及 Alibaba 平台专用 Skill。部分 Skill 已形成初版测试规则，但尚未完成真实案例验收。

## Skill 路由与编排

`ROUTE()` 是 WorkFn 的路由与编排层。

它负责识别问题、选择 Skill、安排顺序、传递必要结果并设置停止条件。它不自动执行其他 Skill。

如果需要了解每个 Skill 能解决什么问题以及适用场景，请查看 [WorkFn Skill 使用场景指南](SKILL_USE_CASE_GUIDE.zh-CN.md)。

如果需要把 WorkFn 配置为 ChatGPT 自定义 GPT，请使用 [WorkFn 自定义 GPT 配置包](gpt_package/README.md)。

## 第一批 Skill

第一批计划完善：`REPLY()`、`RFQ()`、`FOLLOWUP()`。其中 `REPLY()` 和 `FOLLOWUP()` 已升级至 v0.2.0 测试规则，`RFQ()` 仍等待补充。

新增骨架包括 `INTENT_DECODE()`、`KEYPOINT()` 和 `ORDER_KICKOFF()`，目前仅完成基础定位和文档结构。

## 使用边界

- 不把 AI 推测写成事实。
- 不覆盖人工已经确认的事实和判断。
- 信息不足时允许停止并提出缺失项。
- 当前不声明兼容 WorkBuddy 或其他 Skill 平台。
- 当前不包含自动调用逻辑。

## 发布计划

先逐个完善第一批 Skill，再补充真实脱敏案例和测试，确认许可证、作者信息和平台格式后，才考虑 GitHub 或平台发布。详见 [PUBLISHING.md](PUBLISHING.md)。
