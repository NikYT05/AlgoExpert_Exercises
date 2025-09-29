# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:08:18 2023

@author: raphael luigi tan
"""

def productSum(array):
    SENTRY = 1
    
    def helper(array1, sentry):
        num =0
        while array1 != []:
            if type(array1[0]) == list:
                sentry += 1
                num += sentry*(helper(array1[0], sentry))
                array1.pop(0)
                sentry -= 1
            
            else: 
                num += array1.pop(0)

        return num
    
    return helper(array, SENTRY)
    

    
productSum([5, 2, [7, [3], -1], 3])
productSum([[[3]]]) == 18
productSum([
    [1, 2],
    3,
    [4, 5]
  ]
)
    
    