import random
import datetime

bank = {
    'Frank': {
        'password': '123456',
        'country': '中国',
        'province': '沙河',
        'street': '老牛湾',
        'door': '0001',
        'account': 11111111,
        'bank_name': '汉科软地球中国区老牛湾分行',
        'money': 0
    }
}

money = 0
list_log = []


# {'Frank': {'password': '123456', 'country': '中国', 'province': '沙河', 'street': '老牛湾', 'door': '0001', 'account': 60547549, 'bank_name': '汉科软地球中国区老牛湾分行', 'money': 0}}

def bank_useradd(username, password, country, province, street, door, account):
    bank[username] = {
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "account": account,
        "bank_name": bank_name,
        "money": 0
    }
    return 1


def useradd():
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    print("下面请您输入你的地址：")
    country = input("\t\t请输入你所在的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入你的街道：")
    door = input("\t\t请输入您的门牌号：")
    account = random.randint(10000000, 99999999)

    status = bank_useradd(username, password, country, province, street, door,
                          account)
    if status == 1:
        print("恭喜你成功开户，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door,
                      bank[username]["money"], bank_name))


#查看明细
def write_log(amount,type):
    now = datetime.datetime.now()
    create_time = now.strftime("%Y-%m%d %H:%M:%S")
    data = [create_time,type,amount,f"{money:.2f}"]
    list_log.append(data)


#存钱：
def save(amount):
    global money
    money += amount
    write_log(amount,"存入")

# 取钱
def get(amount):
    global money
    if amount > money:
        print(f"余额不足，目前余额是：{money:.2f}")
    else:
        money -= amount
    write_log(amount, "取出")


# 登录
def login():
    uname = input("请输入您的用户名：")
    if uname in bank.keys():
        pwd = input("请输入您的密码：")
        if pwd == bank[uname]['password']:
            return uname
        else:
            return -1
    else:
        return 0
while True:
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、存钱              ------------|")
    print("|------------3、取钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")
    bank_name = "汉科软地球中国区老牛湾分行"  # 全局变量
    begin = input("请选择业务：")
    if begin == "1":
        useradd()
        a = input("按任意键退出")
        if a == "":
            print()

    elif begin == "2":
        # print("存钱")
        while True:
            # 调用登录
            flag = login()
            if isinstance(flag, str):
                print("登录成功！您的余额为：", bank[flag]['money'])
                amount = float(input(f"请输入存款金额："))
                save(amount)
                bank[flag]['money'] += amount
                print('存款成功，当前余额：', bank[flag]['money'])
                x = input("你想继续存钱吗？N/Y：")
                if x == "Y" or x == "y":
                    continue
                else:
                    a = input("按任意键退出")
                    if a == "":
                        break
            elif flag == 0:
                print("该用户不存在")
                break
            elif flag == -1:
                print('密码错误')
                break

    elif begin == "3":
        # print("取钱")
        while True:
            # 调用登录
            flag = login()
            if isinstance(flag, str):
                print("登录成功！您的余额为：", bank[flag]['money'])
                amount = float(input(f"请输入取款金额："))
                save(amount)
                if amount < bank[flag]['money']:
                    bank[flag]['money'] -= amount
                    print('取款成功，当前余额：', bank[flag]['money'])
                    x = input("你想继续存钱吗？N/Y：")
                    if x == "Y" or x == "y":
                        continue
                    else:
                        a = input("按任意键退出")
                        if a == "":
                            break
                else:
                    print('余额不足')
                    break
            elif flag == 0:
                print("该用户不存在")
                break
            elif flag == -1:
                print('密码错误')
                break

    elif begin == "4":
        # 转账
        while True:
            # 调用登录
            flag = login()
            if isinstance(flag, str):
                print("登录成功！您的余额为：", bank[flag]['money'])
                # 输入转入账户
                uname2 = input(f"请输入转入用户：")
                # 判断用户是否存在
                if uname2 in bank.keys():
                    # 判断转出转入是否同一个人
                    if uname2 != flag:
                        amount = float(input('请输入转账金额：'))
                        # 判断余额是否足够
                        if amount < bank[flag]['money']:
                            # 转出账户余额减少
                            bank[flag]['money'] -= amount
                            print('转账成功，当前余额：', bank[flag]['money'])
                            # 转入账户余额增加
                            bank[uname2]['money'] += amount
                            break
                        else:
                            print('余额不足')
                            break
                    else:
                        print('不能给自己转账')
                        break
                else:
                    print('转入账户不存在')
                    break
            elif flag == 0:
                print("该用户不存在")
                break
            elif flag == -1:
                print('密码错误')
                break

    elif begin == "5":
        print("查询")
        print(list_log)
        a = input("按任意键退出")
        if a == "":
            continue

    elif begin == "6":
        z = input("您确定要退出系统吗？N/Y：")
        if z == "N":
            continue
        else:
            break

    else:
        print("您输入的序号不存在,请重新输入：")
        continue
