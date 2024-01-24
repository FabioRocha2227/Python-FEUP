# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:17:52 2023

@author: fabio
"""
text  = input()

shift = int(input())
enc_msg = ""


for i in text:
    text_shift = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
    enc_msg += text_shift
    
print(enc_msg)
