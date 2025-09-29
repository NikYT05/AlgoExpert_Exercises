# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:29:31 2023

@author: raphael luigi tan
"""
'''
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    r = sorted(redShirtSpeeds)
    b = sorted(blueShirtSpeeds)
    
    
    def minimumspeeds(a, b):
        i = 0
        k = -1
        n = 0
        while i<len(b):
            if a[i]<b[k]:
                n+=a[i]
                i+=1
                k-=1
            else:
                n+=b[k]
                i+=1
                k-=1
        return print(n)
    
    def maxspeeds(x, y):
        i = 0
        k=-1
        summed = 0
        while i<len(y):
            if x[i]>y[k]:
                summed+=x[i]
                i+=1
                k-=1
            else:
                summed+=y[k]
                i+=1
                k-=1
        return print(summed)
    
    if fastest == True:
        maxspeeds(r, b)
    else:
        minimumspeeds(r, b)
'''

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    r = sorted(redShirtSpeeds)
    b = sorted(blueShirtSpeeds)
    summed = 0
    
    def maxspeeds(r, b, summed):
        front = 0
        back = -1
        while front < len(r):
            summed += max(r[front], b[back])
            front += 1
            back -= 1
        return summed
    
    '''my mistake here was that I took the minimum of the two numbers instead of getting the max.
    It might be confusing at first, but it's really how you understand the problem.
    We note that this is a tandem bike so we have to pair them up with sorted array to sorted array instead of sorted-reverse.
    Hence, why we did not get the answers for min speed.'''
    def minspeeds(r, b, summed):
        front = 0
        while front < len(r):
            summed+= max(r[front], b[front])
            front+=1
        return summed

    if fastest == True:
        return maxspeeds(r, b, summed)
    else:
        return minspeeds(r, b, summed)
        
tandemBicycle([5,5,3,9,2],[3,6,7,2,1], False)
tandemBicycle([5,5,3,9,2],[3,6,7,2,1], True)
#assert tandemBicycle([5,5,3,9,2],[3,6,7,2,1], True) == 32
#assert tandemBicycle([5,5,3,9,2],[3,6,7,2,1], False) == 11
