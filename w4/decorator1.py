#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   :2018-1-17 8:44
# @Author :dujia

def timer(func):
    def deco():
        print("add new func")
        func()
    return deco

def test1():
    print("test1")
    #time.sleep(3)

def test2():
    print("test2")

@timer #test3=timer(test3)
def test3():
    print("test3")

test1()
test2()
#test3()
print("------添加功能后-------")
test1=timer(test1)
test1()
test2=timer(test2)
test2()
test3()