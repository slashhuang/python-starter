# 注释
# 采用缩进来映射语法，当语句以冒号:结尾时，缩进的语句视为代码块。
# Python程序是大小写敏感的

a=101
if a>100:
	print(a)
else:
	print(-a)	

# 数据类型和变量
# 整数:	Python可以处理任意大小的整数，当然包括负整数;十六进制用0x前缀和0-9【和JS一致】
print(0x123)
# 浮点数
print('float num',1.2e-5)

# 字符串
# \n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\\//fda')

# 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''fuck
you
hello''')

# 布尔值
# 一个布尔值只有True、False两种值
# 运算层面: 用and、or和not运算。 ===>not为单目运算
print('boolean',True and True)
print('boolean',True and False)
print('boolean',True or False)

print('boolean', not False)

# 空值
#空值是Python里一个特殊的值，用None表示。

# 变量
# 变量名必须是大小写英文、数字和_的组合

# >>>>变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言


# 常量

# 所谓常量就是不能变的变量


# 在Python中，有两种除法，一种除法是/： ==>结果为浮点数
print(10/3)
# 一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10//3)
 # %取余数
print(10%3)

