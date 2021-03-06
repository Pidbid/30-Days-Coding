# -*- coding: utf-8 -*-
"""
鸡兔同笼是中国古代的数学名题之一。大约在1500年前，《孙子算经》中就记载了这个有趣的问题。书中是这样叙述的：
今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
这四句话的意思是：
有若干只鸡兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问笼中各有多少只鸡和兔？
"""

head=35
allFoot=94
for rabbit in range(1,head+1):
    if 4*rabbit+2*(head-rabbit)==allFoot:
        print('%d rabbits'%rabbit)
        print('%d chickens'%(head-rabbit))