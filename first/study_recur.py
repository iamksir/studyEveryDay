def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(6))
#使用递归函数需要注意防止栈溢出

#汉诺塔移动
def move(n,a,b,c):
    if n == 1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        # print('move',a,'-->',c)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')