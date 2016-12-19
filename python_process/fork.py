#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# process 29093 start...
print('process %s start...'% os.getpid())

pid = os.fork()

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），

# 然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，
# 每当有新的http请求时，就fork出子进程来处理新的http请求。

# if pid == 0:
#     print("i'm a child process %s and my parent is %s" % (os.getpid(),os.getppid()))
# else:
#     print("i %s just created a child process %s" % (os.getpid(), pid))


# multiprocessing
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