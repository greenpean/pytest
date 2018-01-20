#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   :2018-1-19 16:50
# @Author :dujia


#装饰器

def deco(func):
    print("add new func")
    return func

@deco
def test1():
    print("test1")
    #time.sleep(3)

test1()
# print("------添加功能后-------")
# test1=deco(test1)
# test1()