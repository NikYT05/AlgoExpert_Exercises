# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:16:39 2023

@author: raphael luigi tan
"""
#a majority element is an element that appears in the array over 50% of the time
#we assume that all inouts have a majority element
def majorityElement(array):
    req = 1/2
    for i in range(len(array)):
        majority = 0
        for k in range(len(array)):
            if array[k] == array[i]:
                majority += 1
            else:
                continue
        
        if majority/len(array)>req:
            return array[i]
        
assert majorityElement([2]) == 2
assert majorityElement([435, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]) == 6543