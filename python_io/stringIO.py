



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
