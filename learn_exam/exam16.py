import datetime

while True:
    try:
        lst = input().split()
        d = datetime.date(int(lst[0]), int(lst[1]), int(lst[2]))
        print(d)
        print(d.strftime("%j").lstrip('0'))
    except:
        break