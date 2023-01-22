
#continue statement 
#print odd no

'''i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue;
    print(i)
    i+=1
'''

# Remove ',' from a string

str='A,B,C,D,E'
str2=''

for i in str:
    if i ==',':
        continue
    str2 = str2 + i
print(str2)