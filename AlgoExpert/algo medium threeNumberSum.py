# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:28:53 2023

@author: raphael luigi tan
"""

def threeNumberSum(array, targetSum):
    final = []
    for i in range(len(array)):
        triplets = []
        for k in range(i+1,len(array)):
            difference = targetSum - (array[i] + array[k])
            if difference in array[k:] and array[i]!=array[k]!=difference:
                triplets.append(array[i])
                triplets.append(array[k])
                triplets.append(difference)
                final.append(sorted(triplets))
                break
            else:
                continue
            
    res = []
    [res.append(x) for x in final if x not in res]


    return print(sorted(res))

threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
#threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32)
threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0)
            
        