# -*- coding: utf-8 -*-
"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first 
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred 
divisors?
"""
import math as m
import pandas as pd
primes = pd.read_excel('Primes.xlsx')

def isPrime(x):
    for i in range(2,int(x**0.5)):
        if x%i==0:
            return(False)
    return(True)

def primeFactorize(x, primeCount):
    divd = False
    for prime in primes['prime']:
        #print(x,prime)
        if x%prime == 0:
            divd = True
            primeCount+=1
            primeCount = primeFactorize(x/prime, primeCount)
            return(primeCount)
    return(primeCount)

def nCr(n,r):
    f = m.factorial
    ncr = int(f(n) / f(r) / f(n-r))
    return(ncr)

def factorize(x):
    n = primeFactorize(x,0)
    sig = 0    
    for r in range(1,n):
        sig += nCr(n,r)
    sig = int(sig)
    return(sig)
            

def main():
    nFac = 2
    n = 7
    triNum = 28
    while nFac<500:
        n+=1
        triNum += n
        nFac = factorize(triNum)
    print(triNum, nFac)
    return(triNum)

#main()


    