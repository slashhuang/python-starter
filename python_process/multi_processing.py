#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multiprocessing
# multiprocessing模块提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os

def run_proc(name):
    print('run child process %s (%s)...' % (name,os.getpid()))
# 创建子进程时，只需要传入一个执行函数和函数的参数，
# 创建一个Process实例，
# 用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
if __name__=='__main__':
    print('parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end.')