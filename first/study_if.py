age = 20
if age >= 18:
    print('you age is',age)
    print('adult')

age1 = 3
if age1 >=18:
    print('adult')
else:
    print('teenager')

age2 = 10
if age2 >=18:
    print('adult')
elif age2 >=6:
    print('teenager')
else:
    print('kid')


age3 = 20
if age3 >=6:
    print('adult')
elif age3 >=18:
    print('teenager')
else:
    print('kid')

#input返回的数据类型是str，不能与整数直接比较
s = input("birth:")
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')