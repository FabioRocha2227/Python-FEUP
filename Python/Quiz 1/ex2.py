# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:46:20 2023

@author: fabio
"""

n = int(input("n:"))

min_value = float('inf')
max_value = float('-inf')
sum_values = 0
cnt = 0

while cnt < n:
    value = float(input(f"value({cnt}):"))
    sum_values+=value
    cnt+=1
    
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value
        
final_sum = sum_values - max_value - min_value
final_cnt = cnt-2

average = final_sum / final_cnt
print(f"Average = {average:.2f}")