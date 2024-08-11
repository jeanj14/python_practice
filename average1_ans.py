# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:58:26 2024

@author: ALBERTJUNIOR
"""

x=0
numlist=[]

# function for calculating count
def calccount(inputList : list):
    count = len(inputList)
    
    return count
    
# function for calculating sum
def calcsum(inputList : list):
    sumList = 0
    i = 0

    while i < len(inputList):
        sumList+=inputList[i]
        i+=1

    return sumList

# function for finding lowest value
def findlow(inputList : list):
    low=inputList[0]
    x=0
    for x in inputList:
        if x<low:
            low=x
    return low

# function for finding the highest value
def findhigh(inputList: list):
    high=inputList[0]
    x=0
    for x in inputList:
        if x>high:
            high=x
    return high

# function for finding the mean
def findmean(inputList: list):
    sumList = 0
    for i in inputList:
        sumList+=i
        
    mean = sumList / len(inputList)
    return mean

# while loop to start the process of entering data
while x>=0:
    prompt=input('Enter a number or Press Enter to stop\n')
    if prompt == "":
        break
    else:
        numlist.append(int(prompt))
        
    
print(numlist) #using f string to output returned outputs from the functions
print(f"count = {calccount(numlist)} sum = {calcsum(numlist)} lowest = {findlow(numlist)} highest = {findhigh(numlist)} mean = {findmean(numlist)}")