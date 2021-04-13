'''
Created on 12 Aug 2017

@author: Tim Barton
'''

import src.dataParsers as dataParsers
import re
from decimal import Decimal
import src.ui.cli as ui


def matchRegexes(regexes, desc):
    return [x for x in regexes if re.search(re.escape(x), desc) is not None]


def parseSpending(dataFile, settingsList, dataFileType):
    settings = settingsList[dataFileType]
    parser = dataParsers.parsers[settings.dataType](dataFile)

    spendList = []
    for element in parser:
        desc = element[settings.descIndex]
        amount = Decimal(element[settings.amountIndex])
        if settings.spendingNegative and amount < 0:
            amount = amount * -1
            spendList.append(SpendElement(desc, amount))
        elif (not settings.spendingNegative) and amount > 0:
            spendList.append(SpendElement(desc,  amount))
    return spendList


def collateSpending(spending, categoryManager):
    spendingMap = {}
    for spend in spending:
        matchedKeys = matchRegexes(
            categoryManager.getRegexesAsList(), spend.desc)
        if len(matchedKeys) == 0:
            ui.PromptCategoryRegexRelation(categoryManager, spend.desc)
        if len(matchedKeys) == 1:
            category = categoryManager.getCategoryFromRegex(matchedKeys[0])
            if category not in spendingMap.keys():
                spendingMap[category] = 0
            currentSpend = spendingMap[category]
            spendingMap[category] = currentSpend + Decimal(spend.amount)
        elif len(matchedKeys) > 1:
            ui.PrintError(
                "Too many matching keys - cannot put into bucket: {}".format(matchedKeys))

    ui.PrintFinalOutput(spendingMap)


class SpendElement:

    def __init__(self, desc, amount):
        self.desc = desc
        self.amount = amount
