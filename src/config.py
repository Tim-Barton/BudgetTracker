'''
Created on 10 Aug 2017

@author: Tim Barton
'''
import json


def ParseConfig( config):
    configJson = json.loads(config)
    
    categoriesJson = {}
    if "Categories" in configJson.keys():
        categoriesJson = configJson["Categories"]
    
    categoryManager = CategoryManager(categoriesJson)
    
    dataConfigs = {}
    if "Configuration" in configJson.keys():
        dataConfigJson = configJson["Configuration"]
        for key, value in dataConfigJson.items():
            dataConfigs[key] = DataFileConfig(value) 
    return categoryManager, dataConfigs


def WriteConfig(categoryManager, dataConfigs):
    config = {}
    
    config["Categories"] = categoryManager.dump()

    dataConfigJson = {}
    for key, value in dataConfigs.items():
        dataConfigJson[key] = value.dump()
        
    config["Configuration"] = dataConfigJson
    
    return json.dumps(config, indent=2)
    
    
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
    
    def addCategory(self,name):
        if name not in self.getCategoryNames():
            self.__categoriesList.append(Category(name))
        
        
    def addRegexToCategory(self, categoryName, regex):
        list(filter(lambda x: x.name == categoryName, self.__categoriesList))[0].addRegex(regex)
        
    def getRegexes(self):
        return map(lambda x: x.regexes, self.__categoriesList)
    
    def getCategoryNames(self):
        return map(lambda x: x.name, self.__categoriesList)
        
    def getRegexesAsList(self):
        return [regex for regexes in self.getRegexes() for regex in regexes]
    
    #returns the first category that has the appropriate regex
    def getCategoryFromRegex(self, regex):
        #print(regex)
        return list(filter(lambda x: regex in x.regexes, self.__categoriesList))[0].name
    
class Category:
    def __init__(self, name):
        self.name = name
        self.regexes = set([])
        
    def addRegex(self, regex):
        self.regexes.add(regex)
        
    def getRegexes(self):
        return list(self.regexes)
    
class DataFileConfig:
    '''
    classdocs
    '''

    def __init__(self, params):
        self.amountIndex = params["AmountIndex"]
        self.descIndex = params["DescriptionIndex"]
        self.spendingNegative = params["SpendingIsNegative"]
        self.dataType = params["DataType"]
        
    def dump(self):
        outDict = {}
        outDict["AmountIndex"] = self.amountIndex
        outDict["DescriptionIndex"] = self.descIndex
        outDict["SpendingIsNegative"] = self.spendingNegative
        outDict["DataType"] = self.dataType
        return outDict
        
