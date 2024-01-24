# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:35:49 2023

@author: fabio
"""

n = int(input())

values = []

for i in range(n):
    value = int(input())
    values.append(value)
    
distinct_numbers = set(values)

cnt_distinct = len(distinct_numbers)

print(f'number of distinct values: {cnt_distinct}')