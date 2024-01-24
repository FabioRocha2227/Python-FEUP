# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:58:20 2023

@author: fabio
"""

weighted_sum = 0
total_weight = 0

n = int(input(f"n:"))

cnt = 0

while cnt < n:
    value = float(input(f"X{cnt}:"))
    weight = float(input(f"P{cnt}:"))
    
    weighted_sum += value * weight
    total_weight += weight
    
    cnt+=1
 
    
weighted_avg = weighted_sum / total_weight
print(f"Weighted average = {weighted_avg:.2f}")

