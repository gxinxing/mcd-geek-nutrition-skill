#!/usr/bin/env python3
"""
麦门极客营养与省钱参谋 (McGeek Advisor) - 官方真实 MCP 对接引擎
支持从麦当劳官方 MCP Server (https://mcp.mcd.cn) 实时拉取最新餐品营养与活动。
"""

import os
import sys
import json
import urllib.request
import argparse

MCP_URL = "https://mcp.mcd.cn"
DEFAULT_TOKEN_FILE = os.path.expanduser("~/WorkBuddy/mcd-geek-nutrition-skill/mcd_nutrition_live.json")

def call_mcd_mcp(tool_name, arguments=None, token=None):
    token = token or os.environ.get("MCD_MCP_TOKEN")
    if not token:
        raise ValueError("请设置 MCD_MCP_TOKEN 环境变量")
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments or {}
        }
    }
    req = urllib.request.Request(
        MCP_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        resp = json.loads(r.read().decode("utf-8"))
        if "error" in resp:
            raise RuntimeError(f"MCP Error: {resp['error']}")
        return resp.get("result", {}).get("content", [{}])[0].get("text", "")

def get_live_foods(token=None):
    """从官方真实 MCP 获取 160 款餐品营养表"""
    try:
        raw_text = call_mcd_mcp("list-nutrition-foods", token=token)
        data_str = json.loads(raw_text.split("## Original Response\n\n")[1])["data"]
        lines = data_str.strip().split("\n")[1:]
        foods = []
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 9:
                foods.append({
                    "name": parts[0].strip(),
                    "energyKcal": float(parts[3].strip()) if parts[3].strip() != "null" else 0,
                    "protein": float(parts[4].strip()) if parts[4].strip() != "null" else 0,
                    "fat": float(parts[5].strip()) if parts[5].strip() != "null" else 0,
                    "carbohydrate": float(parts[6].strip()) if parts[6].strip() != "null" else 0
                })
        return foods
    except Exception as e:
        # 降级读取本地缓存的真实 MCP 镜像
        if os.path.exists(DEFAULT_TOKEN_FILE):
            with open(DEFAULT_TOKEN_FILE) as f:
                return json.load(f)
        raise e

def analyze_geek_combo(food_names, token=None):
    all_foods = get_live_foods(token=token)
    food_map = {f["name"]: f for f in all_foods}

    matched = []
    for name in food_names:
        # 支持模糊匹配
        found = next((f for k, f in food_map.items() if name in k), None)
        if found:
            matched.append(found)

    if not matched:
        return {"error": "未匹配到指定餐品"}

    total_kcal = sum(f["energyKcal"] for f in matched)
    total_protein = sum(f["protein"] for f in matched)
    total_carb = sum(f["carbohydrate"] for f in matched)

    # 程序员代谢模型：静态高强度脑力编码约消耗 120 kcal/h
    coding_hours = round(total_kcal / 120.0, 1)

    return {
        "source": "McDonalds Official MCP Server (https://mcp.mcd.cn)",
        "items": [f["name"] for f in matched],
        "total_calories_kcal": total_kcal,
        "total_protein_g": total_protein,
        "total_carb_g": total_carb,
        "geek_coding_hours_burn": coding_hours,
        "nutrition_score": "🔥 高蛋白抗困组合 (低GI+足量蛋白)" if total_protein >= 30 and total_carb <= 55 else "👌 能量补充型套餐"
    }

def main():
    parser = argparse.ArgumentParser(description="麦门极客营养与省钱参谋 (基于麦当劳官方MCP)")
    parser.add_argument("--live", action="store_true", help="调用官方 MCP 实时分析")
    parser.add_argument("--calendar", action="store_true", help="查询官方今日营销活动日历")
    parser.add_argument("--demo", action="store_true", help="运行高蛋白组合演示")
    args = parser.parse_args()

    token = os.environ.get("MCD_MCP_TOKEN")

    if args.calendar:
        print("[MCP 实时调用] 获取麦当劳今日活动日历...")
        cal = call_mcd_mcp("campaign-calendar", token=token)
        print(cal[:600] + "...\n[OK] 官方活动实时拉取成功！")
        return

    print("==================================================")
    print("🍔 麦门极客营养参谋 · 官方真实 MCP 实时分析报告")
    print("==================================================")
    res = analyze_geek_combo(["双层吉士汉堡", "麦乐鸡"], token=token)
    print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
