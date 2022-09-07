#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    rev = reverseStr(inputStr)
    app = containsWord(inputStr, "apple")
    ban = containsWord(inputStr, "banana")
    pal = isPalindrome(inputStr)
    upp = upperCaseStr(inputStr)

    print("Input string is " + inputStr)
    print("Reverse of string is " + rev)
    print("Does string contain apple? " + app)
    print("Does string contain banana? " + ban)
    print("Is string a palindrome? " + pal)
    print("Uppercase of string is " + upp)
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    w = Worker(inputStr)
    wrev = w.wreverseStr()
    wapp = w.wcontainsWord("apple")
    wban = w.wcontainsWord("banana")
    wpal = w.wisPalindrome()
    wupp = w.wupperCaseStr()    
    print("Input string is " + inputStr)
    print("Reverse of string is " + wrev)
    print("Does string contain apple? " + wapp)
    print("Does string contain banana? " + wban)
    print("Is string a palindrome? " + wpal)
    print("Uppercase of string is " + wupp)

    #Print the result of each call
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




