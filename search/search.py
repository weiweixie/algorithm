# -*- coding: utf-8 -*-
'''
Created on 2019/1/9 7:13
file : search.py

@author: xieweiwei
'''


def sequentialSearch(alist, item):
    """
      最基础的无序列表的查找算法
    :param lis:
    :param key:
    :return:
    """
    pos = 0
    found = False

    length = len(alist)
    for i in range(length):
        if alist[i] == item:
            return i
    return False


    def binarySearch(alist, item):
        first = 0
        last = len(alist) -1
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint +1
                else:
                    first = midpoint +1
        return found

    def binaraySearchRecur(alist, item):
        if len(alist) == 0:
            return False

        midpoint = len(alist)// 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binaraySearchRecur(alist[:midpoint],item)
            else:
                return binaraySearchRecur(alist[midpoint+1:],item)



if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
