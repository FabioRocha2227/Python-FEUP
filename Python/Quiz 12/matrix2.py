# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:11:24 2023

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
    
    
flattened_matrix = sorted([element for row in matrix for element in row])
sorted_matrix = [flattened_matrix[i:i+n] for i in range(0, n**2, n)]


for i in range(n):
   row_str = '[' + ', '.join(str(x) for x in sorted_matrix[i]) + ']' 
   print(row_str)