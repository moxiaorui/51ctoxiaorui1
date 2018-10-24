#!usr/bin/python
# encoding:utf-8
from __future__ import print_function

'''
author:xiaorui
contact:2123018048@qq.com
@file:demo-5.py
@time:2018/10/9 0009 20:00
@welcome to learn ai
'''
import time

t1 = time.time()
x = range(1,10000)
t2 = time.time()
y = xrange(1,1000)
t3 = time.time()

print(t2-t1,t3-t2)

