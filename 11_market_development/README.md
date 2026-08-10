# WorkFn 目标市场客户开发

本模块帮助用户基于真实业务证据选择目标市场、定义目标客户、规划人工搜索、筛选候选公司并设计联系路径。它是研究与判断辅助系统，不是自动获客、批量抓取或自动外联工具。

## 适用与不适用

适用于新市场验证、细分客户开发、人工搜索前规划、候选公司筛选和联系人路径设计。不适用于持续监控账户、批量抓取名单、猜测邮箱、自动群发、自动写入作战池或用公开标签替代采购证据。

## 五个 Skill

| Skill | 职责 | 关键产出 |
|---|---|---|
| `zayn-market-opportunity` | 判断市场是否值得进入 | 重点开发/先测试/暂不进入、风险、验证动作 |
| `zayn-target-customer-profile` | 定义应寻找的客户 | 具体客户类型、采购场景、匹配与排除信号 |
| `zayn-search-strategy` | 规划人工搜索 | 平台关键词、搜索顺序、结果判断标准 |
| `zayn-company-screening` | 筛选人工提供的候选公司 | 去重、证据、优先级、排除原因、下一步 |
| `zayn-contact-strategy` | 规划联系路径 | 部门、岗位、查找路径、开发角度、可信度 |

推荐顺序：

```text
产品和业务资料
→ MARKET_OPPORTUNITY()
→ TARGET_CUSTOMER_PROFILE()
→ SEARCH_STRATEGY()
→ 人工搜索
→ COMPANY_SCREENING()
→ 人工确认
→ CONTACT_STRATEGY()
```

不需要每次运行全部五个 Skill；已有明确市场或公司时，从对应步骤开始。

## 输入与输出

把产品、公司、历史订单、询价、报价、客户记录、搜索截图/文本、Excel 或 CSV 放入 `input/`，或在对话中明确提供路径。每次输出写入 `output/YYYY-MM-DD_任务名/`，不得覆盖旧结果。

所有输出区分：已确认事实、有依据的判断、待确认信息、AI 推测；注明来源与下一步。证据等级见 `config/evidence-rules.md`，筛选和输出规则见同目录其他配置。

## 人工确认节点

必须由用户确认：目标市场进入选择、客户画像是否符合业务、搜索关键词是否适合当地语境、候选公司是否进入下一步、联系人是否可信、是否联系及发送什么内容。系统不得自动外联。

## 与现有 WorkFn 联动

- 行业宏观研究：`zayn-market-research`
- 企业主体核验：`zayn-company-research`
- 公司与我方能力匹配：`zayn-company-fit`
- 既有客户事实画像：`zayn-customer-profile`
- 投入资格与优先级：`zayn-qualify`、`zayn-priority`
- 询价与报价：`zayn-rfq`、`zayn-price`、`zayn-quote`
- 对外沟通：`zayn-followup`、`zayn-reply`、`zayn-relation`
- 过程记录：`zayn-daily-report`

典型衔接：

```text
目标市场客户开发
→ COMPANY_RESEARCH()/COMPANY_FIT()
→ QUALIFY()
→ RFQ()/QUOTE()
→ FOLLOWUP()/REPLY()
→ DAILY_REPORT()
```

## 最小示例

“针对 DDR4 64GB 3200 RDIMM，结合我提供的历史询价和供应条件，先判断俄罗斯市场是否只适合测试，并建立目标客户画像。”

没有真实资料时仅输出参数缺口和验证计划，不把示例数据当事实。

## 常见错误和限制

不要因市场规模大就推荐进入；不要用官网产品词证明采购；不要把 LinkedIn 岗位当成交证据；不要为凑 5–10 家保留低质量公司；不要把推测邮箱当已验证；不要自动加入作战池或发送消息。
