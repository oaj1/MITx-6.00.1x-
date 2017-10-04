# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:00:21 2017

@author: Oliver James
"""
def get_data (aTuple):
    #created empty nums tuple to hold nums
    nums = ()
    #created empty words tuple to hold words
    words = ()
    
    #iterate through all the numbers, which will be index 0 for the tuples
    for t in aTuple:
        nums = nums + (t[0],) #this will add all 1st elements of tuples to nums
        
        #now I want to add words to empty words tuple
        if t[1] not in words:
            words = words + (t[1],)#this will add words to words tuple that are not in tuple already
    
    #now I want to create variables to hold max number, min number, and each unique word
    min_num = min (nums)
    max_num = max (nums)
    unique_words = len (words)
    # now i want to return the above variables for user to retrieve
    return (min_num, max_num, unique_words)

#Now I will call the small num, large num, and unique words
(small,large,words) = get_data(((1,'mine'),(3,'yours'), (5,'ours'), (7,'mine')))