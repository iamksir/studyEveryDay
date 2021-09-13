while True:
    try:
        n = int(input())
        m = 0
        if n == 0:
            break
        else:
            if 1 <= n <= 100:
                while n >= 2:
                    if n == 2:
                        m += 1
                        n = 0
                    m += n // 3
                    n = n // 3 + n % 3
                print(m)
            else:
                print("输入值超出限定范围[1-100]")
    except ValueError:
        print("输入值不正确")
        break