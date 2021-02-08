# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 04:34:06 2021

@author: 陳淳
"""

#5
born = "2000"
year = "1911"
age = eval(year) - eval(born)
print(type(age))

#6
x1,y1 = 7,2
b = x1 / y1
c = x1 // y1
print(type(b))
print(type(c))

#8
datas = {1:'小明',2:'小美',3:'小王'}
num = input('請輸入座號:')
if not num in datas:
    print('該座號不存在')
else:
    print("學生名字"+datas[num])
    
f = open('file1.txt','r')
eof = False
while eof == False:
    data = f.readline()
    if data !='' :
        if data !='\n':
            print(data.strip())
    else:
        eof =True
        print=("close")
f.close()        