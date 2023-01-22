#default starting value:0  
#ending value:it will print the end value by end  -1
for i in range(6):# how many rows 
    for j in range(i):# how many columns
        print('*', end='')
    print('')
for i in range(5,0,-1):
    for j in range(i):
        print('*', end='')
    print('') 
# the first loop is used for how many lines we want
# the 2nd loop is uesd to control columns