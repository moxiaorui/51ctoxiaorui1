#!usr/bin/python
# encoding:utf-8


'''
author:xiaorui
contact:2123018048@qq.com
@file:demo_9_plus.py
@time:2018/10/11 0011 20:47
@welcome to learn ai
'''

from demo_9 import point

class Vector(point):
    def dot(self,v2):
        result = 0
        for i,j in zip(self.c,v2.c):
            result += i *j
            return result

    def cosin(self,v2):
       o =  point(*[0 for i in range(len(self.c))])
       # o = point([o] * len(self.c))
       d1 = self.dist(o)
       d2 = v2.dist(o)

       result = 1.0 * self.dot(v2) / (d1 * d2)
       return result

v1 = Vector((0,1))
v2 = Vector((1.0))
print(v2.cosin(v2))

