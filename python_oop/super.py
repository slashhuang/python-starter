class Animal():
	def run(self):
		print('animal is running')

# 继承
class Dog(Animal):
	def run(self):
		print('dog is running')		

def runTest(animal):
	animal.run()


# 多态
runTest(Dog())	

runTest(Animal())	
print(isinstance(Dog(),Dog))