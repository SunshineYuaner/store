count = 3
user1 = "root"
password1 = "admin"
print("欢迎使用本系统")

while count > 0:
    user = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    if user ==user1 and password == password1:
        print("你好，欢迎登陆本系统")
        break
    else:
        print("账号和密码不匹配，请重新输入")
        count -= 1
else:
    print("三次密码输入错误,系统已被锁定，你已被踢出")




