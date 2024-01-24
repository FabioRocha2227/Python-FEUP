# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:56:43 2023

@author: fabio
"""

n = int(input('n:'))
sum = 0
for i in range(1,n+1):
    value = float(input(f'value {i}:'))
    sum +=value
    
mean = sum / n

print(f'Arithmetic mean = {mean:.2f}')