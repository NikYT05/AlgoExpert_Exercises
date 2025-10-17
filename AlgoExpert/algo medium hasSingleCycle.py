# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 14:50:07 2025

@author: raphael luigi tan
"""

def hasSingleCycle(array):
    traversed = []
    index = 0
    length = len(array)
    sentry = 0
    while sentry < length:
        index += array[index]
        while index < 0:
            #print('add')
            index += length

        while index >= length:
            #print('substract')
            index -= length
            
        #print(index)
        traversed.append(index)
        sentry += 1

    #print(traversed)
    traversed.sort()
    #print(traversed)


    for i in range(length):
        if i == traversed[i]:
            continue
        else:
            return False

    return True
        
A = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(A))