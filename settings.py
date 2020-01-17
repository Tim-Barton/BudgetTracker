'''
Created on 27 Aug 2017

@author: Tim Barton
'''

import argparse
import src.settings_handler as settings
import src.spending as spending
import src.ui.cli as ui


def saveSettings(datasettings, categoryManager):
    with open(args.settingsFile, 'w') as settingsFile:
        settingsFile.write(settings.WriteSettings(
            categoryManager, datasettings))


def SetUpDatasettings(datasettings, dataFile):
    pass
    #repLine = dataFile.read_line()
    #print("This is a line from your data file")
    #print(repLine)
    #print("Please tell us what type of data it is from the following")


def WhichDataFileType(datasettings):
    pass


def SetupCategories(categoryManager):
    userInput = ui.PromptForNewCategory(categoryManager)
    while userInput.lower() != "":
        categoryManager.addCategory(userInput)
        userInput = ui.PromptForNewCategory(categoryManager)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Createa config using a spending file as source")
    parser.add_argument('-c', dest="settingsFile")
    parser.add_argument('-d', dest="dataFile")

    args = parser.parse_args()

    with open(args.settingsFile, 'r') as settingsFile:
        settingsJson = settingsFile.read()
        if settingsJson == "":
            settingsJson = "{}"
        categoryManager, datasettings = settings.ParseSettings(settingsJson)

        SetupCategories(categoryManager)

        with open(args.dataFile, 'r') as dataFile:
            if len(datasettings) == 0:
                SetUpDatasettings(datasettings, dataFile)
            elif len(datasettings) == 1:
                dataFileType = list(datasettings.keys())[0]
            else:
                dataFileType = WhichDataFileType(datasettings)
            spendList = spending.parseSpending(
                dataFile, datasettings, dataFileType)
            for spend in spendList:
                matchedKeys = spending.matchRegexes(
                    categoryManager.getRegexesAsList(), spend.desc)
                if len(matchedKeys) == 0:
                    ui.PromptCategoryRegexRelation(categoryManager, spend.desc)
                    saveSettings(datasettings, categoryManager)
