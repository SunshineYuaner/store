# 实现输入10个数字，并打印10个数的求和结果
sum1 = int(input("请输入第1个数："))
sum2 = int(input("请输入第2个数："))
sum3 = int(input("请输入第3个数："))
sum4 = int(input("请输入第4个数："))
sum5 = int(input("请输入第5个数："))
sum6 = int(input("请输入第6个数："))
sum7 = int(input("请输入第7个数："))
sum8 = int(input("请输入第8个数："))
sum9 = int(input("请输入第9个数："))
sum10 = int(input("请输入第10个数："))
list = [sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,sum10]
Max = max(list)
print("这10个数中最大的为：",Max)
sum = sum1 + sum2 + sum3 + sum4 + sum5 +sum6 +sum7 + sum8 +sum9 + sum10
print("10个数的总和为",sum)
aug = sum / len(list)
print("平均数为：",aug)


