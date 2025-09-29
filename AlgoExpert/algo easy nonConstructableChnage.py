# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:38:39 2022

@author: raphael luigi tan
"""

def nonConstructibleChange(coins):
    coins = coins.sort()
    if coins == []:
        return 1
    else:
        i = 0
        while len(coins) > i:
             print(coins.index(i))
             i+=1
         
nonConstructibleChange([1,2,3,4])

print(len([10,2]))