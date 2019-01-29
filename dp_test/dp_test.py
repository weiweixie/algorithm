# -*- coding: utf-8 -*-
'''
Created on 2019/1/28 22:49
file : dp_test.py

@author: xieweiwei
'''

from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


def memo1(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

@memo
def fib(i):
    if i<  2 :
        return 1
    return fib(i -1 )+ fib(i-2)




"""
二项式系数C(n,k)表示从n个中选k个，假设我们现在处理n个中的第1个，
考虑是否选择它。如果选择它的话，那么我们还需要从剩下的n-1个中选k-1个，
即C(n-1,k-1)；如果不选择它的话，我们需要从剩下的n-1中选k个，即C(n-1,k)。
所以，C(n,k)=C(n-1,k-1)+C(n-1,k)。
"""



@memo
def cnk(n,k):
    if k==0: return 1 #the order of `if` should not change!!!
    if n==0: return 0
    return cnk(n-1,k)+cnk(n-1,k-1)


print(fib(100))


from collections import defaultdict

s = "the quick brown fox jumps over the lazy dog"

words = s.split()
location = defaultdict(list)
for m, n in enumerate(words):
    location[n].append(m)

print (location)