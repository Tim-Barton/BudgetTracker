import unittest
import json
import src.categories as categories
import src.spending as spending

categorySetupData = """[{"Category": "Test",
"Regexes": [
"SIMPLE FOOD PLACE",
"STRING WITH REGEX SPECIAL CHAR * PLUS EXTRA TEXT"]}]"""


class TestSpending(unittest.TestCase):

    def setUp(self):
        categorySetupDataJson = json.loads(categorySetupData)
        self.testManager = categories.CategoryManager(categorySetupDataJson)

    def testMatchRegexes(self):
        regexes = self.testManager.getRegexesAsList()
        matches = spending.matchRegexes(regexes, "SIMPLE FOOD PLACE")
        self.assertEqual(1, len(matches), "Simple Regex match Case Failed")
        matches = spending.matchRegexes(
            regexes, "STRING WITH REGEX SPECIAL CHAR * PLUS EXTRA TEXT")
        self.assertEqual(1, len(matches), "Complex Regex match case failed")

    def testCollateSpending(self):
        self.assertTrue(True)
