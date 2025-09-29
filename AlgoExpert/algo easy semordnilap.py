# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:07:52 2023

@author: raphael luigi tan
"""

def semordnilap(words):
    pairs = []
    if len(words) <= 1:
        return []
    
    first = words.pop()
    count = 0
    while count != len(words):
        subpairs = []
        i = 0
        j = -1
        while i != len(words[count]) - 1:
            if words[count[i]] == first[j]:
                i+=1
                j-=1
            else:
                break
        
            