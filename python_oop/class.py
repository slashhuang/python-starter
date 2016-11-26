

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。

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
