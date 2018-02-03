#Author:Jerom

#-*- coding:gbk -*-

#import sys

#print(sys.getdefaultencoding())
s="你好"
#print(s,type(s))
#s_to_unicode=s.decode()
#print(s_to_unicode)
s_to_gbk=s.encode("gbk")
print(s_to_gbk)