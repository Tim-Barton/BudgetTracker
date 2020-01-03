'''
Created on 10 Aug 2017

@author: Tim Barton
'''
import json
import categories


def ParseSettings(config):
    configJson = json.loads(config)

    categoriesJson = {}
    if "Categories" in configJson.keys():
        categoriesJson = configJson["Categories"]

    categoryManager = categories.CategoryManager(categoriesJson)

    dataConfigs = {}
    if "Configuration" in configJson.keys():
        dataConfigJson = configJson["Configuration"]
        for key, value in dataConfigJson.items():
            dataConfigs[key] = DataFileConfig(value)
    return categoryManager, dataConfigs


def WriteSettings(categoryManager, dataConfigs):
    config = {}

    config["Categories"] = categoryManager.dump()

    dataConfigJson = {}
    for key, value in dataConfigs.items():
        dataConfigJson[key] = value.dump()

    config["Configuration"] = dataConfigJson

    return json.dumps(config, indent=2)


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
