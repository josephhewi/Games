# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:45:12 2020

@author: josep
"""

def IsPrime(x):
    """
    Return True if the number is prime, else return False
    
    >>> IsPrime(13)
    True
    
    >> IsPrime(12)
    False
    
    """
    
    assert ((type(x) == int) or type(x) == float), "isPrime() requires a numeric input"
    if x == 2:
        return(True)
    for i in range(2,x):
        if x%i==0:
            return(False)
    return(True)

def Decompose(x):
    """
    Return all factors of a given interger, but does not specify frequency of occurance
    
    >>> Decompose(6)
    [1,2,3,6]
    
    >>> Decompose(100)
    [1,2,]
    
    """
    
    assert ((type(x) == int) or type(x) == float), "Decompose() requires a numeric input"
    factors = set([])
    if x==1:
        return([1])
    elif x==0:
        return([0])
    for i in range(1,x//2+1):
        if (x%i==0):
            factors.add(i)
            factors.add(int(x/i))
    factors = sorted(factors)
    return(factors)

def PrimeDecompose(x):
    """
    Returns all prime factors of a given interger, but does not specify frequency or occurance
    
    >>> PrimeDecompose(100)
    [2,5]
    
    >>> PrimeDecompose(127)
    [127]

    """
    
    unfilteredFactors = Decompose(x)
    primeFactors = []
    for factor in unfilteredFactors:
        if IsPrime(factor):
            primeFactors.append(factor)
    return(primeFactors)

def PrimeFactorize(x):
    '''
    Return a dictionary of all prime factors and their frequency of occurance for a given number
    
    >>> PrimeFactorize(100)
    [[2,2],[5,2]]
    
    >>> PrimeFactorize(945)
    [[3,3],[5,1],[7,1]]
    

    '''
    primeFactors = PrimeDecompose(x)
    if 1 in primeFactors:
        primeFactors.remove(1)
    results = []
    for prime in primeFactors:
        n=0
        testValue = x
        
        while (testValue%prime==0):
            n+=1
            testValue /= prime
        results.append([prime,n])
    if results == []:
        results = [0,0]
    return(results)

def LCD(X):
    '''
    Return the lowest common denominator of an array of numbers.
    Finds all prime factors of each value in the array, raises the prime to
    the max occurance rate, and finds the product.
    
    e.g. LCD of 25, 9, 15:
        25 = [5,2], 9 = [3,2], 15 = [[3,1],[5,1]]
        LCD = (5**2)*(3**2) = 225
        
    >>> LCD([7,30,50])
    
    '''
    lcdFactors = {}
    for x in X:
        pF = PrimeFactorize(x)
        for primeSet in pF:
            try :
                if lcdFactors[primeSet[0]]<primeSet[1]:
                    lcdFactors[primeSet[0]] = primeSet[1]
            except:
                lcdFactors[primeSet[0]] = primeSet[1]
                
    product = 1
    for i in lcdFactors:
        product*=i**lcdFactors[i]
        
    return(product)

    
