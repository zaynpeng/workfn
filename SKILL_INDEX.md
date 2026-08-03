# Skill Index

| 分类 | Skill ID | Display Name | 中文名称 | 用途 | 当前状态 | 优先级 |
|---|---|---|---|---|---|---|
| Skill Orchestration | zayn-route | ROUTE() | Skill 路由与编排 | 识别问题，选择合适的 Skill，安排调用顺序、参数传递和停止条件 | 等待测试 | P0 |
| 客户沟通 | zayn-reply | REPLY() | 客户回复 | 根据客户原话、事实和目标，检查风险并决定如何回复 | Draft for testing | P0 |
| 客户沟通 | zayn-followup | FOLLOWUP() | 客户跟进 | 判断是否应该跟进、何时跟进以及跟进什么 | Draft for testing | P0 |
| 客户沟通 | zayn-clarify | CLARIFY() | 需求澄清 | 识别客户需求中缺失的关键信息并生成澄清方向 | Draft for testing | P1 |
| 客户沟通 | zayn-push | PUSH() | 推进成交 | 判断商机卡点并设计最小下一步动作 | Draft for testing | P3 |
| 客户沟通 | zayn-decline | DECLINE() | 拒绝与边界表达 | 无法满足要求时，清晰表达边界并避免制造错误期待 | Draft for testing | P3 |
| 客户沟通 | zayn-apology | APOLOGY() | 道歉与问题说明 | 出现问题时判断事实、责任和解决方案表达 | Draft for testing | P3 |
| 客户沟通 | zayn-relation | RELATION() | 客户关系维护 | 无具体询价时设计有价值的轻量联系 | Draft for testing | P3 |
| 客户沟通 | zayn-intent-decode | INTENT_DECODE() | 客户意图解读 | 从客户原话和上下文中区分明确表达、潜在关注点、可能意图和待确认事项 | Draft for testing | P1 |
| 询价与报价 | zayn-rfq | RFQ() | 询价判断 | 判断询价是否值得投入以及下一步处理方式 | Draft for testing | P0 |
| 询价与报价 | zayn-quote | QUOTE() | 报价检查 | 检查报价是否完整、可执行且不会引起误解 | Draft for testing | P1 |
| 询价与报价 | zayn-price | PRICE() | 价格策略 | 综合客户、市场、成本和风险判断报价策略 | Draft for testing | P2 |
| 询价与报价 | zayn-negotiate | NEGOTIATE() | 价格谈判 | 判断降价、换方案、交换条件或坚持价格 | Draft for testing | P2 |
| 询价与报价 / 硬件 | zayn-alternative | ALTERNATIVE() | 硬件替代方案 | 对比硬件、设备、备件和二手产品的型号、PN、兼容、成色与供应风险 | Draft for testing | P2 |
| 询价与报价 / 通用 | zayn-general-alternative | GENERAL_ALTERNATIVE() | 通用替代方案 | 跨行业比较产品、服务、材料、供应商或执行方案的替代差异与风险 | Draft for testing | P2 |
| 询价与报价 / 硬件 | zayn-availability | AVAILABILITY() | 硬件货源与库存判断 | 规范硬件现货、调货、锁货、成色、照片与序列号证据 | Draft for testing | P3 |
| 询价与报价 / 通用 | zayn-general-availability | GENERAL_AVAILABILITY() | 通用可用性判断 | 判断产品、服务、人员、场地、产能或预算的可用状态与条件 | Draft for testing | P3 |
| 询价与报价 / 硬件 | zayn-condition | CONDITION() | 硬件成色判断 | 规范全新、拆机、翻新、二手等硬件成色表达 | Draft for testing | P3 |
| 询价与报价 / 通用 | zayn-general-condition | GENERAL_CONDITION() | 通用状态与质量判断 | 依据适用检验或验收证据判断对象状态、缺陷和使用限制 | Draft for testing | P3 |
| 订单与交付 | zayn-order | ORDER() | 订单确认 | 下单前检查订单执行条件是否完整 | Draft for testing | P3 |
| 订单与交付 | zayn-delivery | DELIVERY() | 交付计划 | 形成采购、QC、包装和物流交付计划 | Draft for testing | P3 |
| 订单与交付 | zayn-delay | DELAY() | 交期异常 | 识别延期风险并设计客户沟通和替代方案 | Draft for testing | P2 |
| 订单与交付 | zayn-shipment | SHIPMENT() | 发货通知 | 检查发货信息是否齐全并生成通知结构 | Draft for testing | P3 |
| 订单与交付 | zayn-payment | PAYMENT() | 付款跟进 | 根据付款状态判断提醒方式和风险边界 | Draft for testing | P2 |
| 订单与交付 / 硬件 | zayn-order-kickoff | ORDER_KICKOFF() | 硬件订单启动协调 | 核对硬件货源、兼容、固件、测试、序列号、包装和清关责任 | Draft for testing | P0 |
| 订单与交付 / 通用 | zayn-general-order-kickoff | GENERAL_ORDER_KICKOFF() | 通用订单与项目启动 | 组织产品订单、服务合同或项目的范围、里程碑、验收和责任分工 | Draft for testing | P0 |
| 投诉与售后 / 硬件 | zayn-complaint | COMPLAINT() | 硬件客诉分析 | 基于序列号、测试、兼容、运输和保修证据分析硬件投诉 | Draft for testing | P1 |
| 投诉与售后 / 通用 | zayn-general-complaint | GENERAL_COMPLAINT() | 通用投诉分析 | 分析产品、服务、订阅或项目投诉的事实、证据和处理阶段 | Draft for testing | P1 |
| 投诉与售后 / 硬件 | zayn-rma | RMA() | 硬件 RMA 判断 | 根据序列号、测试、保修、退运与清关条件判断硬件 RMA | Draft for testing | P3 |
| 投诉与售后 / 通用 | zayn-general-rma | GENERAL_RMA() | 通用退换与补救受理 | 判断退换、重做、退款、取消或其他补救请求的受理路径 | Draft for testing | P3 |
| 投诉与售后 / 硬件 | zayn-responsibility | RESPONSIBILITY() | 硬件责任边界 | 依据测试、兼容、运输安装和保修边界判断硬件售后责任 | Draft for testing | P2 |
| 投诉与售后 / 通用 | zayn-general-responsibility | GENERAL_RESPONSIBILITY() | 通用责任边界 | 依据合同、履约和因果证据判断跨行业责任状态 | Draft for testing | P2 |
| 投诉与售后 / 硬件 | zayn-solution | SOLUTION() | 硬件售后方案 | 比较硬件排查、维修、换货、补发、退款和延保方案 | Draft for testing | P3 |
| 投诉与售后 / 通用 | zayn-general-solution | GENERAL_SOLUTION() | 通用问题解决方案 | 比较修复、重做、退款、抵扣、支持等跨行业补救方案 | Draft for testing | P3 |
| 客户管理 | zayn-qualify | QUALIFY() | 客户资格判断 | 基于真实业务证据判断客户是否值得投入 | Draft for testing | P3 |
| 客户管理 | zayn-segment | SEGMENT() | 客户分层 | 基于证据对客户进行分层，允许保留未判断 | Draft for testing | P3 |
| 客户管理 | zayn-priority | PRIORITY() | 今日客户优先级 | 判断每天应该优先推进哪些客户 | Draft for testing | P3 |
| 客户管理 | zayn-opportunity | OPPORTUNITY() | 商机判断 | 区分普通询价、真实项目和长期机会 | Draft for testing | P3 |
| 客户管理 | zayn-lost | LOST() | 丢单复盘 | 基于证据分析丢单原因，避免简单归因 | Draft for testing | P3 |
| 客户管理 | zayn-reactivate | REACTIVATE() | 沉睡客户激活 | 判断哪些老客户值得重新联系 | Draft for testing | P3 |
| 客户管理 | zayn-account | ACCOUNT() | 客户策略 | 为重点客户制定阶段性推进策略 | Draft for testing | P3 |
| 客户管理与销售策略 | zayn-customer-profile | CUSTOMER_PROFILE() | 客户画像 | 基于真实业务记录和公开资料整理客户事实、采购方向、合作历史和信息缺口 | Draft for testing | P1 |
| 内部协作 | zayn-report | REPORT() | 通用汇报识别与路由 | 识别汇报类型并路由日报、周报、月报、年中报告、年度报告、升级、决策或通用项目汇报 | Draft for testing | P1 |
| 内部协作 | zayn-daily-report | DAILY_REPORT() | 日报推进与结果检查 | 区分当天动作与结果，检查状态、等待、下一步和截止时间 | Draft for testing | P1 |
| 内部协作 | zayn-weekly-report | WEEKLY_REPORT() | 周报复盘与业务推进分析 | 分析一周结果密度、等待、关闭能力与资源分配 | Draft for testing | P1 |
| 内部协作 | zayn-monthly-report | MONTHLY_REPORT() | 月报复盘与业务结果分析 | 复盘月度目标达成、关键成果、结果密度、等待阻塞和下月重点 | Draft for testing | P1 |
| 内部协作 | zayn-midyear-report | MIDYEAR_REPORT() | 年中复盘与下半年策略分析 | 复盘半年目标达成、结构性问题、资源配置和下半年策略 | Draft for testing | P1 |
| 内部协作 | zayn-annual-report | ANNUAL_REPORT() | 年度复盘与下一年度规划 | 复盘年度目标达成、关键成果、业务结构、能力成长和下一年度计划 | Draft for testing | P1 |
| 内部协作 | zayn-cross-functional-collaboration | CROSS_FUNCTIONAL_COLLABORATION() | 跨部门协同 | 整理跨部门事项中的事实、缺失信息、风险、责任边界、下一步动作和内部沟通版本 | Draft for testing | P1 |
| 内部协作 | zayn-request | REQUEST() | 内部请求 | 向采购、工程、财务等提出完整请求 | Draft for testing | P3 |
| 内部协作 | zayn-escalate | ESCALATE() | 问题升级 | 判断问题是否需要升级以及如何汇报 | Draft for testing | P3 |
| 内部协作 | zayn-decision | DECISION() | 决策请求 | 向领导提供选项、风险和建议 | Draft for testing | P3 |
| 内部协作 | zayn-meeting | MEETING() | 会议准备 | 会前整理目标、议题、数据和结论 | Draft for testing | P3 |
| 内部协作 | zayn-minutes | MINUTES() | 会议纪要 | 整理结论、责任人、截止时间和待确认事项 | Draft for testing | P3 |
| 内部协作 | zayn-handover | HANDOVER() | 工作交接 | 将事项、状态、责任和下一步完整移交 | Draft for testing | P3 |
| 内部协同 | zayn-keypoint | KEYPOINT() | 重点梳理 | 从大量信息中提炼核心结论、关键问题、风险和下一步 | Draft for testing | P1 |
| 个人生产力 | zayn-learn | LEARN() | 学习计划 | 判断学习目标是否可执行并补齐路径 | Draft for testing | P3 |
| 个人生产力 | zayn-read | READ() | 阅读转化 | 把收藏内容转化为问题、行动和实践 | Draft for testing | P3 |
| 个人生产力 | zayn-practice | PRACTICE() | 实践转化 | 把想法转化为最小可执行实验 | Draft for testing | P3 |
| 个人生产力 | zayn-review | REVIEW() | 复盘 | 基于目标、结果和证据形成下一次调整 | Draft for testing | P3 |
| 个人生产力 | zayn-plan | PLAN() | 计划拆解 | 把模糊目标拆成可执行步骤 | Draft for testing | P3 |
| 个人生产力 | zayn-focus | FOCUS() | 任务减重 | 检查任务是否过度复杂并找到最小可用版本 | Draft for testing | P3 |
| 平台专用 / Alibaba | zayn-ali-rfq-scan | ALI_RFQ_SCAN() | 阿里 RFQ 市场筛选 | 在 Alibaba RFQ 市场中批量筛选值得点开、报价和投入时间的机会 | Draft for testing | P3 |
| 平台专用 / Alibaba | zayn-ali-rfq-bid | ALI_RFQ_BID() | 阿里 RFQ 报价 | 将已确认的产品、价格和条款整理为 Alibaba RFQ 报价表单内容 | Draft for testing | P3 |
| 产品理解与技术判断 / IT 硬件 | zayn-product-brief | PRODUCT_BRIEF() | IT 硬件产品速览 | 整理服务器、存储、GPU、网络设备等硬件的型号、PN、规格、兼容与采购风险 | Draft for testing | P1 |
| 产品理解与技术判断 / 通用 | zayn-general-product-brief | GENERAL_PRODUCT_BRIEF() | 通用产品与服务速览 | 整理实体产品、数字产品或服务的用途、能力、版本和信息缺口 | Draft for testing | P1 |
