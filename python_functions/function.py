# lambda函数 匿名函数

p = list(map(lambda x: x*x,[1,2,3]))
print(p);

# 返回函数 ==> 闭包{直接类比JS即可}

def p1(x):
	def p2(y):
		return x+y
	return p2
t = p1(1)	

print(t(2))	

# 装饰器 decorator
# 不希望修改函数的定义.
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）,本质上，decorator就是一个返回函数的高阶函数
# 函数对象有一个__name__属性，可以拿到函数的名字：


def log(func):
	# tuple dict
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now(*args, **kw):
	print('2016-11-8',args)    

now(1,2)
# 方法签名发生了变更！
print(now.__name__)

	# tuple dict

import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('testing')
		return func(*args,**kw)
	return wrapper	

@log
def now(*args, **kw):
	print('2016-11-8',args)    
print(now.__name__)
print(now(1,2))


# practice-----
def log(func):
	def test(*args,**kw):
		print('begin execute')
		func(*args,**kw)
		print('execute done')
	return test	

@log
def ab(s):
	print(abs(s))

ab(4)













