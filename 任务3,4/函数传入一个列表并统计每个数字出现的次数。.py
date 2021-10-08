# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据

list = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]


def counts(list1):
    result = {}
    a = set(list1)
    for value in a:
        count = 0
        for i in list1:
            if value == i:
                count += 1
        result[value] = count
    return result


j = counts(list)
print(j)
