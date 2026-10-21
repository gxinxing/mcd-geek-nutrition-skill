# WorkBuddy 协同开发与真实 MCP 联调记录 (WorkBuddy Context)

本项目「麦门极客营养与省钱参谋」全程使用腾讯 WorkBuddy 完成创意构想、麦当劳官方 MCP 连接器配置、数据结构对齐及实测联调。

## 一、 WorkBuddy MCP 连接器配置

在 WorkBuddy 的 `connectors/mcp.json` 中配置官方 Streamable HTTP 服务：
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamableHttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer ${MCD_MCP_TOKEN}"
      },
      "timeout": 60,
      "disabled": false
    }
  }
}
```

## 二、 真实开发与调试上下文

### 轮次 1：MCP 连通性与权限验证
- **输入**：调用 `tools/list` 探测麦当劳官方服务器可用工具集。
- **WorkBuddy 响应**：检测到官方已开放包括 `list-nutrition-foods`、`campaign-calendar`、`delivery-query-stores`、`calculate-price` 在内的 30+ 项生产级 Tools。

### 轮次 2：真实餐品营养数据拉取与清洗
- **输入**：调用 `list-nutrition-foods` 获取全部餐品营养成分。
- **处理过程**：官方接口以紧凑文本表格格式返回了全部 160 款餐品数据，WorkBuddy 协助编写了结构化解析逻辑，成功抽取 `energyKcal`、`protein`、`fat`、`carbohydrate` 关键指标，形成可靠的本地计算模型。

### 轮次 3：极客代谢模型构建与代码落地
- **算法设计**：根据程序员久坐静止代谢率（约 120 kcal/h），测算消耗该餐品所需的沉浸式 Coding 工时。
- **产出交付物**：生成纯标准库 Python 引擎 `advisor.py`，支持带 Token 实时连通与离线极速演示双重模式。
