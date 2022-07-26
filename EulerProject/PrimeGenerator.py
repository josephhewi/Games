# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:48:44 2020

@author: josep
"""
def isPrime(x):
    for i in range(2,int(x**0.5)):
        if x%i==0:
            return(False)
    return(True)

import pandas as pd


primes = [2]
for i in range(3,1000000,2):
    if isPrime(i):
        primes.append(i)
        
p = pd.DataFrame(primes,columns=['prime'])
p.to_excel('Primes.xlsx')
