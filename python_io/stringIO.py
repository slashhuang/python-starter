



# StringIO顾名思义就是在内存中读写str。


from io import StringIO
f=StringIO()
f.write('hello')
f.write('    world!')
print(f.getvalue()) 
# hello world

f1= StringIO('hello \n\nw\norld')
i=0
while True:
	s=f1.readline()
	i=i+1
	if s=='':
		break
	print(s.strip()+str(i))	

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
print('BytesIO started === ===')
from io import BytesIO
q= BytesIO()
word = q.write('中文'.encode('utf-8'))
print(word)


