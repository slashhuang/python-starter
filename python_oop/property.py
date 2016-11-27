
# 通过内建变量来过渡setter getter
class Test():
	# getter 函数名和属性名保持一致
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('value should be an integer')
		if value<0 or value>10:
			raise ValueError('value should be between 0 and 10')
		self._score=value	

p=Test()
p.score=10
print(p.score)