Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def raisePow(num, exp):
	#This is the base case
	if exp == 1:
		return 1
	else:
		num = num ** exp
	return num

>>> raisePow(2,3)
8
>>> raisePow(1,4)
1
>>> raisePow(4,3)
64
>>> 
