l = [ x*x  for x in list(range(10))]
print(l) # 列表生成器

l1= (x*x for x in list(range(10)))
print(next(l1))

from collections import Iterable
print(isinstance(l1,Iterable))

print('------------\n')


def _generator(max):
	n,tmp=1,['1']
	while n<max:
		starter = [1]
		for index,value in enumerate(tmp): # 采用内置函数，变为可遍历对象
			if(index<len(tmp)-1):
				starter.append(tmp[index]+tmp[index+1])
		starter.append(1) # starter done
		print(tmp)
		yield tmp
		tmp = starter
		n+=1
test = 	_generator(6)
next(test)
next(test)
next(test)
next(test)	
next(test)	


