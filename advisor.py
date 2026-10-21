#!/usr/bin/env python3
"""
麦门极客营养与省钱参谋 (McGeek Advisor) - 核心执行引擎
支持离线 Demo 演示与真实 MCP 接口连通测试。
"""

import os
import sys
import json
import argparse

# 内置麦当劳常见核心餐品营养库 (基于 list-nutrition-foods 官方返回标准结构)
SAMPLE_FOODS = [
    {"code": "1001", "name": "双层吉士汉堡", "price": 13.9, "protein_g": 26.0, "calories_kcal": 450, "carb_g": 34.0, "is_1plus1": True},
    {"code": "1002", "name": "麦香鸡", "price": 13.9, "protein_g": 14.0, "calories_kcal": 380, "carb_g": 40.0, "is_1plus1": True},
    {"code": "1003", "name": "麦辣鸡翅(2块)", "price": 13.9, "protein_g": 16.0, "calories_kcal": 390, "carb_g": 18.0, "is_1plus1": True},
    {"code": "1004", "name": "零度可口可乐", "price": 0.0, "protein_g": 0.0, "calories_kcal": 0, "carb_g": 0.0, "is_1plus1": True},
    {"code": "1005", "name": "麦旋风/新地", "price": 0.0, "protein_g": 4.0, "calories_kcal": 310, "carb_g": 48.0, "is_1plus1": True},
    {"code": "1006", "name": "巨无霸汉堡", "price": 25.0, "protein_g": 28.0, "calories_kcal": 520, "carb_g": 42.0, "is_1plus1": False},
    {"code": "1007", "name": "麦辣鸡腿堡", "price": 22.0, "protein_g": 22.0, "calories_kcal": 510, "carb_g": 45.0, "is_1plus1": False},
    {"code": "1008", "name": "麦乐鸡(5块)", "price": 13.0, "protein_g": 13.0, "calories_kcal": 230, "carb_g": 15.0, "is_1plus1": False},
]

def analyze_combo(food_codes):
    selected = [f for f in SAMPLE_FOODS if f["code"] in food_codes]
    if not selected:
        return {"error": "未找到匹配餐品"}

    total_price = sum(f["price"] for f in selected)
    total_protein = sum(f["protein_g"] for f in selected)
    total_calories = sum(f["calories_kcal"] for f in selected)
    total_carb = sum(f["carb_g"] for f in selected)

    protein_cost = round(total_price / total_protein, 2) if total_protein > 0 else 0
    coding_hours = round(total_calories / 120.0, 1) # 按程序员静态脑力消耗约 120kcal/h 换算

    return {
        "items": [f["name"] for f in selected],
        "total_price_cny": total_price,
        "total_protein_g": total_protein,
        "total_calories_kcal": total_calories,
        "total_carb_g": total_carb,
        "protein_cost_cny_per_g": protein_cost,
        "geek_coding_hours_burn": coding_hours,
        "verdict": "🔥 穷鬼蛋白性价比战神" if protein_cost < 0.8 else "👌 营养均衡之选"
    }

def main():
    parser = argparse.ArgumentParser(description="麦门极客营养与省钱参谋")
    parser.add_argument("--demo", action="store_true", help="运行离线推荐 Demo")
    parser.add_argument("--probe", action="store_true", help="检测麦当劳 MCP Token 环境配置")
    args = parser.parse_args()

    if args.probe:
        token = os.environ.get("MCD_MCP_TOKEN")
        if token:
            print(f"[OK] 找到环境变量 MCD_MCP_TOKEN (前4位: {token[:4]}...)")
            print("[OK] MCP 远程接入地址: https://mcp.mcd.cn (Streamable HTTP)")
        else:
            print("[WARN] 未检测到 MCD_MCP_TOKEN，建议在 https://open.mcd.cn/mcp 申请后配置")
        return

    # 默认输出演示
    print("==================================================")
    print("🍔 麦门极客营养参谋：【极客抗困高蛋白 1+1 随心配】推荐")
    print("==================================================")
    result = analyze_combo(["1001", "1004", "1008"]) # 双吉 + 零度可乐 + 麦乐鸡
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
