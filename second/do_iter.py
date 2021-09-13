#判断一个对象是否可迭代
from collections import Iterable

i = isinstance('abc',Iterable)
print(i)
i = isinstance([1,2,3],Iterable)
print(i)
i = isinstance(123,Iterable)
print(i)

# 对list实现类似Java那样的下标循环
for a,value in enumerate(['A','B','C']): #enumerate函数可以把一个list变成索引-元素对
    print(a,value)


def findMinAndMax(L):
    if L != []:
        (max,min) = (L[0],L[0])
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
        return (min,max)
    else:
        return (None,None)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
