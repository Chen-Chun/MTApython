# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:38:41 2021

@author: 陳淳
"""
f = open('file1.txt','r')
for line in f:
    print(line)
f.close()

with open('file1.txt','r') as f:
    for line in f:
        print(line)
        
f = open('file1.txt','r')
s = f.readline()
r = f.readlines()
print(s)
print(r)
f.close()