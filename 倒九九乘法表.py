i = 9
while i >= 0:
    j = 1
    while j <= i:
        j += 1
        print(i,"*",j,"=",i*j,end=" ")
    i -= 1
    print()