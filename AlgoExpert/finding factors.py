# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:02:14 2022

@author: raphael luigi tan
"""

def factor(num):
    k = 2
    while k<=num:
        if num%k == 0:
            print(f'{k} ', end='')
            num = num/k
            k = 2
        else:
            k+=1
            

print(103180/93.8)
print(103180/220)
#factor(103180)
factor(8)



#assert factor(10) == [1,2,5]

        