# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:20:56 2023

@author: fabio
"""

n = int(input("n:"))

factorial = 1
curr_num = 1

while curr_num <=n:
    factorial *= curr_num
    curr_num += 1
    
print(f"Factorial = {factorial}")