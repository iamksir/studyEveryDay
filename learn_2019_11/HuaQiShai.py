from random import randint

money = 1000
while money > 0: #验资
    print('你的资产总额为：', money)
    needs_go_on = False
    while True:
        dept = int(input('请下注：'))
        if 0 < dept <= money:
            print('本次下注金额为：',dept)
            break
        else:
            print('你的资产不足，请重新下注！')
    first = randint(1,6) + randint(1,6)
    print('玩家掷出点数为：', first)
    if first == 7 or first ==11:
        print('玩家胜！')
        money += dept
    elif first == 2 or first == 3 or first ==12:
        print('庄家胜！')
        money -= dept
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current  = randint(1,6) + randint(1,6)
        print('玩家掷出点数为：',current)
        if current == 7:
            print('庄家胜！')
            money -= dept
        elif current == first:
            print('玩家胜！')
            money += dept
        else:
            needs_go_on = True
print('你破产了，游戏结束！')



