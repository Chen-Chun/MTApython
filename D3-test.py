# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:49:22 2021

@author: 陳淳


s = 'AB CD'
A = list(s)
A.append("EF")
print(A)

print(True or False)

t =([7,8],10,False)
tpye(t[0])

list1 = [1,2,3,4,5,6]
print(list1[0:10])
print(list1[-4:-1])

a=5
b=5.5
c=7
d=7.5
print(a == int(b) and c!= int(d))
print(a != int(b) and c!= int(d))
print(a != int(b) and c== int(d))



import math
a=77.4
b=math.ceil(a)
#c= math.round(a)
d= math.floor(a)
print(b)
print(c)
print(d)


aList = [123, 'xyz', 'zara', 'abc']
print("A List : ", aList.pop())
print("B List : ", aList.pop(2))



import time
print(time.localtime())
print(time.localtime(time.time()))


import datetime
d = datetime.datetime(2018,5,16)
print('{:%m-%d-%y}'.format(d))
num = 1234567.89
print('{:.2f}'.format(num))

"""


f = open('file1.txt','r')
for line in f:
    print(line, end="")
f.close()


s1 = set() #兩者印出的東西不太一樣，但型別都是set，可以注意一下
print(s1)
s2 = {} #兩者印出的東西不太一樣，但型別都是set，可以注意一下
print(s2)
s3 = set(range(5))
print(s3)
s4 = {1, 1, 2, 1} #可以注意當印出的時候只剩下不重複的元素，也就是只剩1,2而已
print(s4)
s5 = set("aquickbrownfox")
print(s5)

list1 =["1","2","3","4","5","6","7","8","9","10","11","12"]
print(list1[1::2])

import random

def add_score(score,plus,points):
    if plus==True:
        points = points*2
    score = score + points
    return score
points = 5
score = 10
new_score = add_score = add_score(score,True,points)
print(new_score)

