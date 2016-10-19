age = 15
if age>=18:
	print('your age is %d'%age)
elif age==15:
	print('your age is exactly 15')
else:
	print('hello world')

_i = '2'
# 基本所有语言都有基本类型的转义规则，动态语言尤其
birth = int(_i)
# 条件语句
if birth>20:
	print('u are an adult')
else:
	print('u are student')	

# 循环语句
names = ['1',2,3]

# range函数生成正数序列
for name in names:
 	print(name)
print(list(range(5)))	

# while循环
count=10
sum=0
while(count>0):
	sum+=count
	count=count-1
print(sum)	

