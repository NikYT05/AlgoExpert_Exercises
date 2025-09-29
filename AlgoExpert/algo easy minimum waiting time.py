# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 00:34:01 2022

@author: raphael luigi tan
"""

def minimumWaitingTime(queries):
    lowest = sorted(queries)
    i = -1
    num  = 0
    summed = 0
    while True:
        if len(lowest) == num :
            break
        else:
            summed += lowest[i] * num
            num += 1
            i -= 1
    return summed
#assert minimumWaitingTime([3, 2, 1, 2, 6]) == 22


minimumWaitingTime([3, 2, 1, 2, 6])
