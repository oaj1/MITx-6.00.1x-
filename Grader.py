# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:40:09 2017

@author: Oliver James
"""
from math import tan,pi

def polysum(n,s):
    
    
    area = 0.25 * n * (s ** 2) / (tan(pi / n)) #formula for area
    perimeter = s * n
    
    #This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
    
    result1 =  (area +  (perimeter ** 2))
    resultFinal = round(result1,4)
    
   print(resultFinal)
    
    return resultFinal

    
    
    
    
    
    
   
