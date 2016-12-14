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


# 可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f1= open('dump.text','rb')
d1=pickle.load(f1)
f1.close()
# {'score': 80, 'name': 'bob', 'age': 20}
print(d1)

# 因为JSON表示出来就是一个字符串，可以被所有语言读取
# 要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d2=dict(name='bob',age=20)
f3= json.dumps(d2)
print(f3)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# {'age': 20, 'score': 88, 'name': 'Bob'}
json.loads(json_str)