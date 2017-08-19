'''
Created on 12 Aug 2017

@author: Tim Barton
'''

import src.dataParsers as dataParsers
import re

def matchRegexes(regexes, desc):
    return list(filter(lambda x: re.match(x, desc) is not None, regexes))

def ParseSpending(dataFile, categoryMap, configs, dataType):
    parser = dataParsers.parsers[dataType](dataFile)
    config = configs[dataType]
    spendingMap = {}
    for element in parser:
        desc = element[config.descIndex]
        matchedKeys = matchRegexes(categoryMap.keys(), desc)
        if len(matchedKeys) == 0:
            matchedKeys.append("Unknown")
        if len(matchedKeys) == 1:
            category = categoryMap[matchedKeys[0]]
            if category not in spendingMap.keys():
                spendingMap[category] = 0
            currentSpend= spendingMap[category]
            spendingMap[category] = currentSpend + float(element[config.amountIndex])
        elif len(matchedKeys) > 1:
            print("Too many matching keys - cannot put into bucket: " + matchedKeys)

    for key,value in spendingMap.items():
        print(key + " " + str(value))
