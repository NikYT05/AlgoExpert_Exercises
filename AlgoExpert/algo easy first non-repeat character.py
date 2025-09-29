# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:08:34 2023

@author: raphael luigi tan
"""

def firstNonRepeatingCharacter1(string):
    i=0
    lst=[]
    for k in range(0, len(string)-1):
        lst.append(string[k])
    second=lst
    while True :
        k=lst[i]
        second.pop(i)
        if i==len(string)-1:
            return print(-1)
        elif k in lst:
            i+=1
            second=lst
        else:
            return print(i)

#assert firstNonRepeatingCharacter('aabtt')==
#firstNonRepeatingCharacter('aabtt')

def firstNonRepeatingCharacter(string):
    i = 0
    empty = []
    if string == '':
        return -1
    for k in range(0, len(string)):
        empty.append(string[k])
    while i<=len(string):
        queue = empty[0]
        empty.pop(0)
        if queue in empty:
            i+=1
            empty.append(queue)
        else:
            return i
    return -1

assert firstNonRepeatingCharacter('aabtt')==2
assert firstNonRepeatingCharacter('abcdcaf')==1
assert firstNonRepeatingCharacter('')==-1

