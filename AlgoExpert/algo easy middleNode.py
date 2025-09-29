# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:06:00 2023

@author: raphael luigi tan
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    head = linkedList
    if not head or not head.next:
        return linkedList
    
    i = 0
    count = linkedList
    while count.next:
        i += 1
        count = count.next
    
    if i%2 == 0:
        fast = linkedList
        slow = linkedList
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    else:
        fast = linkedList
        slow = linkedList
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
