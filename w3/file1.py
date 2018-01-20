#!/usr/bin/env python
# Author:dujia

#逐行打印
f=open("file","r",encoding="utf-8")
for line in f:
    print(line)
f.close()

f=open("file","r",encoding="utf-8")
print(f.readline())
print(f.tell())#打印读取的当前位置
f.seek(0)#回到位置0
print(f.readline())
print(f.encoding)#打印文件编码
print(f.fileno())#文件句柄
if(f.readable()):#是否可读
    print("readable")
else:
    print("unreadable")