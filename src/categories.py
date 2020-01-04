import re


class CategoryManager:
    def __init__(self, inputCategories):
        self.__categoriesList = []
        self.addCategory("Unknown")
        self.addRegexToCategory("Unknown", "Unknown")
        if inputCategories is not None:
            for category in inputCategories:
                name = category["Category"]
                regexes = category["Regexes"]
                self.addCategory(name)
                for regex in regexes:
                    self.addRegexToCategory(name, regex)

    def dump(self):
        returnList = []
        for category in self.__categoriesList:
            thisDict = {}
            thisDict["Category"] = category.name
            thisDict["Regexes"] = category.getRegexes()
            returnList.append(thisDict)
        return returnList

    def addCategory(self, name):
        if name not in self.getCategoryNames():
            self.__categoriesList.append(Category(name))

    def addRegexToCategory(self, categoryName, regex):
        [x for x in self.__categoriesList if x.name
            == categoryName][0].addRegex(regex)

    def getRegexes(self):
        return [x.regexes for x in self.__categoriesList]

    def getCategoryNames(self):
        return [x.name for x in self.__categoriesList]

    def getRegexesAsList(self):
        return [regex for regexes in self.getRegexes() for regex in regexes]

    # returns the first category that has the appropriate regex
    def getCategoryFromRegex(self, regex):
        return [x.name for x in self.__categoriesList if regex in x.regexes][0]


class Category:
    def __init__(self, name):
        self.name = name
        self.regexes = set([])

    def addRegex(self, regex):
        self.regexes.add(regex)

    def getRegexes(self):
        return list(self.regexes)
