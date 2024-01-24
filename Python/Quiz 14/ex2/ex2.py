# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:19:38 2023

@author: fabio
"""

def print_unique_names(file1, file2):
    unique_names = set()  # Use a set to store unique names

    # Read and process File 1
    with open(file1, 'r') as f1:
        for line in f1:
            name = line.strip()
            unique_names.add(name)

    # Read and process File 2
    with open(file2, 'r') as f2:
        for line in f2:
            name = line.strip()
            unique_names.add(name)

    # Print unique names in alphabetical order
    sorted_names = sorted(unique_names)
    for name in sorted_names:
        print(name)

# Example usage:
file1 = 'f1.txt'  # Replace with the actual filename for Fiche1
file2 = 'f2.txt'  # Replace with the actual filename for Fiche2
print_unique_names(file1, file2)