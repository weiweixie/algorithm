# -*- coding: utf-8 -*-
'''
Created on 2019/1/9 7:29
file : 用两个栈实现队列.py

@author: xieweiwei
'''

class Solution:
     def __init__(self):
         self.stack1 = []
         self.stack2 = []

     def push(self,node):
         self.stack1.append(node)

     def pop(self):

         print("the stack2 is: ",self.stack2)
         if len(self.stack2) == 0 and len(self.stack1) == 0:
             return None

         if len(self.stack2) == 0:
             while len(self.stack1) > 0:
                 self.stack2.append(self.stack1.pop())

         return self.stack2.pop()

if __name__ == "__main__":
    P = Solution()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())