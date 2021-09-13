while True:
    try:
        N = int(input())
        a = 2
        s = 0
        for i in range(N):
            s += a
            a += 3
        print(s)     
    except:
        break