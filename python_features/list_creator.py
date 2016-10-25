
l = range(1,10)

l1 = list(l) # 非常像个种子 bean

print(l1)

l2 = []
for i in l:
	l2.append(i*i)

print(l2)	
print([ x*x for x in l1]) # 列表生成式用一行语句代替循环生成上面的list：

# 两层循环

print([m + n for m in 'ABC' for n in 'XYZ'])


d={
	'a':'1',
	'b':'2'
}
d1 = [ k+v for k,v in d.items()]
print(d1)

## 总结: 整体看来，这种语法内部的逻辑 基本也是 function return的方式，只不过python进行了足够的简化