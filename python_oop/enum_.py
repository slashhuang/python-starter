





from enum import Enum
# Month= Enum('Month',('1','2'))

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 下面两个的返回值是一致的
print(Month.Jan)
print(Month(1))


# value属性则是自动赋给成员的int常量，默认从1开始计数
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 这里我运行的时候出现了bad magic number error
# http://stackoverflow.com/questions/514371/whats-the-bad-magic-number-error
