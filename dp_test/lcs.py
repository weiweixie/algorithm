# -*- coding: utf-8 -*-
'''
最长公共子序列LCS


c[i,j] = 0 i=0 or j=0
         c[i-1,j-1] + 1 i,j > 0 and x_i = y_j
         max(c[i,j-1] ,c[i-1,j]) i,j > 0 and x_i != y_j
Created on 2019/1/28 23:24
file : lcs.py

@author: xieweiwei
'''


def LCS(a, b):
    if a == '' or b == '':
        return ''
    elif a[-1] == b[-1]:
        return LCS(a[:-1], b[:-1]) + a[-1]
    else:
        sol_a = LCS(a[:-1], b)
        sol_b = LCS(a, b[:-1])
        if len(sol_a) > len(sol_b):
            return sol_a
        return sol_b


def lcs_dp(input_x,input_y):
    dp =[([0]*(len(input_y) + 1)) for i in range(len(input_x) +1 )]

    for i in range(1,len(input_x) + 1):
        for j in range(1,len(input_y)+1):
            if i == 0 or j==0:
                dp[i][j] = 1
            elif input_x[i-1] == input_y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for dp_line in dp:
        print(dp_line)
    return dp[-1][-1]

if __name__ == "__main__":
    a = 'abc'
    print(a[::-1])
    print(lcs_dp(a,a[::-1]))
