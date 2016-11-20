#！/usr/bin/env python3
# -*- coding:utf-8 -*-
'testing module for module_basic.py' # 第一个字符串视为注释

__author__='slashhuang' # __xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途

import sys

def test():
	args = sys.argv #使用list存储argv
	if len(args)==1:
		print('hello world')
	elif len(args)==2:
		print('hello %s!' % args[1])
	else:
		print('Too many arguments')

 #_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
if __name__=='__main__':
	test()
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试
## 运行python3 module_basic.py

# private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，
# 但是，从编程习惯上不应该引用private函数或变量。