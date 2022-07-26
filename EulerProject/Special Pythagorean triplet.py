# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:53:58 2020

@author: josep
"""
triplets = []
for i in range(1,1000):
    for j in range(i,1000):
        test = i**2+j**2
        sqrt = test**0.5
        if int(sqrt) == sqrt:
            triplets.append([i,j,sqrt])
            
for triplet in triplets:
    sig = sum(triplet)
    if sig == 1000:
        print(triplet, triplet[0]*triplet[1]*triplet[2])