# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:41:52 2023

@author: raphael luigi tan
"""

def oneEdit(stringOne, stringTwo):
    l1 = len(stringOne)
    l2 = len(stringTwo)
    if l1 == l2:
        i = 0
        j = 0
        while i < l1:
            if stringOne[i] == stringTwo[i]:
                i += 1
            else:
                i += 1
                j += 1
        
        if j <= 1:
            return True
        else:
            return False
        
    if l1+1 == l2 or l1-1==l2 or l1 == l2+1 or l1 == l2-1:
        if l1 > l2:
            if l1[0]!=
                    
    
assert oneEdit("AAAB", "AAAA") == True