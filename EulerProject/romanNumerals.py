# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 07:10:13 2021

@author: josep
"""

inputfile = "C:/Users/josep/Downloads/p089_roman.txt"


def rom2dec(rom):
    numerals = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,
                "C" : 100,"D" : 500,"M" : 1000}
    
    lastvalue = 1001
    curvalue = 0
    total = 0
    for n in rom:
        curvalue = numerals[n]
        print(curvalue)
        if curvalue > lastvalue:
            print("subtract")
        elif curvalue == lastvalue:
            print("group")
        elif curvalue < lastvalue:
            print("add")
        lastvalue = curvalue
        
        
        
        
rom2dec("IV")