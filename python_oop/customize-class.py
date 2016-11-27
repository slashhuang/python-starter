# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
# 定制类，这一章节展示了类的内部操作机制及一些黑魔法



# len ==>  __len__

# __str__ 打印字符串

# 直接显示变量 __repr__

# 返回可遍历对象 __iter__ 

# __next__()方法拿到循环的下一个值


# 实现对可遍历对象下标取值 __getitem__

# 访问类的属性__getattr__

# 只需要定义一个__call__()方法，就可以直接对实例进行调用
class Test():
	def a(a):
		self.a=a
print(callable(Test())) #false

