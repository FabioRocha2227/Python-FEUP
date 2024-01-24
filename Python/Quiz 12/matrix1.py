# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:47:10 2023

@author: fabio
"""

matrix = []

n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        elem = float(input())
        row.append(elem)
    matrix.append(row)
    
min_value = float('inf')
max_value = float('-inf')

for i in range(n):
    for j in range(n):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_position = (i,j)
        if matrix[i][j] > max_value:
             max_value = matrix[i][j]
             max_position = (i,j)   
             
matrix[min_position[0]][min_position[1]], matrix[max_position[0]][max_position[1]] = matrix[max_position[0]][max_position[1]], matrix[min_position[0]][min_position[1]]


for i in range(n):
   row_str = '[' + ', '.join(str(x) for x in matrix[i]) + ']' 
   print(row_str)