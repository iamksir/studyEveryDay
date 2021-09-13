while True:
    try:
        n = int(input())
        res = -1
        if n < 3:
            res = -1
        elif n % 3 == 0:
            res = 2
        elif n % 4 == 0:
            res = 3
        else:
            res = 4
        print(res)
    except:
        break