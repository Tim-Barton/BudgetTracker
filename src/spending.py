'''
Created on 12 Aug 2017

@author: Tim Barton
'''

import src.dataParsers as dataParsers
import re

def matchRegexes(regexes, desc):
    return filter(lambda x: re.match(x, desc) is not None, regexes)

def parseSpending(dataFile, configs, dataType):
    parser = dataParsers.parsers[dataType](dataFile)
    config = configs[dataType]
    spendList = []
    for element in parser:
        desc = element[config.descIndex]
        amount = float(element[config.amountIndex])
        if config.spendingNegative:
            amount = amount * -1
        spendList.append(SpendElement(desc, amount))
    return spendList
        
        
def collateSpending(spending, categoryMap ):
    spendingMap = {}
    for spend in spending:
        matchedKeys = list(matchRegexes(categoryMap.keys(), spend.desc))
        if len(matchedKeys) == 0:
            matchedKeys.append("Unknown")
        if len(matchedKeys) == 1:
            category = categoryMap[matchedKeys[0]]
            if category not in spendingMap.keys():
                spendingMap[category] = 0
            currentSpend= spendingMap[category]
            spendingMap[category] = currentSpend + float(spend.amount)
        elif len(matchedKeys) > 1:
            print("Too many matching keys - cannot put into bucket: " + matchedKeys)

    for key,value in spendingMap.items():
        print(key + " " + str(value))



class SpendElement:
    
    def __init__(self, desc, amount):
        self.desc = desc
        self.amount = amount
