# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:33:06 2017

@author: Oliver James
"""
x = 25 # what im trying to square
epsilon = 0.01 #epsilon is used to see how close I am
numGuesses = 0 # how many guesses it will take me
low = 1.0 # low value in range 1 - x
high = x # high value in range 1 -x 
ans = (high + low)/2.0 # used to divide range by two for each increment to narrow range

while abs(ans**2 -x) >= epsilon:
    print ("low = " + str(low) + " high = " + str(high) + " answer = " + str(ans))
    numGuesses +=1
    
    # the code will repeat until the low and high are .01 difference (epsilon)
    
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ("numGuesses = " + str(numGuesses))
print (str(ans) + " is close to the sqaure root of " + str(x))
