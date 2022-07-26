# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 07:32:50 2021

@author: josep
"""

import matplotlib.pyplot as plt
import numpy as np
import imageio
import time


class ball:
    
    def __init__(self):
        self.posn = [0,0] #m
        self.velo = [1,-1] #m/s
        self.dt = 1/50    #s
        self.r = 1        #m
        self.medpc = 0
        self.circle = True
        self.square = False
    
    def reflect_square(self):
        while abs(self.posn[0])>=self.r:
            self.velo[0] *= -(1-self.medpc)
            
            if self.posn[0]<-self.r:
                self.posn[0]= -self.r-(self.r+self.posn[0])
            
            elif self.posn[0]>self.r:
                self.posn[0]= self.r-(self.posn[0]-self.r)
                
        while abs(self.posn[1])>=self.r:
            self.velo[1] *= -(1-self.medpc)
            
            if self.posn[1]<-self.r:
                self.posn[1]= -self.r-(self.r+self.posn[1])
           
            elif self.posn[1]>self.r:
                self.posn[1]= self.r-(self.posn[1]-self.r)
        
    def reflect_circle(self):
        v = (self.velo[0]**2+self.velo[1]**2)**(0.5)
        angle_collision = np.arctan(self.posn[0]/self.posn[1])
        angle_tangent = np.arctan(self.velo[0]/self.velo[1])
        angle_new = 2 * angle_collision - angle_tangent
        
        self.posn[0] = self.r * np.sin(angle_collision)
        self.posn[1] = self.r * np.cos(angle_collision)
        
        self.velo[0] = v * np.sin(angle_new)
        self.velo[1] = v * np.cos(angle_new)
        
        if angle_collision>0:
            pass
        
        print(v,self.velo[0],self.velo[1],angle_collision)     
                 
    def calc_move(self):
        self.velo[0] += -9.8 * self.dt
        self.posn[0] += self.velo[0] * self.dt
        self.posn[1] += self.velo[1] * self.dt
        
        
        #distance = (abs(self.posn[0])>=1) or (abs(self.posn[1])>=1)
        if self.square:
            if (abs(self.posn[0])>=self.r) or (abs(self.posn[1])>=self.r):
                self.reflect_square()
        elif self.circle:
            if ((self.posn[0]**2+self.posn[1]**2)**(0.5) >= self.r):
                self.reflect_circle()
        
        
        
a = ball()
frames = 200


historyx = [a.posn[1]]
historyy = [a.posn[0]]
images = []
generation = 0
f1 = plt.figure()

while generation < frames:
    a.calc_move()
    historyy.append(a.posn[0])
    historyx.append(a.posn[1])
    generation += 1
    #plt.scatter(historyx,historyy,c='b',alpha=0.2)
    plt.scatter(a.posn[1],a.posn[0],c='r')
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.savefig(f"./images/{generation}.jpg",dpi=50)
    images.append(imageio.imread(f"./images/{generation}.jpg")) 
    plt.clf()
    #if (generation * 100)/frames == 0:
    print(generation)
imageio.mimsave(f'bounce_{time.time()*1e6}.gif', images, fps=50)
