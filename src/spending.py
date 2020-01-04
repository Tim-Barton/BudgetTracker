'''
Created on 12 Aug 2017

@author: Tim Barton
'''

import src.dataParsers as dataParsers
import re
from decimal import Decimal


def matchRegexes(regexes, desc):
    #return filter(lambda x: re.search(x, desc) is not None, regexes)
    return [re.escape(x) for x in regexes if re.search(re.escape(x), desc) is not None]


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


def collateSpending(spending, categoryMap):
    spendingMap = {}
    for spend in spending:
        matchedKeys = matchRegexes(
            categoryMap.getRegexesAsList(), spend.desc)
        if len(matchedKeys) == 0:
            matchedKeys.append("Unknown")
            print("Unknown regex: {}".format(spend.desc))
        if len(matchedKeys) == 1:
            category = categoryMap.getCategoryFromRegex(matchedKeys[0])
            if category not in spendingMap.keys():
                spendingMap[category] = 0
            currentSpend = spendingMap[category]
            spendingMap[category] = currentSpend + Decimal(spend.amount)
        elif len(matchedKeys) > 1:
            print(
                "Too many matching keys - cannot put into bucket: {}".format(matchedKeys))

    for key, value in spendingMap.items():
        print(key + " " + str(value))


class SpendElement:

    def __init__(self, desc, amount):
        self.desc = desc
        self.amount = amount
