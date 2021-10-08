a = int(input("请输入第1条边"))
b = int(input("请输入第2条边"))
c = int(input("请输入第3条边"))
if a < 0 or b <0 or c<0:
    print("边长不合法")
elif a ==0 or b==0 or c==0:
    print("无法构成三角形")
elif a==b==c:
    print("构成等边三角形")
elif a==b!=c or a==c!=b or b==c!=a:
    print("构成等腰三角形")
else:
    print("构成普通三角形")