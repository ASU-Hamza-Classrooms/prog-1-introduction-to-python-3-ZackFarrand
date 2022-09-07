#!/bin/python3
#additional resource: https://www.w3schools.com/python/python_classes.asp

from stringlib import *

#Add a Worker class to this file.
class Worker:

#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
    def __init__(self, string):
        self.string = string
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

    def wreverseStr(self):
        return self.string[::-1]
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
    def wcontainsWord(self, contained):
        lowStr = self.string.lower()
        if lowStr.count(contained) > 0:
            return "Yes"
        else:
            return "No"
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise
    def wisPalindrome(self):
        lowStr = self.string.lower()
        revStr = reverseStr(lowStr)
        if lowStr == revStr:
            return "Yes"
        else: 
            return "No" 
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
    def wupperCaseStr(self):
        return self.string.upper()


