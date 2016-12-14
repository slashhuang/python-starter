# 像open()函数返回的这种有个read()方法的对象，
# 在Python中统称为file-like Object
# 文件读写是通过open()函数打开的文件对象完成的
f= open('/Users/slashhuang/personal-repo/github-python/python-starter/std_io.py','r')
file=f.read()
print(file)