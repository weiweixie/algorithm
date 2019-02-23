# -*- coding: utf-8 -*-
'''
Created on 2019/2/23 22:05
file : 生成窗口最大值数组.py

使用双端队列，遍历一遍数组，假设遍历到的位置是 i，
如果队列为空或者队尾所对应的元素大于arr[i]，将位置 i 压入队列；
否则将队尾元素弹出，再将 i 压入队列。
此时，判断队头元素是否等于i - w，
如果是的话说明此时队头已经不在当前窗口的范围内，删去。
这样，这个队列就成了一个维护窗口为w的子数组的最大值更新的结构，
队头元素就是每个窗口的最大值


@author: xieweiwei
'''

class Solution:

    def __init__(self):
        #使用双端队列，遍历一遍数组，假设遍历到的位置是 i，
        self.deque = []
        self.res = []

    def getMaxWindow(self,arr,w):
        if arr is None or w < 1 or\
                len(arr) < w:
            return

        for i in range(len(arr)):
            # 如果队列为空或者队尾所对应的元素大于arr[i]，将位置 i 压入队列；
            # 否则将队尾元素弹出，再将 i 压入队列。

            while self.deque and arr[self.deque[-1]] < arr[i]:
                self.deque.pop()
            self.deque.append(i)
            """
            此时，判断队头元素是否等于i - w，
            如果是的话说明此时队头已经不在当前窗口的范围内，删去。
            """
            if self.deque[0] <= i - w:
                self.deque.pop(0)
            # 这样，这个队列就成了一个维护窗口为w的子数组的最大值更新的结构，
            # 队头元素就是每个窗口的最大值
            if i -self. w + 1 >= 0:
                self.res.append(arr[self.deque[0]])
        return self.res

