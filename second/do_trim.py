# 非递归实现
# def trim(s):
#     if 0 == len(s):
#         return s
#
#     while ' ' == s[0]:
#         s = s[1:]
#         if 0 == len(s):
#             return s
#
#     while ' ' == s[-1]:
#         s = s[:-1]
#         if 0 == len(s):
#             return s
#     return s

#递归实现
def trim(s):
    if 0 == len(s):
        return s
    else:
        if s[0] == ' ':
            return trim(s[1:])
        if s[-1] == ' ':
            return trim(s[:-1])
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')