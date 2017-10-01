Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def factorial(num):
	if num <= 0: # if num equal's 0 return 1
		return 1
	else:
		return num * factorial (num -1)#example 4 *3, 12*2, ==24

	
>>> factorial (4)
24
>>> 
