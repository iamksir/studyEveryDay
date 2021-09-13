try:
    n = int(input())
except ValueError:
    print("请输入一个整型数值")
else:
    n = str(n)
    print(n)
    n = [i for i in n]
    n.reverse()
    print(n)
    n = "".join(n)
    print(n)