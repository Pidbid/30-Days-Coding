# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:37:52 2018

@author: wicos
"""

a=input('请输入一个数：')
a=int(a)
c=0
for i in range(2,a):
    if a%i==0:
        c=c+1
if c==0:
    print('%d是素数'%a)
else:
    print('%d不是素数'%a)
        