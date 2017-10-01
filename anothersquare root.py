# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:15:04 2017

@author: Oliver
"""
x = 16
low = 1.0
high = x
epsilon = 0.01
answer= (high + low)/2.0
numGuesses = 0
 
while abs(answer **2 - x) > epsilon:
    numGuesses +=1
   
    if answer **2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2.0
print ("square root of 16 is " + str(answer))
print ("it took this many guesses " + str(numGuesses))
