# 类属性 实例属性


class Test(object):
	def __init__(self):
		self.name="instance property"

	name='Test'

p = Test()
print(hasattr(p,'name'))

# 实例属性覆盖类属性
print(p.name)
# 都能打印出'Test'
print(Test.name)

		
