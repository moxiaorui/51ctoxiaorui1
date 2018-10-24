#!usr/bin/python
# encoding:utf-8
from __future__ import print_function

'''
author:xiaorui
contact:2123018048@qq.com
@file:demo-4.py
@time:2018/10/9 0009 1:22
@welcome to learn ai
'''

p1 = [10,20,11,13,35,23,12,44,13]

p2 = [12,2,17,14,34,24,2,4,3]

dist = 0

if len(p1) != len(p2):
    print('can not compute distance')
    exit(1)

for i1,i2 in zip(p1,p2)  :
    if i1 <0 or i2 < 0:
        dist = 0
        break
    dist += (i1-i2)**2
else :
    print('in else')
dist  = dist ** 0.5

print(dist)
