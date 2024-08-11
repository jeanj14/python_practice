# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:08:54 2023

@author: ALBERTJUNIOR
"""

arrayprac = [1, 2, 3, 4, 5]

for x in range(0, len(arrayprac)):
    print(arrayprac[x])
    
class Dummy:
    def __init__(self):
        self.array = []
        
    def arraybuilder(self, x):
        self.array = x
    
    
d = Dummy()
d.arraybuilder(arrayprac)
print(d.array)