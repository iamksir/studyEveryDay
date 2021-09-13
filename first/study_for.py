# for x in ...循环就是把每个元素代入变量x
names = ['zhangsan','lisi','wangwu']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' %(i,j,i*j),end='\t')
    print()


row = int(input("请输入行数："))
for i in range(row):
    for _ in range(i+1):
        print('*',end='')
    print()