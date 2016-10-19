age = 15
if age>=18:
	print('your age is %d'%age)
elif age==15:
	print('your age is exactly 15')
else:
	print('hello world')

_i = input('plese input your age:')
# 基本所有语言都有基本类型的转义规则，动态语言尤其
birth = int(_i)
if birth>20:
	print('u are an adult')
else:
	print('u are student')	