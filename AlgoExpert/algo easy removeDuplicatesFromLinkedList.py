# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:39:19 2023

@author: raphael luigi tan
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    ptr = linkedList
    
    while ptr.next is not None:
        nextNode = ptr.next
        if ptr.value == nextNode.value:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next
    
    return linkedList