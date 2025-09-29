# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:12:15 2023

@author: raphael luigi tan
"""

def classPhotos(redShirtHeights, blueShirtHeights):
    r = sorted(redShirtHeights)
    b = sorted(blueShirtHeights)
    i = 1
    if r[0]>b[0]:
        while i<len(b):
            if r[i]<b[i]:
                return False
            else:
                i+=1
        return True
    elif r[0]<b[0]:
        while i<len(b)-1:
            if r[i]>b[i]:
                return False
            else:
                i+=1
        return True
    else: 
        return False


assert classPhotos([5,8,1,3,4], [6, 9, 2, 4, 5]) == True