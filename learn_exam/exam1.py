n = input()
n = float(n) * 10
if n <= 0:
    print("请输入一个正浮点数")
else:
    n1 = n % 10
    if n1 >= 5:
        print(int(n/10)+1)
    else:
        print(int(n/10))