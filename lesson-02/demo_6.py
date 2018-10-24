#!usr/bin/python
# encoding:utf-8


'''
author:xiaorui
contact:2123018048@qq.com
@file:demo_6.py
@time:2018/10/9 0009 20:53
@welcome to learn ai
'''

def euDistance(p1,p2):
    dist = 0

    if len(p1) != len(p2):
        print('can not compute distance')
        return -1

    for i1, i2 in zip(p1, p2):
        if i1 < 0 or i2 < 0:
            dist = -1
            break
        dist += (i1 - i2) ** 2
    else:
        dist = dist ** 0.5
    return dist

if __name__== '__main__ ':
    print(euDistance((10,20),(20,30)))