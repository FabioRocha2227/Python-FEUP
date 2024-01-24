# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:43:32 2023

@author: fabio
"""

str = input()

words = str.split()

reverse = ' '.join(reversed(words))

print(reverse)