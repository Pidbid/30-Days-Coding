# -*- coding: utf-8 -*-
"""
裴波那契数列的第N项
"""
n=input('请输入裴波那契数列的第N项：')
n=int(n)
# 使用递归
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        all=fib(n-1)+fib(n-2)
        return all

print(fib(n))