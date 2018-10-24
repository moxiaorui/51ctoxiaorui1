#!usr/bin/python
# encoding:utf-8
from __future__ import print_function

'''
author:xiaorui
contact:2123018048@qq.com
@file:demo-3.py
@time:2018/10/7 0007 23:19
@welcome to learn ai
'''

p1 = [10,20]
p2 = [14,34]

dist = ( (p1[0] -p2[0])**2 + (p1[1]-p2[1])**2 ) ** 0.5
print(dist)


p1 ={'x' : 10,'y' : 20}
p2 ={ 'y': 34,'x' : 14}
dist = ( ( p1[ 'x']-p2['x'])**2 +(p1['y']-p2['y'])**2) ** 0.5
print(dist)
