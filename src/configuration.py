import os

DEFAULT_CONFIG = "~/.budget/config"

#Return Statuses
SUCCESS = 1
NO_CONFIG = 1



def GetConfiguration():
    if not os.path(DEFAULT_CONFIG).exist():
        return NO_CONFIG
    return SUCCESS
