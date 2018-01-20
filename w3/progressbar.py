#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   :2018-1-17 8:44
# @Author :dujia

import sys,time

print("start")
for i in range(10):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(1)
print("\nend")

