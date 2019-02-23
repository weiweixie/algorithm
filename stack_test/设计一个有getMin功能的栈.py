# -*- coding: utf-8 -*-
'''
Created on 2019/2/23 8:56
file : 设计一个有getMin功能的栈.py

@author: xieweiwei
'''

class Solution:
    def __int__(self):
        self.stackData = []
        self.stackMin = []

    def push(self,newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum < self.getMin():
            self.stackMin.append(newNum)

    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("stack data is empty")
        value = self.stackData.pop()
        if self.getMin() == value:
            self.stackMin.pop()
        return value

    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("stack is empty")
        return self.stackMin[-1]