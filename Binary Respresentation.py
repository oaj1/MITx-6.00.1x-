# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:13:30 2017

@author: Oliver
"""
num = 3


if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''  
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num//2
if isNeg:
    result = "-" + result
