# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:21:26 2022

@author: raphael luigi tan
"""
#Given an array and without sorting it, return an array of the three largest integers in the array


def findThreeLargestNumbers(array):
    big_list = []
    i=0
    while len(big_list)!=3 or i<len(array):
        if big_list == 0 and len(array)==3:
            big_list.append(array[0])
            big_list.append(array[1])
            big_list.append(array[2])
            print(big_list)
            break
        else:
            return 1


findThreeLargestNumbers([1,2,3])