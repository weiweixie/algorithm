# -*- coding: utf-8 -*-
'''
Created on 2019/2/23 21:32
file : deque_basic.py

@author: xieweiwei
'''

class DequeBasic:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)
