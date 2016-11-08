def add(x,y,fn):
	return fn(x)+fn(y)

x=5
y=-8
print(add(x,y,abs))	

import builtins
print(builtins.abs)
# 内建函数对象

def f(x):
	return x*x

p = map(f,[2,1,3])	
# p为惰性序列，需要list进行类型转换
print(list(p))
print(list(range(5)))

# 手动引入函数工具
from functools import reduce
def fn(x,y):
	return x+y
s = reduce(fn,[1,5,4,5])
print(s)

def calc(x,y):
	return 10*x + y
def stringToInt(s):
	 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# just iterable
test = reduce(calc,map(stringToInt,'123445'))
print(test)

print(str.lower('ffTT'))


