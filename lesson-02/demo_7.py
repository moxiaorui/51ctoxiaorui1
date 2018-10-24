#!usr/bin/python
# encoding:utf-8


'''
author:xiaorui
contact:2123018048@qq.com
@file:demo_7.py
@time:2018/10/9 0009 21:25
@welcome to learn ai
'''

def myopen(filename):
    f = open(filename)
    for line in f :
        #do somethine
        result = line
        yield result
    f.close()

logs = myopen('test.log')
for line in logs:
    print(line)



