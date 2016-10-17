#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ASCII编码和Unicode编码的区别
# ASCII ==> Unicode只需要前面补位0即可（多一倍的存储空间，在存储和传输上就十分不划算）

# Unicode==>utf-8本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

# ==>可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len('fdas')) #4
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) #6


#  格式化
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('hello,%s' % "world")
print('hello,%s%d' % ("world",100))
print('hello,%%s%d' % 100)