# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:29:39 2023

@author: raphael luigi tan
"""

def generateDocument(characters, document):
    a = sorted(characters)
    b = sorted(document)

    if len(a) >= len(b):
        while True:
            if a==[] and len(b)>0:
                return False
            elif b==[]:
                return True
            elif a[-1]==b[-1]:
                a.pop()
                b.pop()
            elif a[-1]!=b[-1]:
                a.pop()
            else:
                return False
                
    else: 
        return False


assert generateDocument('aabbccc', 'babaccc') == True
assert generateDocument('babygirl', 'nnn') == False

