




# Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
print(os.name) #posix portable operating system interface
_path = os.environ.get('PATH')
print(_path)

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 绝对路径
_dir = os.path.abspath('.')
print(_dir)
os.mkdir('%s/hello'%(_dir))