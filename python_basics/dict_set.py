


# Python内置了字典：dict的支持，dict全称dictionary.
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d={
	'a':'1',
	'b':'2'
}
print(d)

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
# 那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
d['t']=3
print(d)
d.pop('a')
print(d)
print('b' in d)

# set和dict类似，也是一组key的集合，但不存储value
s=set([1,2,2,3])
print(s)
s.remove(2)
print(s)
s.add(4)
print(s)

# 实现的set集合 交并集操作
s1=set([1,3])
s2=set([2,3,4])
print((s1|s2))
print(s1&s2)