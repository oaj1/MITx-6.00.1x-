# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 08:54:28 2017

@author: Oliver James
"""

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
iteration = 0
while iteration < 5:
    count = 0 # THIS count needs to be declared outside of while iteration
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
    
iteration = 0 # variable iteration will hold the variable for how many rotations I will go through
while iteration < 5: #0 - 4 rotations
    count = 0 # counter variable, since inside the while, the highest it will go is to the max length of the string, it will not be iterated (12,24, ect)
    for letter in "hello, world": # iterate through each letter in the literal string "hello world"
        count += 1 #counter increased by one in each lettter (for a val of 12), stops at 12, due to count being declared within the while loop
        if iteration % 2 == 0: # if iteration is even number, break (some reason returns a count of 1, not to sure as to why)
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))#print it out
    iteration += 1 # iteration number increases by a counter of 1 through each loop