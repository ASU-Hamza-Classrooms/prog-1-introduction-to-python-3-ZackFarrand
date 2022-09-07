#!/bin/python3
#online resource: https://www.w3schools.com/python/python_strings.asp
#                 https://www.w3schools.com/python/python_conditions.asp
#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(txt):
    return txt[::-1]
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(txt, contained):
    lowTxt = txt.lower()
    if lowTxt.count(contained) > 0:
        return "Yes"
    else:
        return "No"
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise
def isPalindrome(txt):
      lowTxt = txt.lower()
      revTxt = reverseStr(lowTxt)
      if lowTxt == revTxt:
          return "Yes"
      else: 
          return "No" 
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(txt):
    return txt.upper()

#

