# 麦当劳 MCP 服务集成说明 (MCP Integration)

## 一、 集成概述
本项目「麦门极客营养与省钱参谋 (McGeek Advisor)」深度集成麦当劳中国官方远程 MCP Server (`https://mcp.mcd.cn`)。
项目已通过官方真实 MCP Token 完成全流程联调测试，支持实时拉取官方全量 160 款餐品营养热量成分，以及官方实时营销活动日历。

## 二、 实际使用的麦当劳 MCP Tools 清单

| MCP Tool 名称 | 官方中文名称 | 实际联调测试情况与业务价值 |
|---|---|---|
| `list-nutrition-foods` | 餐品营养信息列表 | **实测通过**：成功实时拉取全量 160 款餐品的准确能量(kcal)、蛋白质(g)、脂肪(g)、碳水(g)数据，用于计算「克蛋白单价」与极客抗困配比。 |
| `campaign-calendar` | 活动日历查询工具 | **实测通过**：成功调用并实时获取到当日官方热门营销活动（如 GD 联名活动、积分抢先购等），动态呈现最新优惠。 |
| `available-coupons` | 麦麦省券列表查询 | 用于外送/点餐前匹配用户名下可减免的立减券与品类券。 |
| `calculate-price` | 商品价格计算 | 对选定的低碳高蛋白极客套餐进行官方引擎计价，确保实付价格精准。 |

## 三、 真实 MCP 调用示例与返回验证

### 1. 营养数据实时获取 (`list-nutrition-foods`)
通过 Streamable HTTP 协议请求 `https://mcp.mcd.cn`：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list-nutrition-foods",
    "arguments": {}
  }
}
```
**实测官方接口返回**（节选）：
```text
[160]{productName,nutritionDescription,energyKj,energyKcal,protein,fat,carbohydrate,sodium,calcium}:
  双层吉士汉堡,null,1882,450,26,24,34,892,201
  麦乐鸡5块,null,962,230,13,13,15,480,12
  ...
```

### 2. 极客分析与换算输出
调用本地计算引擎 `advisor.py` 整合后的实时分析结果：
```json
{
  "source": "McDonalds Official MCP Server (https://mcp.mcd.cn)",
  "items": [
    "双层吉士汉堡",
    "麦乐鸡5块"
  ],
  "total_calories_kcal": 680.0,
  "total_protein_g": 39.0,
  "total_carb_g": 49.0,
  "geek_coding_hours_burn": 5.7,
  "nutrition_score": "🔥 高蛋白抗困组合 (低GI+足量蛋白)"
}
```

## 四、 业务与用户价值
1. **真实数据背书**：所有卡路里、蛋白质数据均来自麦当劳官方实验室测定值，无任何 AI 捏造。
2. **极客健康赋能**：帮助开发者告别“下午饭后脑雾昏睡”，在预算可控范围内最大化蛋白质补充效率。
