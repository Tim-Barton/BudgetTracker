import unittest
import json
from src import categories

simpleRegexString = "abc"
complexRegexString = "ab*bc*cd*"


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.testCat = categories.Category("Test")

    def test_addRegex_simple(self):
        preTestRegex = self.testCat.getRegexes()
        self.testCat.addRegex(simpleRegexString)
        postTestRegex = self.testCat.getRegexes()
        self.assertNotEqual(len(preTestRegex), len(postTestRegex))
        self.assertTrue(simpleRegexString in postTestRegex)

    def test_addRegex_complex(self):
        preTestRegex = self.testCat.getRegexes()
        self.testCat.addRegex(complexRegexString)
        postTestRegex = self.testCat.getRegexes()
        self.assertNotEqual(len(preTestRegex), len(postTestRegex))
        self.assertTrue(complexRegexString in postTestRegex)


categorySetupData = """[{"Category": "Test",
"Regexes": [
"SIMPLE FOOD PLACE",
"STRING WITH REGEX SPECIAL CHAR * PLUS EXTRA TEXT "]}]"""


class TestCategoryManager(unittest.TestCase):

    def setUp(self):
        categorySetupDataJson = json.loads(categorySetupData)
        self.testManager = categories.CategoryManager(categorySetupDataJson)

    def test_add_Category_new(self):
        preTestCategories = self.testManager.getCategoryNames()
        self.testManager.addCategory("New")
        postTestCategores = self.testManager.getCategoryNames()
        self.assertNotEqual(len(preTestCategories), len(postTestCategores))
        self.assertTrue("New" in postTestCategores)
