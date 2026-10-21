import unittest
import os
import json
from advisor import analyze_geek_combo

class TestMcGeekAdvisor(unittest.TestCase):
    def test_nutrition_combo(self):
        res = analyze_geek_combo(["双层吉士汉堡", "麦乐鸡5块"])
        self.assertIn("total_calories_kcal", res)
        self.assertIn("total_protein_g", res)
        self.assertGreater(res["total_protein_g"], 0)
        self.assertEqual(res["items"], ["双层吉士汉堡", "麦乐鸡5块"])

if __name__ == "__main__":
    unittest.main()
