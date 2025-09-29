# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:01:10 2023

@author: raphael luigi tan
"""

def transposeMatrix(matrix):
    if matrix is None:
        return matrix
    
    columns = len(matrix)
    rows = len(matrix[0])
    
    final = []
    count = 0
    while count < rows:
        piece = []
        count2 = 0
        while count2 < columns:
            piece.append(matrix[count2][count])
            count2 += 1
        final.append(piece)
        count += 1
        
    return final

transposeMatrix([[1,3,5],[2,4,6]])