# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:11:08 2024

@author: ALBERTJUNIOR
"""

def EvenNums(num):
    print(num)
    if num == 2:
        return num
    else:
        EvenNums(num-2)
        
EvenNums(8)