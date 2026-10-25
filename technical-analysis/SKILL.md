---
name: ashare-technical-analysis
description: 面向沪深北 A 股的技术分析，要求可追溯数据、明确单位和覆盖范围。
---

# 技术分析

先阅读 `../references/data-contract.md`。使用 ashare MCP，不需要 Distilla 账户。

## 研究重点

前复权价格、趋势、RSI、MACD、量能与交易制度约束。

## 执行流程

1. 确认证券、区间和研究目标。默认沪深北 A 股、人民币、Asia/Shanghai，以数据库最新交易日为准。
2. 调用 `list_queryable_entities` 和 `describe_queryable_entities`，检查实际覆盖及 is_demo。先解析公司 ID、证券代码，再做依赖查询。
3. 按研究重点整理证据。财务实际值连接 time_period 与 financial_metric，区分累计/单季、归母/合并、扣非/净利；对比必须同口径。
4. 筛选工具仅为本地词项匹配，不是语义模型。轮询到 done/error，记录 coverage，不能把分数当投资评级。
5. 缺失数据标“未覆盖”。行情及部分财务可由用户同步；研报、一致预期、电话会和 KUs 需合法导入，不能假定已覆盖。
6. 复核关键数字的来源、时点、单位与反证。必要时向用户询问关键假设，不能自行补造。

可用 `scripts/technical.py prices.csv` 计算指标。输入 date、adjusted_close、volume，至少 250 个独立交易日。

## 专项检验

- 优先数据：stock_price；本地technical.py。先 describe 核对字段和覆盖。
- 核验方法：调整历史一致性先于指标计算。区分指标数值与信号，信号标触发日；MACD、RSI需充分预热，停牌和零成交要披露。
- 专项交付：列趋势、均线、RSI、MACD、量能及冲突信号；未回测则不报胜率或收益承诺。

## 输出

- 中文结论、范围、最新数据日、覆盖及局限。
- 指标或证据表：数值、单位、报告期、口径、来源链接和发布时间。
- 驱动因素、反证、待验证问题和风险。估算列公式与假设。
- 涨跌停、ST、北交所、新股规则应按证券和日期核实，不能统一套用 10%/20%。
- 不把虚构数据、词项评分或缺失样本作为交易建议。
