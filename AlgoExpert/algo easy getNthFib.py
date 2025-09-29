# -*- coding: utf-8 -*-
def getNthFib(n):
    if n == 1:
        return n
    elif n == 2:
        return 1
    else:
        num = 0
        queue = [0, 1]
        i=0
        while i<n-2:
            num = queue[0] + queue[1]
            queue.pop(0)
            queue.append(num)
            i+=1
        return num
    
    
getNthFib(3)
'''
assert getNthFib(0) == 0
assert getNthFib(1) == 1
assert getNthFib(2) == 1
assert getNthFib(6) == 5'''