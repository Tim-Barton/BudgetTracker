'''
Created on 12 Aug 2017

@author: Tim Barton
'''

import csv

def csvParser(dataFile):
    return csv.reader(dataFile)

parsers = {"CSV":csvParser}