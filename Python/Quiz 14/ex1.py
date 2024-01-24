# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:50:02 2023

@author: fabio


filename= input("Filename:")
id= input("Name id:")
with open(filename, 'r') as file:
    for line in file:
        fields = line.strip().split(';')
        if fields[0] == id:
            print(line.strip())

"""
def find_person_by_id(filename, person_id):
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(';')
            if fields[0] == person_id:
                print(f"Filename:{filename}")
                print(f"Name id:{person_id}")
                print(line.strip())
                return
        
filename ='ginasio.csv'
person_id_to_find ='1974598'  
find_person_by_id(filename, person_id_to_find)




    





