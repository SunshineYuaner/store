# i = 1
# j = 1
# result = 0
# res = 1
# while i <= 20:
#     while j <= i:
#         res *= j
#         j += 1
#     result += res
#     i += 1
# print(result)

res =1
sum = 0
for i in range(1,21):
    res = i *res
    print(res)
    sum += res
print("阶乘和是：",sum)
