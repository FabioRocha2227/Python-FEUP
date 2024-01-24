# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:30:09 2023

@author: fabio
"""
n = int(input('n:'))
max_diff = float('-inf')

value1 = int(input('value 1:')) 

for i in range(2,n+1):
    value = float(input(f'value {i}:'))
    diff = abs(value - value1)
    if diff > max_diff:
        max_diff = diff
    value1 = value
    
print(f"Maximum difference = {max_diff:.2f}")