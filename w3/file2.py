#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   :2018-1-17 8:16
# @Author :dujia

import os
#if(os.path.exists("file_w")):
#    os.remove("file_w")
f=open("file_w","r+",encoding="utf-8")#读写模式
f.truncate()
print(f.readline())
f.write("hello")
f.flush()#写入后提交写到硬盘
f.seek(0)
print(f.readline())
f.close()

