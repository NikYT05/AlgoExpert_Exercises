# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 00:04:15 2022

@author: raphael luigi tan
"""

def sortedSquaredArray(array):
    empty = []
    for i in range(0, len(array)):
        squared = array[i] ** 2
        empty.append(squared)
    return (sorted(empty))

assert sortedSquaredArray([1,2,3,5,6,8,9]) == [1,4,9,25,36,64,81]
assert sortedSquaredArray([5,2,3,1]) == [1,4,9,25]


