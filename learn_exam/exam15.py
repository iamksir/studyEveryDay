import re
while True:
    try:
        a = input()
    except:
        break
    else:
        result = re.findall(r'[A-Z]',a)
        print(len(result))