# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:44:24 2021

@author: 陳淳
"""

import random
ans = random.randint(1,10)
while True:
    guess = int(input("guess number?"))
    if ans==guess:
        print("right")
        break
    else:
        print("worng")