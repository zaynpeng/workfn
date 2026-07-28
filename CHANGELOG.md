# Changelog

## v0.1.0

- 建立 WorkFn 项目骨架。
- 建立 7 个分类、43 个 Skill 文件夹和标准文档。
- 建立模板、完整索引、开发规范和本地发布准备说明。
- 完成 `REPLY()` 的 `v0.1` 测试规范与测试要求。
- 完成 `FOLLOWUP()` 的 `v0.1` 测试规范与测试要求。
- 新增 `CUSTOMER_PROFILE()` 客户画像 Skill。
- 新增 `PRODUCT_BRIEF()` 产品速览 Skill。
- 新增 `ALI_RFQ_SCAN()` 阿里 RFQ 市场筛选 Skill。
- 新增 `ALI_RFQ_BID()` 阿里 RFQ 报价 Skill。
- 新增 `INTENT_DECODE()`、`KEYPOINT()`、`ORDER_KICKOFF()` 三个 Skill 文件骨架。
- 新增 `SKILL_RUNTIME_PROTOCOL.md`，并为所有 Skill 增加统一参数解析与正式分析触发机制。
- 完成 `APOLOGY()`、`CLARIFY()`、`DECLINE()`、`PUSH()`、`RELATION()` 和 `INTENT_DECODE()` 的 `v0.1` 初版规则。
- 合并 `REPLY()`、`FOLLOWUP()` 完整版提示词中的最低运行条件，保留原有详细规则。
- 完成 `RFQ()`、`QUOTE()`、`PRICE()`、`NEGOTIATE()`、`ALTERNATIVE()`、`AVAILABILITY()` 和 `CONDITION()` 的 `v0.1` 初版规则。
- 完成 `ORDER()`、`ORDER_KICKOFF()`、`DELIVERY()`、`DELAY()`、`PAYMENT()` 和 `SHIPMENT()` 的 `v0.1` 初版规则。
- 完成 `COMPLAINT()`、`RESPONSIBILITY()`、`RMA()` 和 `SOLUTION()` 的 `v0.1` 初版规则。
- 完成客户管理类 `QUALIFY()`、`SEGMENT()`、`PRIORITY()`、`OPPORTUNITY()`、`LOST()`、`REACTIVATE()`、`ACCOUNT()` 初版规则，并合并 `CUSTOMER_PROFILE()` 完整版要求。
- 完成内部协作类 `REPORT()`、`REQUEST()`、`ESCALATE()`、`DECISION()`、`MEETING()`、`MINUTES()`、`HANDOVER()` 和 `KEYPOINT()` 初版规则。
- 完成个人生产力类 `REVIEW()`、`FOCUS()`、`LEARN()`、`PLAN()`、`PRACTICE()` 和 `READ()` 初版规则。
- 合并 `PRODUCT_BRIEF()`、`ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 完整版提示词要求，保留原有详细业务规则。
- 新增 `ROUTE()` Skill 路由与编排，以及 `00_skill_orchestration` 项目级分类。
- 为所有 Skill 增加统一的 `zayn-` 正式 Skill ID，并保留原函数式展示名称和中文名称。
- 将 `REPLY()`、`FOLLOWUP()`、`ALI_RFQ_SCAN()` 和 `ALI_RFQ_BID()` 升级至 `v0.2.0` 最新规则，补充最新参数、最低运行条件、双运行模式、停止条件、职责边界、场景案例和协议测试。
- 尚未补充真实案例、测试结果或平台适配。
