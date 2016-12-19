#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 子进程

# subprocess模块可以让我们非常方便地启动一个子进程，
# 然后控制其输入和输出

import subprocess

print('$ nslookup www.python.org')
r=subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:',r)

# 子进程还需要输入，则可以通过communicate()方法输入
p = subprocess.Popen(['nslookup'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)




# 参考
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000
