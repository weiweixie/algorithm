# -*- coding: utf-8 -*-
'''
Created on 2019/2/23 9:14
file : 两个栈实现队列.py

@author: xieweiwei
'''

class Solution:

    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def add(self,newNum):
        self.stackPop.append(newNum)

    def poll(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is ecpty")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPop.pop())
        return self.stackPop.pop()

    def peek(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is ecpty")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPop.pop())
        return self.stackPop[-1]