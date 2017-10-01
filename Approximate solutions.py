# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 09:29:01 2017

@author: Oliver James
"""
cube = 8 # number to be cubed
epsilon = 0.01 # In mathematics, a small positive infinitesimal quantity, usually denoted or , whose limit is usually taken as .
guess = 0.0 # variable will hold the number of guesses
increment = .001 # the increment operator, smaller number is used to get a more accurate answer
num_guesses = 0.0 # holds the number_of guess it will take to arrive at the answer

while abs (guess **3 - cube) >= epsilon: # espilon will be used as the standard (think modulus == 0 to find even)
    guess += increment
    num_guesses +=1
print("num_guesses =", num_guesses)

if abs (guess**3 - cube) >= epsilon:
    print ("Fail")
else:
    print (guess, " is close to the square root of ", cube) #Once (guess **3 - cube) <= epsilon you are extremely close, thus basically a cubic root
    
    
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
