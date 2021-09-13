try:
    n = int(input())
except ValueError:
    print("请输入一个整型数值")
else:
    if n < 0:
        print("请输入一个正整数")
    else:
        print(bin(n).count('1'))