# -*- coding: utf-8 -*-
'''
Created on 2019/1/9 7:13
file : search.py

@author: xieweiwei
'''

def sequential_search(lis,key):
    """
      最基础的无序列表的查找算法
    :param lis:
    :param key:
    :return:
    """
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(LIST, 123)
    print (result)
