# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:21:54 2021

@author: 陳淳
"""

scort = []
while True:  #一直進入迴圈模式ˋ
    inscort = int(input("分數"))
    if (inscort==""):
        break # 直到碰到break才會跳出迴圈
    else:
        scort.append(inscort)
        scort2 = sorted(scort,reverse=True)
#        scort.sort()
#        scort.reverse()  #由大到小排列
    print(scort2)
        

