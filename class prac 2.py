# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:07:13 2024

@author: ALBERTJUNIOR
"""

class Book:
    def __init__(self, name, bookid, genre, returned=False):
        self.name = name
        self.bookid = bookid
        self.genre = genre
        
class Library:
    def __init__(self):
        self.bookstack=[]
        
    def insertbook(self, book):
        self.bookstack.append(book)
    
    def get_latest_book(self):
        if self.bookstack:
            return self.bookstack[-1]
        else:
            return "No books"
        

lib = Library()
book1=Book("Harry potter", "1234", "Fantasy")
book2=Book("Percy jackson", "5678", "Fantasy")
lib.insertbook(book1)
lib.insertbook(book2)
latest =  lib.get_latest_book()
print(latest.name)