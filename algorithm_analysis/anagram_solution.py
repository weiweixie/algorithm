# -*- coding: utf-8 -*-
'''
Created on 2019/1/28 22:06
file : anagram_solution.py

@author: xieweiwei
'''

def anagramSolution2(s1,s2):

    # new list initialized from iterable's items
    alist1 = list(s1)
    alist2 = list(s2)

    #
    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','adcbe'))