'''
Created on 27 Aug 2017

@author: Tim Barton
'''

import argparse
import src.config as config
import src.spending as spending

def saveConfig(dataConfigs, categoryManager):
    with open(args.configFile, 'w') as configFile:
        configFile.write(config.WriteConfig(categoryManager, dataConfigs))

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
    for category in categoryManager.getCategoryNames():
        print(category)
    return input("Please enter another desired Category or 'none' to complete this section:\n")

def SetupCategories(categoryManager):
    userInput = PromptForCategory(categoryManager)
    while userInput.lower() != "none":
        categoryManager.addCategory(userInput)
        userInput = PromptForCategory(categoryManager)

def ConfigureCategoryRegex(categoryManager, regex):
    print("Which Category does this regex belong to? {}".format(regex))
    categories = list(categoryManager.getCategoryNames())
    print(categories)
    for category in categories:
        print(category)
    inputCategory = input()
    while inputCategory not in categories:
        print("Oops, not a configured Category")
        inputCategory = input()
    categoryManager.addRegexToCategory(inputCategory, regex)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Createa config using a spending file as source")
    parser.add_argument('-c', dest="configFile")
    parser.add_argument('-d', dest="dataFile")

    args = parser.parse_args()
    
    with open(args.configFile, 'r') as configFile:
        configJson = configFile.read()
        if configJson == "":
            configJson = "{}"
        categoryManager, dataConfigs = config.ParseConfig(configJson)
        
        if len(list(categoryManager.getCategoryNames())) == 0:
            SetupCategories(categoryManager)        
            
        with open(args.dataFile,'r') as dataFile:
            if len(dataConfigs) == 0:
                SetUpDataConfigs(dataConfigs, dataFile) 
            elif len(dataConfigs) == 1:
                dataFileType = list(dataConfigs.keys())[0]
            else:
                dataFileType = WhichDataFileType(dataConfigs)
            #print(dataFileType)
            spendList = spending.parseSpending(dataFile, dataConfigs, dataFileType)
            #print(spendList)
            for spend in spendList:
                #print(spend.desc)
                matchedKeys = list(spending.matchRegexes(categoryManager.getRegexesAsList(), spend.desc))
                #print(matchedKeys)
                if len(matchedKeys) == 0:
                    ConfigureCategoryRegex(categoryManager, spend.desc)
                    saveConfig(dataConfigs, categoryManager)
