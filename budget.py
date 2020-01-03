'''
Created on 9 Aug 2017

@author: Tim Barton
'''
import argparse
import src.settings_handler as settings
import src.spending as spending
# from src.config import WriteConfig

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Track spending agaisnt a defined budget")
    parser.add_argument('-c', dest="settingsFile")
    parser.add_argument('-d', dest="dataFile")

    args = parser.parse_args()

    settingsFile = open(args.settingsFile)
    categoryManager, settings = settings.ParseSettings(settingsFile.read())

    dataFile = open(args.dataFile)
    spendList = spending.parseSpending(dataFile, settings, "Spendfile")
    spending.collateSpending(spendList, categoryManager)
