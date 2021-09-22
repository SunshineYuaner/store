import random

shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["阿玛尼", 300],
    ["圣罗兰",288],
    ["辣条",2.5],
    ["老干妈",13]
]
while True:
    user = input("请输入账号")
    password = int(input("请输入密码"))
    if user == "root" and password == 123:
        money = int(input("请输入你的金额："))
        # 优惠券
        ticket = random.randint(1, 10)
        print(f"恭喜您抽中了{ticket}元的优惠券")
        mycart = []
        print(f"序号---名称---价格")
        for index, value in enumerate(shop):
            print(f"{index + 1}----{value[0]}----{value[1]}")


        while True:
            result = 0
            choose = input("请输入你要买的商品的序号：")
            if not mycart:
                pass
            else:
                for item in mycart:
                    result += item[1]
            if choose.isdigit():
                choose = int(choose)
                if 0 < choose <= len(shop):
                    if money-result >= shop[choose - 1][1]:
                        mycart.append(shop[choose - 1])
                        print("加入购物车成功!!,输入Q/q结账")
                    else:
                        print("您的资金不足，购物车已满，输入Q/q结账")
                else:
                    print("商品不存在！！")
            elif choose == 'Q' or choose == 'q':
                print("购物结束，欢迎下次光临！")
                if not mycart:
                    print("您本次没有购买商品")
                else:
                    if mycart.count(["辣条", 10]) >= 10:
                        result -= 0.3
                    elif mycart.count(["老干妈", 10]) >= 20:
                        result -= 0.9
                    print("您的购物清单如下：")
                    newcart = []
                    for item in mycart:
                        if [item[0], mycart.count(item)] not in newcart:
                            newcart.append([item[0], mycart.count(item)])
                    for x in newcart:
                        print(x[0], "X", x[1])
                    print("您的余额为：", money - result + ticket, "元")
                    break
            else:
                print("输入非法！！")
    else:
        print("你的账号或密码有误，请重新输入")
