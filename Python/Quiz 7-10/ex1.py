# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:02:01 2023

@author: fabio
"""

n = int(input())

values = []

for i in range(n):
    value = int(input())
    values.append(value)
    
values.sort()

print('The sorted list is:')
for i in range(n):
    print(values[i])
    