# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:36:10 2022

@author: Alec
"""

import sys
from finder import finder

helpText = """
first argument supplied will be the directory of list.txt and puzzle.txt
without supplying it will default to working directory

"""


if __name__ == "__main__":          #checks if the script is first called from interpretor or another script
    print(f"Arguments count: {len(sys.argv)}")
    for idx, arg in enumerate(sys.argv):
        print(f"Argument {idx:>6}: {arg}")
    for arg in sys.argv:
        if '-h' in arg:
            print(helpText)
            sys.exit(0)
    if(len(sys.argv)>=2):
        thing = finder(sys.argv[1])
    else: 
        thing = finder('.')
    thing.showAnswers()