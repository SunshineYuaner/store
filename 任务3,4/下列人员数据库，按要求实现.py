names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
# 统计每个人的平均薪资
name1 = []       #定义一个空列表
for i in names:     #i 属于names
    name1.append(i[0])  # 空列表name1添加i，也就是names[0]的名字
name2 = set(name1)     #这是啥？是吧name1列表转为集合？？？
for i in name2:
    k = 0
    money = 0
    for j in names:
        if j[0]==i:
            k+=1
            money += j[5]
    print(f"{i}的工资为{money/k}")

# 统计每个人的平均年龄
name1 = []
for i in names:
    name1.append(i[0])
name2 = set(name1)
for i in name2:
    k = 0
    age = 0
    for j in names:
        if j[0]==i:
            k+=1
            age += int(j[1])
    print(f"{i}的平均年龄为{age/k}")

# 公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.append(["刘备","45","男","220","alibaba",500,"30"])
print(names)

# 统计公司男女人数
gongsi = []
for i in names:
    gongsi.append(i[4])
gongsi1 = set(gongsi)

for i in gongsi1:
    male = 0
    female = 0
    for j in names:
        if j[4]==i:
            if j[2]=="男":
                male += 1
            else:
                female += 1
    print(f"{i}公司有男性有{male}人，女性有{female}人")

# 每个部门的人数
people = []
for i in names:
    people.append(i[6])
people1 = set(people)

for i in people1:
    k = 0
    for j in names:
        if j[6]==i:
            k +=1
    print(f"{i}部门有{k}人")