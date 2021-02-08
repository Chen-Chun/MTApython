# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:14:23 2021

@author: 陳淳
"""

def reverse_pname(backwards_pname):
    forward_pname=""
    for index in range(len(backwards_pname)-1,-1,-1):
        forward_pname +=backwards_pname[index]
    return forward_pname
print(reverse_pname("klim"))

