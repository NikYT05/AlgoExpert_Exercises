# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:41:19 2023

@author: raphael luigi tan
"""
def decreasing(array):
    count = 0
    while count < len(array) - 1:
        if array[count] >= array[count+1]:
            count += 1
        else:
            return False
    
    return True

def increasing(array):
    count = 0
    while count < len(array)-1:
        if array[count] <= array[count+1]:
            count+=1
        else:
            return False
        
    return True

def isMonotonic(array):
    if array == None or len(array) == 1:
        return True
    
    if array[0] > array[len(array)-1]:
        count = 0
        while count < len(array) - 1:
            if array[count] >= array[count+1]:
                count += 1
            else:
                return False
        
        return True
    else:
        count = 0
        while count < len(array)-1:
            if array[count] <= array[count+1]:
                count+=1
            else:
                return False
            
        return True

isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])