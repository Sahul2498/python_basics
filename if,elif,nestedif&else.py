# simple if else statement
# write a program to check the given number is even no
n=int(input('Enter the No :'))
if n % 2 == 0:
    print(n," is Even Number")
else:
    print(n,' is Odd Number')

# Write a program to check vote eligibility
name=input('Enter your Name :')
age=int(input('Enter your Age :'))
if age>= 18:
    print(name , "age is", age ,'Eligible for vote')
else:
    print(name ,'age is ', age ,'Not Eligible for vote')


# simple elif statement with example 

'''
0 no fine
1-5 0.5
5-10  1
10-30 5
>30 Membership cancel
'''
days=int(input('Enter the Days :'))
if days==0:
    print('Good No fine')
elif days>=1 and days<=5:
    print('Fine Amount :',days*0.5)
elif days>5 and days<=10:
    print('Fine Amount :',days*1)
elif days>10 and days<=30:
    print('Fine Amount :',days*5)
else:
    print('Membership is Cancelled')



#simple nested if statement with example
English=int(input('Enter english mark:'))
Tamil=int(input('Enter tamil mark:'))
Maths=int(input('Enter maths mark:'))
Science=int(input('Enter science mark:'))
Social=int(input('Enter social mark:'))

Total=English+Tamil+Maths+Science+Social
print("Total:",Total)
avg=Total/5
print("Average:",avg)
if(English>=35 and Tamil>=35 and Maths>=35 and Science>=35 and Social>=35) or avg>=35:
    Result='pass'
    if avg>=75:
        Result=Result+ ' Distinction'
    elif avg>=65:
        Result=Result+' First class'
    elif avg>=50:
        Result=Result+' Second class'
    else:
        Result=Result+' Third class'
else:
    Result='fail'
print('Result:',Result)



