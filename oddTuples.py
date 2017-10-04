# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:31:19 2017

@author: Oliver James
"""

def oddTuples(aTup):
    x = aTup[::2]
    print(x)
    
    return x #goes through entire tuple, returning every 2nd item
oddTuples((2, 7, 9, 13, 18, 2))
        
        