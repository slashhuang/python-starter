# 迭代
'''
	for ... in ...
	from collections import Iterable
'''

d={'a':1,'b':2}
for key in d:
	print( key )


e = [1,2,3]
for i,value in enumerate(e): # 将list列表转化索引元素对
	print (i,value)


from collections import Iterable
 
print(isinstance([1,2],Iterable)) # True
