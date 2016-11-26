
# 限制实例的属性
class Slot():
	def __init__(self,name='slash'):
		self.name=name

# 创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
p=Slot()
print(p.name)

def test(self,age=18):
	self.age=age
	return age

from types import MethodType

# 给实例添加属性
p.test=MethodType(test,p)
print(p.test())

# 给类添加通用属性、方法

Slot.test=test

print(Slot().test(100))

# 限制实例属性
class Slot1():
	# 使用tuple来描述显示属性
	__slots__=('name','age')
	def __init__(self,age):
		self.age=age

p1 = Slot1('26')
# 报错，不在属性名单内
# p1.test='slashhuang'
# print(p1.test)
p1.name="hello"	
print(p1.name)	

# __slots__定义的属性仅对当前类实例起作用
class Child(Slot):
	pass

p2=Child()
p2.name='ddd'










