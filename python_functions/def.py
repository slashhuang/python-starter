def power(x):
	return x*x

# 将参数的默认值指向不可变对象
def power1(x=None):
	if x is None:
		x=[]
	x.append('yes! x is immutable now ')
	return x	

# 当参数的默认值是可变对象的时候，除非进行变量覆盖，不然reference还是相同
def power2(x=[]):
	x.append('test1')
	return x		

print(power(1))
print(power1(['test']))
print(power2(['test2']))
print(power2())
print(power2())
# 可变参数
def _c(*l):
	sum=0
	for i in l:
		sum = sum+ i
	return sum
# 对于list或者tuple进行可变参数变换
print(_c(1,2))
print(_c(*[1,2]))	
print(_c(*(1,2)))

# 关键字参数,这些关键字参数在函数内部自动组装为一个dict ==>  最后以tuple的形式输出
def person(name,age,**kw):
	print('name',name,'age',age,kw)

test= {'city':'shanghai','job':'it engineer'}
person('slash','25',**test)

# ****位置参数和命名关键字参数****
def person1(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name',name,'age',age,'other',kw)

person1('slash',25,**{"a":1})	
# 命名关键字参数：

def person2(name,age,*,city,job):
	print(name,age,city,job)

# positional arguments vs  key code arguments
person2('slash',25,city='shanghai',job='it')


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a,b=1,*c,**d):
	print(a,b,c,d)

f1('u','are',{'awesome':'awesome'},c=1,d=2)

def f2(a,b=1,*,job,engineer):
	print(a,b,job,engineer)
f2('u','are',job=1,engineer=2)
# 小结

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


	


















		

