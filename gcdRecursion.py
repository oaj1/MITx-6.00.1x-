# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:07:36 2017

@author: Oliver
"""

def gcd(a,b):
    """
    Return the greatest common divisor of a and b
    example (7,14) gcd is 7

    """
    #if a is 0, then the greatest common divisor is b
    if (a == 0):
        return b
    elif (b == 0):
        # if b is zero, then the greatest common divisor is a
        return a
    else:
        #result will diplay value b, and the divisor of a and b
        result = gcd(b,a%b)
        print (result)
        return result
gcd(3,9)


       
