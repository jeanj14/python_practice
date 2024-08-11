# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:30:48 2024

@author: ALBERTJUNIOR
"""

from queue import Queue

class Food:
    def __init__(self , name, price, available=False):
        self.name = name
        self.price = price

class Cafeteria:
    def __init__(self):
        self.foodqueue = Queue()
        
    def insert_cafe(self, food):
        self.foodqueue.put(food)
        
    def get_cafe(self):
        if self.foodqueue.empty() == False:
            return self.foodqueue.get()
        else:
            return "No food :("
        
        
cafe = Cafeteria()
food1=Food("pizza", "120",)
food2=Food("pasta", "90")
food3=Food("fish and chips", "75", available=True)

cafe.insert_cafe(food3)
cafe_food = cafe.get_cafe()
print(f"{cafe_food.name} is ready")