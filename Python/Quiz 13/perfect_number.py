# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:54:03 2023

@author: fabio
"""

def perfect(number):
    
    if number <= 0:
        return False
    
    divisors_sum = sum(divisor for divisor in range(1,number) if number % divisor == 0)
    
    return divisors_sum == number


n = 6

result = perfect(n)

if result:
    print("True")
else:
    print("False")