class Student():
	# self为实例变量
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def printScore(self):
		print('%s has score %s' % (self.name , self.score))
		return self.score	

bart = Student('slashhuang','100')
bart.test="test"

print(bart.printScore())

print(Student)
