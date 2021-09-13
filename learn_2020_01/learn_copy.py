import copy

"""
    浅拷贝
"""
#顶层是mutable，子元素全是immutable
a = [1, 'hello', 3]
print(id(a))
print([id(x) for x in a])
b = copy.copy(a)
print(b)
print(id(b))
print([id(x) for x in b])
'''修改后'''
a[0] = 2
print(a)
print(b)
print([id(x) for x in a])
print([id(x) for x in b])

#顶层是mutable，子元素部分immutable
'''修改前'''
A = [10, [20, 30]]
B = copy.copy(A)
print(A, B)
print(id(A), id(B))
print([id(x) for x in A], [id(x) for x in B])
'''修改后'''
A[0] = 100
A[1][1] = 300
print(A, B)
print(id(A), id(B))
print([id(x) for x in A], [id(x) for x in B])

#顶层是immutable，子元素全是immutable
t = (1,2,3)
tc = copy.copy(t)
print(id(t))
print(id(tc))
print([id(x) for x in t])
print([id(x) for x in tc])

#顶层是immutable，子元素部分mutable
a = (1, 2, ['hello', 'world'])
b = copy.copy(a)
print(b)
print(id(a))
print(id(b))
a[2][1] = 'china'
print(a)
print(b)

A = [1,2,3,4]
a = A[:]
print(a)
B = list(A)
print(B)