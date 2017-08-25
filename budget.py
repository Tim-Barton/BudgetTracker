'''
Created on 9 Aug 2017

@author: Tim Barton
'''
import argparse
import src.config as config
import src.spending as spending
from src.config import WriteConfig

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Track spending agaisnt a defined budget")
    parser.add_argument('-c', dest="configFile")
    parser.add_argument('-d', dest="dataFile")

    args = parser.parse_args()

    configFile = open(args.configFile)
    categoryManager, configs = config.ParseConfig(configFile.read())

    dataFile = open(args.dataFile)
    spendList = spending.parseSpending(dataFile, configs, "Spendfile")
    spending.collateSpending(spendList, categoryManager)

    with open('test.txt', 'w') as outFile:
        outFile.write(WriteConfig(categoryManager,configs))
        
        
        