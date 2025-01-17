# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:51:04 2024

@author: ALBERTJUNIOR
"""

class Empty(Exception):
    pass

class ArrayStack():
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
def is_matched(expr):
    lefty =  '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

if is_matched('[(5+x)-(y+z)]'):
    print("The expression is balanced")
else:
    print("The expression is unbalanced")