# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:48:44 2021

@author: 陳淳
"""

import random
num = random.sample(range(1,50),7)
special = num.pop()
num.sort()
print(num)
#print("本期號碼:")
print("特別數字:" +str(special))

import time
time.sleep(3)
print(time.ctime())
#print(time.localtime())
