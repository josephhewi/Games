# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:00:36 2020

@author: josep
"""
def isPrime(n):
    prime = True
    for j in range(2,n//2):
        if n%j == 0:
            return(False)
    return(True)

sig = 2

for i in range(3,int(2e6),2):
    if isPrime(i):
        sig+=i

print(sig)
