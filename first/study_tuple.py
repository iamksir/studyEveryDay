#元组(tuple)和list非常相似，但tuple一旦初始化就不能修改

classmates = ('zhangsan','lisi','wangwu')
print(classmates)
#元组的小陷阱
t = (1)  #此处定义的并非元组，而是小括号 eg：仅当元组中元素只有1个时
print(t)
#当元组中元素只有一个是，加,来区分
d = (1,)
print(d)
#'可变的'tuple
b = ('a','b',['A','B'])
print(b)
b[2][0] = 'X'
b[2][1] = 'Y'
print(b)