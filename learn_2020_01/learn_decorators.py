# #日志打印器
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print('我准备开始计算:{}函数了:'.format(func.__name__))
#
#         # 真正执行的是下面
#         func(*args, **kwargs)
#         print('大功告成')
#     return wrapper
#
# @logger
# def add(x, y):
#     print('{} + {} = {}'.format(x, y, x + y))
#
# add(100,200)

# from functools import wraps
# import time
#
# '''输出函数执行时间的装饰器'''
# def record_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__}函数执行了{end - start}秒')
#     return wrapper
#
#
# @record_time
# def want_sleep(sleep_time):
#     time.sleep(sleep_time)
#
# want_sleep(2)

# from functools import wraps
# from time import time
#
# def record(output):
#     '''自定会带参数的装饰器'''
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return result
#         return wrapper
#     return decorate
#
# @record(print)
# def add(x, y):
#     print('{} + {} = {}'.format(x, y, x + y))
#
# add(10, 20)

# def say_hello(country):
#     def wrapper(func):
#         def deco(*args, **kwargs):
#             if country == 'china':
#                 print('你好')
#             elif country == 'america':
#                 print('hello')
#             else:
#                 return
#             func(*args, **kwargs)
#         return deco
#     return wrapper
#
# @say_hello('china')
# def chinese():
#     print('我来自中国')
#
# @say_hello('america')
# def american():
#     print('I am from America')
#
# chinese()
# print('----------')
# american()

# from functools import wraps
# def wrapper(func):
#     @wraps(func)
#     def inner_function():
#         pass
#     return inner_function
#
# @wrapper
# def wrapped():
#     pass
# print(wrapped.__name__)
# '''等价于'''
# def wrapped():
#     pass
# print(wrapper(wrapped).__name__)

import time
import functools

class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)

def delay(duration):
    """
    装饰器：推迟某个函数的执行。同时提供.eager_call方法立即执行
    """
    return functools.partial(DelayFunc,duration)

@delay(duration=1)
def add(a, b):
    print(a + b)


print(add)
add(3, 5)

