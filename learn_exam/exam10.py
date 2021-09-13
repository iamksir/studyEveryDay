def perfnum(n):
    if n<4:return 0
    else:
        pnn=0
        for mm in range(4,n+1): #calculate perfact number
            sum = 0
            for s in range(1,mm//2+2):
                if mm%s==0:sum+=s
            if sum==mm:pnn+=1
        return pnn
while 1:
    try:
        n=int(input())
        print(perfnum(n))
    except:break