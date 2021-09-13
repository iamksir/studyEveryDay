def power(x):
    return x*x

print(power(5))

def power1(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power1(2))


def add_end(L=[]):
    L.append('end')
    return L

print(add_end([1,2]))
print(add_end())
#定义默认参数要牢记一点：默认参数必须指向不变对象！
print(add_end())

def add_end1(L=None):
    if L is None:
        L = []
    L.append('end1')
    return L
print(add_end1())
print(add_end1())

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1,2,3))
num = [2,3,4]
print(calc(*num))