# A 股数据约定

## 本地数据库与来源

先检查实体覆盖，不把 0 行称作全市场没有。拒绝把 is_demo=1 / fictional_demo 记录用于真实研究。缺失值不是 0，资料未覆盖不是业务不存在。每个关键结论给出来源、发布日期及数据库抓取时点。

优先证据：公司公告和交易所/巨潮原文 → 可追溯数据提供方 → 合法导入研报与公司交流。官网：上交所 sse.com.cn、深交所 szse.cn、北交所 bse.cn、巨潮 cninfo.com.cn。此项目不自动抓取所有公告，也不提供付费研报授权。

## 查询约定

- `query_entity(entity, select, filters, joins, sort, limit, filter_logic, offset)`。
- filters 为 `[{"field":"symbol","op":"=","value":"600519.SH"}]`；op 支持 =、!=、>、>=、<、<=、in、not in、like。filter_logic 支持 AND/OR，不能嵌套。
- joins 为 `[{"relation":"company"}]`，选择 `company.name`；财务使用 `time_period` 的别名 T、financial_metric 的 M，一致预期用 consensus_metric 的 C。
- 按 schema 提供的字段查询；`financial_data_point` 通过 `T.company_id` 过滤公司，不能凭空直连 company。
- 翻页保持相同过滤和排序，将 next_hint.offset 传回 offset，直到 truncated=false。跨页时不同时更新数据库。
- `aggregate_entity` 的 aggregates 为 `[{"function":"SUM","field":"value","alias":"total_sales"}]`，返回键 totalSales。having 使用原始 alias total_sales。
- 文本 value 在普通查询里按字典序比较；数字大小用 aggregate/having 或在 Python 显式转换。聚合自动去逗号并转数字。

## A 股单位与时间

代码保留 6 位：600519.SH、000001.SZ、920001.BJ。SH/SZ/BJ 是上市地，hq_country=CN 不区分注册地。ST 不是普通行业，行业分类必须注明体系和版本。

价格为 CNY/股，成交量为股（AKShare 来源的手已乘 100），change 为小数（0.05=5%）。adjusted_close 为前复权，用于收益率和技术指标，复权历史可能随分红变化，应同步同一时段，不拼接不同复权版本。

为保留公开 Distilla 单位约定，stock_price.market_cap 与 enterprise_value 仍要求 USD；缺少同日汇率时为空。人民币市值用扩展字段 market_cap_local，绝不能用 USD 市值直接除 CNY 股价。

财务以 row.unit 为准，AKShare 映射金额为元，EPS 为元/股。一致预期金额约定为百万 currency，EPS/DPS 为币种/股；导入时必须转换。

中国季报常为年初累计。is_cumulative=1 的半年和九月利润/现金流应减同年上期累计才能求单季；资产负债表为期末存量，不能相减当流量。归母净利、合并净利、扣非净利不能混用。营业利润不等于 EBIT，金融企业不能机械套工业 DCF。

事件 date、报告 end_date、公告 published_at 与抓取 as_of_date 是不同时间。回测只使用当时已公告的数据；未提供公告时间的资料不可用于无前视回测。

## 当前能力边界

20 类实体是可导入的数据模型，不代表均有自动数据源。自动源仅覆盖公司名录、日线及明确映射的部分三表科目；北交所财报请导入。一致预期、研报、KUs、事件、产品等需用户提供合法资料。

screen_drivers/screen_earnings 是确定性词项匹配；否定语境、同义词与因果关系需人工复核。search_public_library 只检索已导入资料，synthesize 仅拼接匹配摘要，不调用大模型。所有结果都要报告 coverage。
