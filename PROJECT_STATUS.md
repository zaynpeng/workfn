# Project Status

## 当前版本

`v0.1.0`（本地项目骨架）

## 已完成

- 当前共有 12 个编号分类和 82 个已登记 Skill。
- 每个 Skill 建立 `README.md`、`SKILL.md`、`examples.md`、`tests.md` 和 `changelog.md` 5 个标准 Markdown 文件；需要时增加 `agents/openai.yaml` 和运行参考文件。
- 建立项目索引、开发规范、贡献规范、发布准备说明、许可证选择说明和平台适配占位。
- `REPLY()` 已升级至 `v0.2.0` 测试规范，包含最新必填参数、双运行模式、停止条件、职责边界和正式输出结构。
- `FOLLOWUP()` 已升级至 `v0.2.0` 测试规范，包含最新跟进输入、双运行模式、停止条件、职责边界和正式输出结构。
- 已新增 `CUSTOMER_PROFILE()` 客户画像 Skill 初版规则。该 Skill 只负责事实整理，不负责客户价值判断、分层和推进策略。
- 已新增 `PRODUCT_BRIEF()` 产品速览 Skill 初版规则。该 Skill 只负责产品理解，不负责询价价值判断、报价生成和最终兼容性结论。
- 已新增 `ALI_RFQ_SCAN()` 阿里 RFQ 市场筛选 Skill 初版规则，用于批量筛选机会和控制报价权益。
- 已新增 `ALI_RFQ_BID()` 阿里 RFQ 报价 Skill 初版规则，用于生成和检查平台报价表单内容。
- 已新增 `INTENT_DECODE()`、`KEYPOINT()`、`ORDER_KICKOFF()` 三个 Skill 骨架。当前只完成基础定位、职责边界和文档结构，尚未补充完整输入参数、判断规则和真实测试案例。
- 已建立统一的 Skill 参数解析与运行协议。所有 Skill 后续必须先完成参数映射、参数状态检查和最低运行条件判断，再进入正式分析。
- 已按专用提示词完成 `APOLOGY()`、`CLARIFY()`、`DECLINE()`、`PUSH()`、`RELATION()` 和 `INTENT_DECODE()` 的 `v0.1` 初版规则。
- 已将 `REPLY()` 和 `FOLLOWUP()` 完整版提示词中的最低运行条件合并到现有详细规则，未覆盖原有内容。
- 已按专用提示词完成 `RFQ()`、`QUOTE()`、`PRICE()`、`NEGOTIATE()`、`ALTERNATIVE()`、`AVAILABILITY()` 和 `CONDITION()` 的 `v0.1` 初版规则。
- 已按专用提示词完成 `ORDER()`、`ORDER_KICKOFF()`、`DELIVERY()`、`DELAY()`、`PAYMENT()` 和 `SHIPMENT()` 的 `v0.1` 初版规则。
- 已按专用提示词完成 `COMPLAINT()`、`RESPONSIBILITY()`、`RMA()` 和 `SOLUTION()` 的 `v0.1` 初版规则。
- 已按专用提示词完成 `QUALIFY()`、`SEGMENT()`、`PRIORITY()`、`OPPORTUNITY()`、`LOST()`、`REACTIVATE()` 和 `ACCOUNT()` 的 `v0.1` 初版规则，并合并 `CUSTOMER_PROFILE()` 完整版最低运行条件。
- 已按专用提示词完成 `REPORT()`、`REQUEST()`、`ESCALATE()`、`DECISION()`、`MEETING()`、`MINUTES()`、`HANDOVER()` 和 `KEYPOINT()` 的 `v0.1` 初版规则。
- 已新增 `MONTHLY_REPORT()`、`MIDYEAR_REPORT()` 和 `ANNUAL_REPORT()` 三个周期性汇报 Skill，并同步 `REPORT()` 路由规则。
- 已新增 `CROSS_FUNCTIONAL_COLLABORATION()` 跨部门协同 Skill，覆盖事实、承诺、推责、推进和信息不足判断。
- 已新增 `UPWARD_COMMUNICATION()` 上级沟通与管理沟通 Skill，覆盖跨岗位汇报、请示、审批、升级、资源申请、个人事项和意见反馈。
- 已按专用提示词完成 `REVIEW()`、`FOCUS()`、`LEARN()`、`PLAN()`、`PRACTICE()` 和 `READ()` 的 `v0.1` 初版规则。
- 已合并 `PRODUCT_BRIEF()`、`ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 完整版提示词要求，并保留原有更详细的业务规则。
- 已新增 `ROUTE()` Skill 路由与编排初版规则。
- 已新增 `NETWORKMAP()` 公开关系研究 Skill，覆盖行业与展会、行业与协会、公司与近期活动三种模式，并建立证据、角色和名单完整度边界。
- `ROUTE()` 位于所有业务 Skill 之上，只负责选择 Skill、安排顺序、管理参数传递和设置停止条件，不直接完成业务分析。
- 已为所有 WorkFn Skill 统一增加 `zayn-` 前缀的正式 Skill ID，用于体现 Zayn 的个人品牌。
- 已将全部 51 个原有 Skill 的末级文件夹名称统一为对应的 `zayn-` 正式 Skill ID，同时保留函数式 Display Name 和中文名称。
- `ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 已升级至 `v0.2.0`，补齐明确最低运行条件、停止条件、相邻 Skill 边界、场景案例和协议测试。
- 已为全部 51 个原有正式 `SKILL.md` 统一规范 YAML front matter，包含用于 Skill 识别、卡片展示和调用发现的唯一 `name` 与中文 `description`。

## 未完成

- `REPLY()` 的真实脱敏案例测试和验收。
- `FOLLOWUP()` 的真实脱敏案例测试和验收。
- `CUSTOMER_PROFILE()` 的真实脱敏案例测试和验收。
- `PRODUCT_BRIEF()` 的真实脱敏案例测试和验收。
- `ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 的真实脱敏案例测试和验收。
- 本次更新的 8 个客户沟通 Skill 尚未完成真实脱敏案例测试和验收。
- 本次更新的 7 个询价与报价 Skill 尚未完成真实脱敏案例测试和验收。
- 本次更新的 6 个订单与交付 Skill 尚未完成真实脱敏案例测试和验收。
- 本次更新的 4 个客诉与售后 Skill 尚未完成真实脱敏案例测试和验收。
- 本次更新的 8 个客户管理 Skill 和 8 个内部协作 Skill 尚未完成真实脱敏案例测试和验收。
- 新增的 3 个周期性汇报 Skill 尚未完成真实脱敏案例测试和验收。
- 新增的 `CROSS_FUNCTIONAL_COLLABORATION()` 尚未完成真实脱敏案例测试和验收。
- 本次更新的 6 个个人生产力 Skill 尚未完成真实脱敏案例测试和验收。
- `ROUTE()` 尚未完成真实复杂案例测试和验收。
- 其余 Skill 的详细业务规则。
- 经人工确认的真实或脱敏案例。
- 可执行的测试案例与验收结果。
- 平台格式验证、作者信息确认和正式许可证。

## 第一批开发 Skill

- `REPLY()`
- `RFQ()`
- `FOLLOWUP()`

## 第二批开发 Skill

- `QUOTE()`
- `CLARIFY()`
- `COMPLAINT()`

## 当前风险

- `REPLY()` 规则仍处于 Draft for testing，尚未通过真实案例验证。
- `FOLLOWUP()` 规则仍处于 Draft for testing，尚未通过真实案例验证。
- `CUSTOMER_PROFILE()` 和 `PRODUCT_BRIEF()` 规则仍处于 Draft for testing，尚未通过真实案例验证。
- `ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 规则仍处于 Draft for testing，尚未通过真实案例验证。
- 本次更新的 6 个个人生产力 Skill 仍处于 Draft for testing，尚未通过真实案例验证。
- `ROUTE()` 仍处于 Draft for testing，需重点验证是否会推荐过多 Skill，以及能否在关键参数缺失时停止。
- 尚未升级的其余 Skill 业务规则仍需补充或确认。
- 真实脱敏示例和实际测试结果尚未建立，不能据此宣称 Skill 已可稳定使用。
- WorkBuddy 及其他平台格式尚未验证。
- 许可证和作者信息尚未确认。

## 下一步

优先用 5 个真实复杂案例测试 `ROUTE()`。重点检查是否会推荐过多 Skill，以及是否能在关键参数缺失时停止。
