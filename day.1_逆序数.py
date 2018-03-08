# -*- coding: utf-8 -*-

number=input('Enter a number:')
number=list(number)
length=len(number)
array=0
for i in range(0,length):
    temp=number[i]
    for j in range(i,length):
        if temp > number[j]:
            array=array+1

print(array)
if array%2==0:
    print('Even arrangement')
else:
    print('Odd arrangement')