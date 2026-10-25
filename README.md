# AShare Skills

37 个面向沪深北 A 股重新编写的研究技能，搭配同级 ashare-server 和 ashare-mcp。独立项目，与 Distilla 无隶属关系；未复制其未声明许可证的技能文本或脚本。

## Codex 使用

按后端 README 配置本地 MCP，在 Codex 中输入：

> 读取本仓库 company-brief/SKILL.md，按流程研究 600519.SH。

直接指定 SKILL.md 路径不依赖客户端自动发现。可按客户端版本的技能安装方式安装，需保留整个仓库目录结构，因为技能引用共享 references 和脚本。

DCF 和技术指标脚本为原创实现。DCF 接受已确认现金流，不自动产生预测。

```bash
python3 scripts/validate.py
```

## 技能目录

- [技术看多信号](bull-signal-screen/SKILL.md)：RSI、MACD、均线、成交量和突破，识别停牌和涨跌停影响。
- [产能利用率](capacity-utilization/SKILL.md)：设计产能、有效产能、产量、爬坡、订单和单位成本。
- [资本开支周期](capex-cycle/SKILL.md)：扩产计划、在建工程、转固、折旧与现金回收。
- [公司简报](company-brief/SKILL.md)：业务构成、收入来源、竞争地位、业绩、公告、估值与风险。
- [竞争地位](competitive-position/SKILL.md)：份额、成本优势、客户锁定、替代风险与竞争强度。
- [消费品牌力](consumer-brand-equity/SKILL.md)：品牌溢价、渠道库存、复购、营销效率与价格带。
- [周期定位](cycle-positioning/SKILL.md)：供需、库存、价格、利用率、资本开支与盈利周期。
- [每日市场简报](daily-brief/SKILL.md)：中国交易日、指数及行业表现、重要公告与市场事件。
- [现金流折现建模](dcf-modeling/SKILL.md)：确认基准乐观悲观现金流、WACC、永续增长、净债务及股本。
- [渠道研究](distribution-channels/SKILL.md)：直营经销结构、终端动销、库存、账期与渠道利润。
- [财报摘要](earnings-digest/SKILL.md)：累计与单季口径、同比环比、业绩预告、经营驱动与现金流。
- [财报前瞻](earnings-preview/SKILL.md)：披露日、业绩预告、预测依据、预期差与待验证问题。
- [盈利预测修正](earnings-revisions/SKILL.md)：同口径预测历史版本、样本数量、修正幅度与原始研报。
- [财务报表审阅](financial-statement-review/SKILL.md)：收入质量、归母及扣非净利、现金流、应收存货、负债与非经常损益。
- [基本面综合研究](fundamental-guru/SKILL.md)：业务质量、财务质量、治理、资本配置、估值及可证伪命题。
- [增长画像](growth-profile/SKILL.md)：量价拆分、内生外延增长、订单兑现与利润弹性。
- [行业研究](industry-analysis/SKILL.md)：申万或中信分类、产业链、市场规模、监管、供需与竞争。
- [初步筛选](initial-screen/SKILL.md)：沪深北范围、最新交易日、ST退市状态、流动性及财务门槛。
- [多空论点](long-short-ideas/SKILL.md)：多空证据、催化剂、估值敏感性及融券可得性，不假设可自由做空。
- [管理与治理](management-governance/SKILL.md)：实控人、国资属性、质押、关联交易、激励、减持与审计意见。
- [制造成本结构](manufacturing-cost-structure/SKILL.md)：原料、能源、人工、折旧、规模效应、成本转嫁与良率。
- [同业对标](peer-benchmarking/SKILL.md)：分类口径、业务可比性、增长、利润率、现金回报与估值。
- [利润池分析](profit-pool-analysis/SKILL.md)：产业链利润分布、议价权、资本强度与利润迁移。
- [ROE拆解](roe-decomposition/SKILL.md)：净利率、资产周转率和权益乘数，使用平均资产权益并解释少数股东差异。
- [行业价格驱动模式](sector-price-driver-patterns/SKILL.md)：价格指标与收益率、领先滞后、样本外检验，区分相关和因果。
- [行业价格驱动复盘](sector-price-driver-review/SKILL.md)：价格窗口、行业因素、公告证据、事件去重与解释置信度。
- [卖方研报摘要](sell-side-brief/SKILL.md)：合法导入研报的日期、机构、核心假设、估值方法与分歧。
- [卖方观点比较](sell-side-view/SKILL.md)：不同机构、报告日期、评级、盈利预测口径与估值分歧。
- [情绪解读](sentiment-read/SKILL.md)：可验证新闻公告、市场反应、样本范围与叙事偏差。
- [特殊情形筛选](special-situations-screen/SKILL.md)：重组、要约、回购、分拆、控制权变更、解禁与退市风险。
- [条件选股](stock-screener/SKILL.md)：显式条件、时点、数值阈值、覆盖率及结果复核。
- [供应链韧性](supply-chain-resilience/SKILL.md)：供应集中度、国产替代、关键材料、贸易约束与替代方案。
- [技术分析](technical-analysis/SKILL.md)：前复权价格、趋势、RSI、MACD、量能与交易制度约束。
- [技术竞争地位](technology-position/SKILL.md)：研发强度、专利质量、技术路线、良率与商业化验证。
- [主题受益者](thematic-winners/SKILL.md)：政策到收入利润的传导、直接间接受益、证据与拥挤风险。
- [估值压缩与修复](valuation-compression-recovery/SKILL.md)：盈利预期、风险溢价、历史估值、资本回报和重估条件。
- [社交讨论研究](x-discourse/SKILL.md)：仅分析用户合法提供的有时间范围样本，区分观点事实与抽样偏差。
