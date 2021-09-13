# def fib(num):
#     """生成器"""
#     a, b = 0, 1
#     for _ in range(num):
#         a, b = b, a + b
#         yield a
#
# class Fib(object):
#     """迭代器"""
#
#     def __init__(self, num):
#         self.num = num
#         self.a, self.b = 0, 1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx < self.num:
#             self.a, self.b = self.b, self.a + self.b
#             self.idx += 1
#             return self.a
#         raise StopIteration('迭代结束')
#
# if __name__ == '__main__':
#     f = Fib(10)
#     for i in f:
#         print(i)

#列表生成式
list = [x * x  for x in range(10)]
print(list)
#生成器
generator_ex = (x * x for x in range(10))
print(generator_ex)

for _ in range(10):
    print(next(generator_ex))


