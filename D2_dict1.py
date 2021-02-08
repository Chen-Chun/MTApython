# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:29:03 2021

@author: 陳淳
"""

dict1 = {"a":"apple","b":"banana","c":"cat",}
dict1['d'] = 'dog'

for key in dict1.values():
    print(key)
    
for k,v in dict1.items():
    print(k,"->",v)
    
