# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:01:06 2023

@author: raphael luigi tan
"""

def sunsetViews(buildings, direction):
    x = []
    if direction == "WEST":
        j = -1
        for i in buildings:
            if j >= i:
                continue
            else:
                j = i
                x.append(buildings.index(i))
        return x

    else:
        j = -1
        for i in range(len(buildings)-1, -1, -1):
            if j >= buildings[i]:
                continue
            else:
                j = buildings[i]
                x.append(i)
            

        return sorted(x)
                
assert sunsetViews([3,5,4,4,3,1,3,2], "EAST") == [1, 3, 6, 7]
assert sunsetViews([3,5,4,4,3,1,3,2], "WEST") == [0, 1]
assert sunsetViews([1], "EAST") == [0]