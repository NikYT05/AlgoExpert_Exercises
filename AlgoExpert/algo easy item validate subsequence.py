# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:18:08 2022

@author: raphael luigi tan
"""

def Valid(array, sequence):
    '''
    if len(array) < len(sequence):
        return 'false'
       ''' 
    i = 0
    j = 0
    while len(array) - 1 > i:
        if sequence[j] == array[i] and len(sequence) - 1 != j:
            j+=1
            i+=1
        elif len(sequence) - 1 == j:
            return 'true'
        elif sequence[j] != array[i] and len(sequence) - 1 != j:
            i+=1
        else:
            return 'false'
            
'''
def isValidSubsequence(array, sequence):
    i = 0
    num = 0
    while True:
        if len(array) < len(sequence):
            return 'false'
        elif sequence[i] in array and len(sequence) -1 == i and num < array.index(sequence[i]):
            return 'true'
        elif sequence[i] in array and (num == 0 or num < array.index(sequence[i])):
            num = 0
            num += array.index(sequence[i])
            i += 1
        elif sequence[i] not in array:
            return 'false'
        else:
            return 'false'
    return 'true'
'''

def isValidSubsequence(array, sequence):
    i = 0
    while len(array)-1>=i and sequence!=[]:
        if array[i]==sequence[0]:
            sequence.pop(0)
            i+=1
        elif array[i]!=sequence[0]:
            i+=1
    if sequence==[]:
        return True
    else:
        return False


#assert isValidSubsequence([1,2], [1, 2, 3]) == 'false'
assert isValidSubsequence([1,2,3], [1,2,3]) == 'true'
assert isValidSubsequence([1,2,3,4,5], [2,4,5]) == 'true'
assert isValidSubsequence([1,2,3,4,5], [3,1,4]) == 'false'
assert isValidSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]) == 'true'
assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22, 8]) == 'false'
assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5]) == 'false'
assert isValidSubsequence([1,1,6,1], [1,1,1,6]) == 'false'

isValidSubsequence([1,2,3],[1,2,3])



    