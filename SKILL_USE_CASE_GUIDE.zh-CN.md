# WorkFn Skill 使用场景指南

本指南帮助用户快速判断：

1. 当前问题应该使用哪个 Skill
2. 这个 Skill 能解决什么问题
3. 它适合在哪些业务场景使用
4. 什么情况下需要先补充信息或转到其他 Skill

## 如何选择 Skill

优先选择一个能够直接解决当前问题的 Skill。只有后一步确实依赖前一步结果时，才组合多个 Skill。

如果仍然不知道该选哪个，可以使用：

```text
zayn-route
Display Name: ROUTE()
```

调用时建议提供：

- 当前遇到的问题
- 最终希望得到的结果
- 已有材料和已确认事实
- 当前处于理解、判断、执行、沟通还是复盘阶段

## 00 路由与编排

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-route` | `ROUTE()` | 不知道该使用哪个 Skill，或需要安排多个 Skill 的先后顺序 | 复杂问题分阶段处理；确定当前先做什么；设置参数传递和停止条件 |

## 01 客户沟通

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-reply` | `REPLY()` | 在事实、边界和沟通目标明确后生成客户回复 | 回复询价、解释情况、确认下一步；生成 Email、WhatsApp 或 WeChat 版本 |
| `zayn-followup` | `FOLLOWUP()` | 判断是否应该跟进、何时跟进以及跟进什么 | 报价后未回复；项目停滞；判断提醒、补充价值还是暂停投入 |
| `zayn-clarify` | `CLARIFY()` | 找出需求中缺失的关键信息并设计澄清问题 | 型号、数量、用途、预算或交期不清；客户描述过于笼统 |
| `zayn-push` | `PUSH()` | 识别成交卡点并设计最小推进动作 | 客户迟迟不决定；样品、价格、技术或付款环节卡住 |
| `zayn-decline` | `DECLINE()` | 清晰拒绝无法满足的要求，同时维护合作边界 | 无法接受付款方式、价格、交期、责任或不合理要求 |
| `zayn-apology` | `APOLOGY()` | 在问题发生后组织道歉、事实说明和解决方向 | 发错货、回复延迟、交期异常、信息错误或服务失误 |
| `zayn-relation` | `RELATION()` | 在没有具体询价时进行有价值的轻量联系 | 节日问候、行业信息分享、老客户关系维护 |
| `zayn-intent-decode` | `INTENT_DECODE()` | 区分客户明确表达、潜在关注点和待确认事项 | 客户说法含糊、语气复杂、同时提出多个要求或可能存在隐藏顾虑 |

## 02 询价与报价

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-rfq` | `RFQ()` | 判断一条询价是否真实、完整和值得投入 | 收到新询价；决定是否找货、核价、投入工程资源 |
| `zayn-quote` | `QUOTE()` | 检查报价是否完整、可执行且不会造成误解 | 报价发送前检查产品、数量、价格、币种、条款和有效期 |
| `zayn-price` | `PRICE()` | 综合成本、客户、市场和风险制定价格策略 | 首次报价、阶梯价格、目标利润、价格有效期和让价空间设计 |
| `zayn-negotiate` | `NEGOTIATE()` | 判断应该降价、换方案、交换条件还是坚持价格 | 客户压价；竞争对手更低；需要以数量、付款或交期换价格 |
| `zayn-alternative` | `ALTERNATIVE()` | 比较硬件、设备、备件和二手产品的替代差异 | 原型号缺货、PN 替代、配置兼容、成色或保修变化 |
| `zayn-general-alternative` | `GENERAL_ALTERNATIVE()` | 跨行业比较产品、服务或执行方案的替代选项 | 更换材料、服务商、方案、流程或交付方式 |
| `zayn-availability` | `AVAILABILITY()` | 判断硬件现货、调货、锁货和供应证据 | 硬件库存、成色、照片、SN 和供应商反馈确认 |
| `zayn-general-availability` | `GENERAL_AVAILABILITY()` | 判断产品、服务、人员、场地或产能是否可用 | 预约、排期、资源确认、部分可用或信息过期 |
| `zayn-condition` | `CONDITION()` | 判断硬件及二手设备成色 | 全新、拆机、翻新、二手、库存新件及保修状态 |
| `zayn-general-condition` | `GENERAL_CONDITION()` | 判断任意产品或交付物的状态与质量 | 外观、功能、完整性、检验、缺陷和适用限制 |

## 03 订单与交付

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-order` | `ORDER()` | 下单前检查订单执行条件是否完整 | 核对产品、数量、价格、付款、收货、交期和特殊要求 |
| `zayn-order-kickoff` | `ORDER_KICKOFF()` | 启动硬件、设备或备件订单 | 协调采购、工程、QC、包装、物流与清关 |
| `zayn-general-order-kickoff` | `GENERAL_ORDER_KICKOFF()` | 启动通用产品订单、服务合同或项目 | 明确范围、里程碑、验收、依赖、责任和沟通机制 |
| `zayn-delivery` | `DELIVERY()` | 制定采购、质检、包装和物流交付计划 | 安排里程碑、责任人、截止时间和风险检查点 |
| `zayn-delay` | `DELAY()` | 识别延期风险并设计补救和客户沟通方案 | 供应商延期、生产延误、物流异常、承诺日期可能无法实现 |
| `zayn-shipment` | `SHIPMENT()` | 检查发货信息并生成完整发货通知 | 提供箱数、重量、物流方式、单号、文件和预计到达时间 |
| `zayn-payment` | `PAYMENT()` | 根据付款状态判断提醒方式和风险边界 | 定金未付、尾款逾期、付款凭证待确认或账期临近 |

## 04 投诉与售后

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-complaint` | `COMPLAINT()` | 分析硬件、设备和备件投诉 | 序列号、测试、兼容、运输、安装或保修问题 |
| `zayn-general-complaint` | `GENERAL_COMPLAINT()` | 分析通用产品、服务或项目投诉 | 结果不符、服务中断、范围争议、交付或体验投诉 |
| `zayn-responsibility` | `RESPONSIBILITY()` | 判断硬件售后责任边界 | 测试、安装、兼容、运输、保修或供应商责任不清 |
| `zayn-general-responsibility` | `GENERAL_RESPONSIBILITY()` | 判断通用履约责任边界 | 合同范围、客户配合、第三方依赖或因果关系不清 |
| `zayn-rma` | `RMA()` | 判断硬件 RMA 与退运检测条件 | 序列号核对、保修、返修、换货、运费和清关 |
| `zayn-general-rma` | `GENERAL_RMA()` | 判断通用退换、重做、退款或取消请求 | 产品退换、服务重做、项目返工或订阅取消 |
| `zayn-solution` | `SOLUTION()` | 比较硬件排查、维修、换货和延保方案 | 硬件售后事实和责任基本明确后选择解决方案 |
| `zayn-general-solution` | `GENERAL_SOLUTION()` | 比较跨行业补救方案 | 修复、重做、退款、抵扣、延期、培训或支持方案 |

## 05 客户管理与销售策略

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-customer-profile` | `CUSTOMER_PROFILE()` | 基于真实记录整理客户事实、采购方向和信息缺口 | 建立客户档案；会前了解客户；整理合作历史和公开资料 |
| `zayn-qualify` | `QUALIFY()` | 判断客户是否值得继续投入资源 | 新客户筛选；识别真实买家、无效询盘或高风险客户 |
| `zayn-segment` | `SEGMENT()` | 根据证据进行客户分层 | 划分重点客户、成长客户、普通客户和待观察客户 |
| `zayn-priority` | `PRIORITY()` | 判断今天应该优先推进哪些客户 | 每日客户清单排序；在有限时间内安排跟进顺序 |
| `zayn-opportunity` | `OPPORTUNITY()` | 判断普通询价是否已形成真实商机 | 识别明确项目、采购时间、预算、决策链和长期机会 |
| `zayn-lost` | `LOST()` | 基于证据复盘丢单原因 | 价格落败、技术不匹配、响应慢、交期问题或客户项目取消 |
| `zayn-reactivate` | `REACTIVATE()` | 判断哪些沉睡客户值得重新联系 | 激活长期未联系客户；利用新库存、价格或方案重新建立联系 |
| `zayn-account` | `ACCOUNT()` | 为重点客户制定阶段性策略 | 大客户经营、年度目标、关系地图、机会组合和资源投入计划 |

## 06 内部协作

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-keypoint` | `KEYPOINT()` | 从大量信息中提炼结论、问题、风险和下一步 | 长聊天记录、项目资料、邮件线程或跨部门信息整理 |
| `zayn-report` | `REPORT()` | 识别汇报类型并路由到日报、周报、月报、年中报告、年度报告或通用项目汇报 | 不确定该用哪种汇报；项目进展、销售汇报、异常说明和管理层更新 |
| `zayn-daily-report` | `DAILY_REPORT()` | 将当天记录转为结果、状态、下一步、负责人和期限 | 日报、下班汇报、当天复盘、检查今日哪些事项没有有效推进 |
| `zayn-weekly-report` | `WEEKLY_REPORT()` | 分析一周结果密度、等待事项、关闭能力和资源分配 | 周报、周会汇报、多份日报汇总、忙但结果少的复盘 |
| `zayn-monthly-report` | `MONTHLY_REPORT()` | 复盘月度目标达成、关键成果、结果密度、等待阻塞和下月重点 | 月报、月会汇报、月度业务复盘、整月成果与问题分析 |
| `zayn-midyear-report` | `MIDYEAR_REPORT()` | 复盘上半年目标达成、结构性问题、资源配置和下半年策略 | 年中总结、半年复盘、上半年汇报、下半年计划 |
| `zayn-annual-report` | `ANNUAL_REPORT()` | 复盘年度目标达成、关键成果、业务结构、能力成长和下一年度计划 | 年度总结、年度述职、全年复盘、年报和明年计划 |
| `zayn-cross-functional-collaboration` | `CROSS_FUNCTIONAL_COLLABORATION()` | 整理跨部门事项中的事实、待确认信息、风险、责任边界、下一步动作和沟通版本 | 跨部门确认进度、请求补充信息、同步风险阻塞、避免过早承诺或推责表达 |
| `zayn-request` | `REQUEST()` | 向内部部门提出完整、可执行的请求 | 请求采购核价、工程确认、财务审核或仓库处理 |
| `zayn-escalate` | `ESCALATE()` | 判断问题是否需要升级以及如何升级 | 超出权限、重大延期、高额损失、客户升级投诉或跨部门阻塞 |
| `zayn-decision` | `DECISION()` | 向领导提供清晰的决策选项 | 需要审批价格、赔偿、付款条件、资源投入或项目取舍 |
| `zayn-upward-communication` | `UPWARD_COMMUNICATION()` | 把事实、建议和请求整理成上级可快速判断和回复的沟通内容 | 向经理或老板汇报、请示、申请审批、升级问题、申请资源、请假、反馈不同意见或讨论职业发展 |
| `zayn-meeting` | `MEETING()` | 在会前整理目标、议题、材料和预期结论 | 客户会议、项目启动会、内部评审和问题协调会 |
| `zayn-minutes` | `MINUTES()` | 整理会议结论、责任人、截止时间和待确认项 | 会后形成可执行纪要并跟踪行动项 |
| `zayn-handover` | `HANDOVER()` | 把事项、状态、风险和下一步完整交接 | 请假交接、岗位变动、销售转运营或项目负责人更换 |

## 07 个人生产力

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-learn` | `LEARN()` | 把学习目标转化为可执行路径 | 学习新产品、行业知识、软件工具或业务能力 |
| `zayn-read` | `READ()` | 把阅读内容转化为问题、结论和行动 | 处理收藏文章、报告、书籍章节和培训材料 |
| `zayn-practice` | `PRACTICE()` | 把想法转化为最小可执行实验 | 将课程知识用于工作；设计练习、验证方法和反馈节点 |
| `zayn-review` | `REVIEW()` | 基于目标、结果和证据进行复盘 | 项目复盘、销售复盘、周复盘、沟通失败或个人表现总结 |
| `zayn-plan` | `PLAN()` | 把模糊目标拆成可执行步骤 | 制定项目计划、周计划、学习计划和阶段性行动方案 |
| `zayn-focus` | `FOCUS()` | 减少任务复杂度并找到最小可用版本 | 任务过多、方案过重、迟迟无法开始或需要缩小范围 |

## 08 Alibaba 平台专用

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-ali-rfq-scan` | `ALI_RFQ_SCAN()` | 判断 Alibaba RFQ 是否值得点开、报价和消耗报价权益 | 批量浏览采购直达市场；选择快速响应、继续核实或跳过 |
| `zayn-ali-rfq-bid` | `ALI_RFQ_BID()` | 在决定参与后生成并检查平台报价字段 | 填写产品、价格、数量、成色、交期、贸易条款、保修和买家留言 |

## 09 产品理解

| Skill ID | Display Name | 解决什么问题 | 典型应用场景 |
|---|---|---|---|
| `zayn-product-brief` | `PRODUCT_BRIEF()` | 快速理解 IT 硬件及其采购关注点 | 服务器、存储、内存、SSD、GPU、网络设备和笔记本配件 |
| `zayn-general-product-brief` | `GENERAL_PRODUCT_BRIEF()` | 快速理解任意产品或服务 | 实体产品、数字产品、服务、订阅或组合方案的用途与信息缺口 |

## 常见问题快速入口

| 用户当前的问题 | 推荐 Skill |
|---|---|
| 不知道该用哪个 Skill | `ROUTE()` |
| 看不懂客户真正想表达什么 | `INTENT_DECODE()` |
| 客户需求不完整 | `CLARIFY()` |
| 需要直接回复客户 | `REPLY()` |
| 客户长时间没有回复 | `FOLLOWUP()` |
| 判断询价是否值得做 | `RFQ()` |
| 报价发送前检查 | `QUOTE()` |
| 客户要求降价 | `NEGOTIATE()` |
| 原型号缺货，需要替代 | `ALTERNATIVE()` |
| 订单是否具备执行条件 | `ORDER()` |
| 订单确认后需要内部启动 | `ORDER_KICKOFF()` |
| 交期可能延误 | `DELAY()` |
| 客户投诉并要求赔偿 | `COMPLAINT()` → `RESPONSIBILITY()` |
| 判断是否接受退货 | `RMA()` |
| 今天先跟进哪些客户 | `PRIORITY()` |
| 给领导汇报复杂项目 | `KEYPOINT()` → `REPORT()` |
| 写日报或下班总结 | `DAILY_REPORT()` |
| 写周报或周会汇报 | `WEEKLY_REPORT()` |
| 写月报或月度复盘 | `MONTHLY_REPORT()` |
| 写年中总结和下半年计划 | `MIDYEAR_REPORT()` |
| 写年度述职或明年计划 | `ANNUAL_REPORT()` |
| 跨部门协同推进、避免过早承诺或推责 | `CROSS_FUNCTIONAL_COLLABORATION()` |
| 需要领导做决定 | `DECISION()` |
| 任务太复杂、不知道怎么开始 | `FOCUS()` → `PLAN()` |
| 陌生产品需要快速理解 | `PRODUCT_BRIEF()` |
| Alibaba RFQ 是否值得报 | `ALI_RFQ_SCAN()` |
| 填写 Alibaba RFQ 报价 | `ALI_RFQ_BID()` |

## 常见组合路径

### 客户表达不清，需要最终回复

```text
INTENT_DECODE() → CLARIFY() → REPLY()
```

### 陌生产品询价

```text
PRODUCT_BRIEF() → CLARIFY() → RFQ()
```

确认值得投入后，再根据需要进入：

```text
PRICE() → QUOTE() → REPLY()
```

### 客户压价

```text
PRICE() → NEGOTIATE() → REPLY()
```

### 客诉退款

```text
COMPLAINT() → RESPONSIBILITY() → RMA() → SOLUTION() → REPLY()
```

### 订单启动与交付

```text
ORDER() → ORDER_KICKOFF() → DELIVERY()
```

### 复杂项目汇报与决策

```text
KEYPOINT() → REPORT() → DECISION()
```

### 跨部门协同后对外回复

```text
CROSS_FUNCTIONAL_COLLABORATION() → REPLY()
```

### 周期性工作汇报

```text
REPORT() → DAILY_REPORT() / WEEKLY_REPORT() / MONTHLY_REPORT() / MIDYEAR_REPORT() / ANNUAL_REPORT()
```

### Alibaba RFQ

```text
ALI_RFQ_SCAN() → ALI_RFQ_BID()
```

## 使用边界

1. 单个 Skill 足够时，不增加不必要的调用链。
2. 关键参数缺失时，先补充信息，不强行输出正式结论。
3. AI 推测只能标记为待验证，不能写成确定事实。
4. 人工已经确认的事实和判断优先。
5. 涉及多个 Skill 时，只传递下一个 Skill 必需的信息。
6. Skill 提供判断和表达支持，不自动替代业务授权和人工决策。
