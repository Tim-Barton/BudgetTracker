import unittest
from src import settings_handler as settings

simpleRegexString = "abc"
complexRegexString = "ab*bc*cd*"
complexRegexStringEsc = "ab\*bc\*cd\*"


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.testCat = settings.Category("Test")

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
        self.assertTrue(complexRegexStringEsc in postTestRegex)
