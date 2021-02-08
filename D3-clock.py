# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:48:41 2021

@author: 陳淳
"""

import time as T

play = T.clock()
for i in range(0,1000):
    for j in range(0,1000):
        n = i * j
stop = T.clock()
print(str(stop-play))
    
    
