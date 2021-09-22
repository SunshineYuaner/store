a = int(input("请输入第1条边的长度:"))
b = int(input("请输入第2条边的长度:"))
c = int(input("请输入第3条边的长度:"))
if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    if a==b!=c or a==c!=b or b==c!=a:
        print("构成等腰三角形")
    elif a==b==c:
        print("构成等边三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("构成直角三角形")
    else:
        print("构成普通三角形")
else:
    print("不构成三角形")