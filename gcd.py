# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:45:10 2017

@author: Oliver
"""
def gcd(a,b):
    greatestCommonDivisor = 1 # this will be starting value for greatest common divisor

    minValue = min(a,b) #min function returns the smallest of the two values (being a)

 # the elements leading up to value a, the 1 to -1, means from first index to last index, or 1 to a
    for i in range (minValue, 1, -1):
        # if the modulus of the two values is == 0, then it is divisible
         if (a % i == 0) and (b % i == 0):
             print(i)
             #Thus return that index of i
             return i
         else:
             greatestCommonDivisor = 1
    return greatestCommonDivisor
    
gcd(8,12)

