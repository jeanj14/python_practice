# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:45:35 2024

@author: ALBERTJUNIOR
"""

testlist = ["tomato (fruit)", "squash (vegetable)", "lettuce (vegetable)", "avocado (fruit)"]
teststr = "name (type)"

output = ""
spacepos = teststr.index(" ")
leftbr = teststr.index("(")
rightbr = teststr.index(")")

x = 0
y = 0


while x in range(0, len(testlist)):
    while y in range(0, len(testlist[y])):
        if y in range(0, spacepos):
            output = testlist[y]
            print(output)
            y += 1
        else:
            y +=1
    x+=1

print(output)

def printout(prompt):
    if prompt == "name":
        while x in range(0, len(teststr)):
            if x in range(0, spacepos):
                output = output + teststr[x]
                x += 1
            else:
                x += 1
    elif prompt == "type":
            leftbr = teststr.index("(")
            rightbr = teststr.index(")")
            x=0
            while x in range(0, len(teststr)):
                if x in range(leftbr + 1, rightbr):
                    output = output + teststr[x]
                    x += 1
                else:
                    x += 1


