# 把变量从内存中变成可存储或传输的过程称之为序列化
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化
import pickle
d=dict(name='bob',age=20,score=80)
# 把任意对象序列化成一个bytes
q=pickle.dumps(d)
print(q)
# 写文件
f=open('dump.text','wb')
pickle.dump(d,f)
f.close()