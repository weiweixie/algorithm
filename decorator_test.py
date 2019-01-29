# -*- coding: utf-8 -*-
'''
Created on 2019/1/28 22:38
file : decorator_test.py

@author: xieweiwei
'''
from datetime import time


def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2019-01-28')

now()
