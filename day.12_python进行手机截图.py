# -*- coding: utf-8 -*-
import os

'''
进入当前目录，调用ADB
'''
path=os.getcwd()+'/adb/'
os.system(path+'/adb.exe shell screencap -p /sdcard/name.png')
os.system(path+'adb.exe pull /sdcard/name.png D:/name.png')
print('finish')