'''
Created on 10 Aug 2017

@author: Tim Barton
'''
import json

def ParseConfig( configFile):
    configJson = json.load(configFile)
    
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


class DataFileConfig():
    '''
    classdocs
    '''

    def __init__(self, params):
        self.amountIndex = params["AmountIndex"]
        self.descIndex = params["DescriptionIndex"]
        self.spendingNegative = params["SpendingIsNegative"]
        