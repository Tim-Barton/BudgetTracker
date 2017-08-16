'''
Created on 9 Aug 2017

@author: Tim Barton
'''
import argparse
import config
import spending

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Track spending agaisnt a defined budget")
    parser.add_argument('-c', dest="configFile")
    parser.add_argument('-d', dest="dataFile")
    
    args = parser.parse_args()
    
    configFile = open(args.configFile)
    categoryMap, configs = config.ParseConfig(configFile)
    
    dataFile = open(args.dataFile)
    spending.ParseSpending(dataFile, categoryMap, configs, "CSV")