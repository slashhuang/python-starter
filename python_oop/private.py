# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问

class Student():
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s has score %s'% (self.__name,self.__score))
	def set_score(self,score):
		# boolean运算 or and not
		if	score>=10 and score<=100:
			self.__score=score
		else:
			# 抛错
			raise ValueError('bad score')	


a = Student('slashhuang',100)
a.print_score()

a.set_score(99)
a.print_score()

a.set_score(19)
a.print_score()

# 虽然可以通过这种方式访问隐藏的私有变量，not recommended
print(a._Student__score)
