# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:24:59 2017

@author: Oliver
"""
#this function will return a quadratic equation result
def evalQuadratic(a, b, c, x):
    # function will return the value of the quadratic formula, a * x**2 + b * x + c
    
    result = (a*(x**2)) + (b*x) +c #this is the formula
    print(result) #print the result
    return result
    
evalQuadratic(3,5,6,2)#The numbers that are passes into the parameters