# -*- coding: utf-8 -*-
"""
解决韩信点兵问题
"""

def rs(a):
    if a%3==2:
        if a%5==3:
            if a%7==4:
                print(a)
            else:
                a=a+1
                rs(a)
        else:
            a=a+1
            rs(a)
    else:
        a=a+1
        rs(a)
rs(54)