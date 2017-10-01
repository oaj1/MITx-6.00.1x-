# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:18:03 2017

@author: Oliver James
"""
low = 0
high =100

print ("think of a number between 1 and 100")
while True:
    guess = int((high + low)/2.0)
    print ("is the number " + str(guess) + " the number you thought of ?" )
    answer = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    elif answer == "c":
        print ("great " + str(guess) + " is the number you thought of! ")
        break
    else:
        print ("sorry I dont recognize that input")
        