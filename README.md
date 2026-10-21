# 麦门极客营养与省钱参谋 (McGeek Advisor)

> 🍔 **麦当劳程序员创意开发大赛参赛作品**  
> 🏆 **参赛声明**：本项目包含完整的 [`CONTEST_DECLARATION.md`](./CONTEST_DECLARATION.md)  
> 🛠️ **MCP 集成**：详见 [`MCP_INTEGRATION.md`](./MCP_INTEGRATION.md)  
> 🤖 **WorkBuddy 支持**：详见 [`workbuddy.md`](./workbuddy.md)

---

## 🎯 项目介绍与痛点

在 1024 程序员节与高强度 Coding 周末，开发者们普遍面临三个真实用餐困境：
1. **预算受限**：希望花最少的钱吃到最饱、最实在的餐品。
2. **下午易犯困**：高升糖比（精制碳水炸弹）容易导致餐后嗜睡、血糖陡升，严重破坏沉浸式编程状态。
3. **健康与营养失衡**：久坐熬夜亟需补充优质蛋白质，但在复杂菜单中难以快速对比出最具营养性价比的搭配。

**麦门极客营养与省钱参谋 (McGeek Advisor)** 是一个基于麦当劳官方 MCP 服务构建的智能辅助 Skill：
- **实时营养分析**：调用官方 `list-nutrition-foods` 接口，穿透餐品热量、蛋白质与碳水成分。
- **极客量化模型**：首创「克蛋白单价（元/g 蛋白质）」与「代码工时热量代谢换算」，让点餐决策像代码重构一样精确。
- **自动领券核价**：调用 `available-coupons` 与 `calculate-price`，自动搭配最优 1+1 随心配或单品，不花一分冤枉钱。

---

## 🚀 快速上手与运行

本项目采用 Python 零外部第三方依赖设计，开箱即用。

### 1. 运行离线演示
```bash
git clone https://github.com/gxinxing/mcd-geek-nutrition-skill.git
cd mcd-geek-nutrition-skill
python3 advisor.py --demo
```

### 2. 连通麦当劳官方 MCP
在 [麦当劳 MCP 开放平台 (open.mcd.cn/mcp)](https://open.mcd.cn/mcp) 申请你的 MCP Token 后执行：
```bash
export MCD_MCP_TOKEN="YOUR_MCP_TOKEN"
python3 advisor.py --probe
```

### 3. 在 WorkBuddy / Cursor / Trae 中使用
在客户端的 MCP 配置文件中填入（参考 `mcp-config.example.json`）：
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_TOKEN"
      }
    }
  }
}
```
配置完成后即可在对话框中唤醒参谋：“帮我搭配一份 25 元以内的高蛋白麦当劳午餐，要求下午不犯困”。

---

## 👥 目标用户
- 互联网从业者、程序员、高强度脑力思考者。
- 健身控卡、注重蛋白质摄入的麦门爱好者。
- 热衷追求「1+1 随心配」极致省钱的理性消费者。

---

## 📄 参赛文件核对清单

- [x] `README.md`：项目说明、安装运行指南与目标用户
- [x] `CONTEST_DECLARATION.md`：官方参赛声明（未做任何修改）
- [x] `MCP_INTEGRATION.md`：使用的麦当劳 MCP Tools、调用链路及业务价值
- [x] `workbuddy.md`：WorkBuddy 开发上下文与协作记录
- [x] 源代码：核心解析引擎 `advisor.py` 与配置示例
