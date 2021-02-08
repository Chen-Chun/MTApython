# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:45:55 2021

@author: 陳淳
"""

#n階
n = int(input("n:"))

total=1
for n in range(1,n+1):
    total *= n

print(total)