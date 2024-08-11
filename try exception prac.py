# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:46:07 2024

@author: ALBERTJUNIOR
"""

def sqr(x):
    try:
        result = x ** x
    except(TypeError):
        print("No string input is allowed")
    finally:
        if isinstance(x, int):
            return result
        else:
            return None

print(sqr(2))
print(sqr(3))
print(sqr("a"))
