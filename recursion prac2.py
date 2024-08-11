# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:45:21 2024

@author: ALBERTJUNIOR
"""

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)  