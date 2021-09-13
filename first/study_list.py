#list一种有序的集合

classmates = ['zhangsan','lisi','wangwu']
print(classmates)
#用索引访问list中每一个位置的元素
print(classmates[0])
print(classmates[-2])

#超出索引报'indexError'
#print(classmates[4])

#用len()获取list元素的个数
a = len(classmates)
print(a)

#lisr是一个可变的有序表，可以用append()追加元素到末尾
classmates.append('zhouliu')
print(classmates)
#通insert()将元素插入到指定位置
classmates.insert(0,'wuer')
print(classmates)
#用pop()删除末尾的元素
classmates.pop()
print(classmates)
#用pop(索引)删除指定位置的元素
classmates.pop(0)
print(classmates)
#可通过执行赋值的方式替换对应索引位置的元素
classmates[0] = 'zhangyi'
print(classmates)
#list里面的数据可以不同
L = [123,12.0,'QWE']
print(L)
#list可以嵌套使用
s = ['a','b',['c','d'],'e']
print(s)
b = len(s)
print(b)
print(s[2][0])