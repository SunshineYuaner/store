import random
ran = random.randint(0,100)
moneyall = 500
count = 3

while count > 0 :
    num = int(input("请猜一个我心里想的数字："))
    print(ran)
    if num == ran:
        print("太棒了，恭喜你猜对了")
        moneyall = moneyall + 10
        count = count - 1
    elif num  < ran:
        print("你猜小了")
        moneyall = moneyall - 100
        count = count - 1
    else:
        moneyall = moneyall - 100
        print("你猜大了")
        count = count - 1
    print("你还有",count,"次机会哦,你还剩下：", moneyall,"元")

    i = input("继续吗? 不玩了/继续：")
    if i == "不玩了":
        print('退出游戏成功')
        break



