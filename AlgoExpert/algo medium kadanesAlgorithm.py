# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:34:28 2023

@author: raphael luigi tan
"""
#Kadane's algorithm finds the max possible sum of an subarray derived from an array
#ex. [3,4,5,-9] the max sum is 12
def kadanesAlgorithm(array):
    from math import maxsize
    max_ending_here = -maxsize
    max_num = -maxsize
    for i in array:
        #we compare the previous sum and the current num in the array to see if it is worth adding into the sum
        max_ending_here = max(max_ending_here + i, i)
        
        max_num = max(max_num, max_ending_here)
    
    return max_num

def kadanes(array):
    max_ending_here = array[0]
    max_num = array[0]
    
    numbers = [max_ending_here]
    for i in array[1:]:
        max_ending_here = max(max_ending_here + i, i)
        max_num = max(max_num, max_ending_here)
        
        numbers.append(max_ending_here)
        
    
    
kadanes([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])