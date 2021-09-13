n = input()
if n.islower() == False:
    print("字符串中只能包含小写字母")
else:
    if len(n) > 1000:
        print("字符串长度不能超过1000")
    else:
        print(n[::-1])
