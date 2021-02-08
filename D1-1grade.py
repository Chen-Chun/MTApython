# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:35:56 2021

@author: 陳淳
"""

score = int(input("分數:"))
if score<100 and score>0:
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("Not Goog")
else:
    print("error")