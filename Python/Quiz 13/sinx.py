# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:38:47 2023

@author: fabio
"""
import math

def senx(x,n):
    result = 0
    
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
        
   
    
    return round(result,4)


result = senx(2, 5)

print(result)    