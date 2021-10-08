list =[["罗恩", 23 ,35 ,44],
["哈利",60, 77 ,68 ,88, 90],
["赫敏", 97 ,99 ,89 ,91, 95, 90],
["马尔福",100, 85 ,90]]
# 求每个人的总成绩？
for i in list:
    sum = 0
    for j in i:
        if isinstance(j,int):
            sum += j
    print(f"{i[0]}的总成绩是{sum}")