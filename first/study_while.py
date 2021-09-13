#while循环，只要条件满足就不断循环，不满足时退出
#计算100以内奇数的和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
a = 0
while a < len(L):
    print('hello,', L[a])
    a += 1

#break提前退出循环
n = 1
while n <= 100:
    print(n)
    n = n+1
print('END')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('END')

#cotinue在循环过程中，跳过当前循环，直接开始下一次循环
n = 0
while n < 10:
    n = n+1
    print(n)

n = 0
while n < 10:
    n = n+1
    if n % 2 == 0:
        continue
    print(n)

num = int(input('num='))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)