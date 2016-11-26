
print(type(123)==type('1234'))
# 返回对应的class类型
print(type(123))
print(type('1234'))
# 判断实例isinstance(instance,constructor)

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('a'))
print('ajifdaf\n'.capitalize())


# 似__xxx__的属性和方法在Python中都是有特殊用途的，
# 比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法

print(len('ABC'))
print('ABC'.__len__())

# 可以利用这里面的调用机制轻松改写相关行为
# 还蛮酷的

class MyDog(object):
	def __init__(self):
		self.dog='dog'
	def __len__(self):
		return 100

print(MyDog().__len__())

dog = MyDog()
# 传入第三个default参数
# 这种设计形式其实和JS中的defineProperty ==> get set很类似
print(getattr(dog,'name','default dog'))
