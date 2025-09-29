# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:46:19 2023

@author: raphael luigi tan
"""

def inOrderTraverse(tree, array):
    while tree.left or tree.right is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    
    return array


def preOrderTraverse(tree, array):
    while tree.left or tree.right is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    
    return array


def postOrderTraverse(tree, array):
    while tree.left or tree.right is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    
    return array