hight = 20
day = 0
while hight > 0:
    hight = hight - 3
    day += 1
    if hight <= 0:
        break
    hight = hight + 2
print(day)