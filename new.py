a = int(input("input : "))
for x in range(0,a,):
    for y in range(0,x):
        if y%2 == 0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print("\n")