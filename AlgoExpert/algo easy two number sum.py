# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:08:24 2022

@author: raphael luigi tan
"""

def twoNumberSum(array, targetSum):
    if len(array) < 2:
        return []
    
    j = 0
    while j != len(array) - 1:
        difference = targetSum - array[j]
        if difference in array and (array[j] != difference):
            return [difference, array[j]]
        else: 
            j+=1
            
    return []

        
assert twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert twoNumberSum([14], 15) == []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(twoNumberSum([14], 15))

def find_num(array, num):
    i = 0
    while len(array) - 1 != i:
        if array[i] == num:
            break
        else:
            i+=1
    if array[i] == num:
        return f'[{num}]'
    
    return 'Number not in list'


        
#print(find_num([1, 5], 1))
                