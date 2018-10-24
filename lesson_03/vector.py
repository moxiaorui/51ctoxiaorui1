#!usr/bin/python
# encoding:utf-8


'''
author:xiaorui
contact:2123018048@qq.com
@file:vector.py
@time:2018/10/11 0011 21:36
@welcome to learn ai
'''

from point import Point
class Vector(Point):

    def norm(self):
        o = Point([0 for i in self.cor])
        result self,dist(o)

    def dot(self,v2):
        result = 0
        for i, j in zip(self.cor, v2.cor):
            result += i * j
            return result
    def cosin(self,v2):
        o = point(*[0 for i in range(len(self.cor))])
        # o = point([o] * len(self.cor))
        d1 = self.dist(o)
        d2 = v2.dist(o)