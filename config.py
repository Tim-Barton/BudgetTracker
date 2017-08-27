'''
Created on 27 Aug 2017

@author: Tim Barton
'''

import argparse
import src.config as config
import src.spending as spending

def SetUpDataConfigs(dataConfigs, dataFile):
    pass
    #repLine = dataFile.read_line()
    #print("This is a line from your data file")
    #print(repLine)
    #print("Please tell us what type of data it is from the following")
    

def WhichDataFileType(dataConfigs):
    pass

def PromptForCategory(categoryManager):
    print("Your currently configured Categories are:")
    for category in categoryManager.getCategoryNames:
        print(category)
    return input("Please enter another desired Category or 'none' to complete this section")

def SetupCategories(categoryManager):
    userInput = PromptForCategory(categoryManager)
    while userInput.toLowerCase() is not "none":
        categoryManager.addCategory(userInput)
        userInput = PromptForCategory(categoryManager)

def ConfigureCategoryRegex(categoryManager, regex):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Createa config using a spending file as source")
    parser.add_argument('-c', dest="configFile")
    parser.add_argument('-d', dest="dataFile")

    args = parser.parse_args()
    
    with open(args.configFile) as configFile:
        configJson = configFile.read()
        if configJson.empty:
            configJson = "{}"
        categoryManager, dataConfigs = config.ParseConfig(configJson)
        
        if len(list(categoryManager.getCategoryNames())) == 0:
            SetupCategories(categoryManager)        
            
        with open(args.datFile) as dataFile:
            if len(dataConfigs) == 0:
                SetUpDataConfigs(dataConfigs, dataFile) 
            if len(dataConfigs) == 1:
                dataFileType = dataConfigs.keys()[0]
            else:
                dataFileType = WhichDataFileType(dataConfigs)
            spendList = spending.parseSpending(dataFile, dataConfigs, dataFileType)
            for spend in spendList:
                matchedKeys = list(spending.matchRegexes(categoryManager.getRegexesAsList(), spend.desc))
                if len(matchedKeys) == 0:
                    pass
                    ConfigureCategoryRegex(categoryManager, spend.desc)
        
        configFile.write(config.WriteConfig(categoryManager, dataConfigs))