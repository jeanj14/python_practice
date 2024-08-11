# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:53:37 2024

@author: ALBERTJUNIOR
"""

class HashMap:
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
            raise KeyError('Key Error: ' + repr(k))
            
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
            
            self._table.append(self.item(k,v))
            
    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
            raise KeyError('Key Error: ' + repr(k))

if __name__ == "__main__":
    pass