'''
Created on 10 Aug 2017

@author: Tim Barton
'''
import json

def ParseConfig( config):
    configJson = json.loads(config)
    
    categoryMap = {}
    configCategoryList = configJson["Categories"]
    for category in configCategoryList:
        for regex in category["Regexes"]:
            categoryMap[regex] = category["Category"]
            
    
    dataConfigs = {}
    dataConfigJson = configJson["Configuration"]
    for key, value in dataConfigJson.items():
        dataConfigs[key] = DataFileConfig(value) 
    return categoryMap, dataConfigs


def WriteConfig(categoryMap, dataConfigs):
    config = {}
    configCategoryMap = {}
    for regex, category in categoryMap.items():
        if category not in configCategoryMap.keys():
            newDict = {}
            newDict["Category"] = category
            newDict["Regexes"]= []
            configCategoryMap[category] = newDict
        categoryHandler = configCategoryMap[category]
        regexList = categoryHandler["Regexes"]
        regexList.append(regex)
    config["Categories"] = list(configCategoryMap.values())

    dataConfigJson = {}
    for key, value in dataConfigs.items():
        dataConfigJson[key] = value.dump()
        
    config["Configuration"] = dataConfigJson
    
    print(config)
    return json.dumps(config, indent=2)
    
    
        
        


class DataFileConfig():
    '''
    classdocs
    '''

    def __init__(self, params):
        self.amountIndex = params["AmountIndex"]
        self.descIndex = params["DescriptionIndex"]
        self.spendingNegative = params["SpendingIsNegative"]
        
    def dump(self):
        outDict = {}
        outDict["AmountIndex"] = self.amountIndex
        outDict["DescriptionIndex"] = self.descIndex
        outDict["SpendingIsNegative"] = self.spendingNegative
        return outDict
        