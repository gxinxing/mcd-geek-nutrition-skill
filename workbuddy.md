# WorkBuddy 协同开发记录 (WorkBuddy Context)

本项目「麦门极客营养与省钱参谋」全程使用 WorkBuddy 完成需求构想、架构拆解、代码实现与 MCP 连接调试。

## 开发会话摘要

### 阶段 1：创意构想与赛道对齐
- **开发者提问**：参与 1024 程序员节黑客松与麦当劳创新大赛，如何利用麦当劳 MCP 打造一款兼具趣味性、实用性且契合程序员群体的项目？
- **WorkBuddy 建议**：
  1. 结合程序员 1024 开发者特征，痛点在于：预算有限、时间紧凑、害怕高碳水导致下午 Coding 犯困、以及对高蛋白质性价比的量化偏好。
  2. 深度调用官方 MCP `list-nutrition-foods` 工具的真实营养数据与 `available-coupons` 工具，搭建一套「克蛋白单价」计算器与「抗困控卡」组合推荐。

### 阶段 2：MCP 连接器集成与协议对接
- 在 WorkBuddy 中配置麦当劳官方 MCP Server：
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer ${MCD_MCP_TOKEN}"
      }
    }
  }
}
```
- 调试 `list-nutrition-foods` 返回格式，建立餐品热量、蛋白质和官方单价的对拍基准。

### 阶段 3：算法逻辑与交互工程落地
- 编写零依赖轻量 Python 核心调度引擎 `advisor.py`，支持离线 Mock 演示与真实 MCP 接口切换。
- 构建兼顾移动端与大屏的单页交互应用 `index.html`，展示直观的营养性价比评分与代码工时代谢换算。

### 阶段 4：合规与竞赛交付物自检
- WorkBuddy 辅助核对大赛规范，保证包含 `CONTEST_DECLARATION.md`、`MCP_INTEGRATION.md`、`README.md` 及对话上下文说明，确保项目格式 100% 满足大赛自动审核机制。
