def myFib(number):
    if number<=0:
        return None
    if number<3:
        return 1
    summ=0
    num1=1
    num2=1
    for i in range(3,number+1):
        summ=num1+num2
        num1=num2
        num2=summ
    return summ

only=['y','n']
choice='y'
while True:
    myNumber=int(input("Enter your number: "))
    for a in range(1,myNumber+1):
        print(a,">",myFib(a))
    choice=input("Would you like to continue? ")
    while choice not in only:
        print("Enter y or n only")
        choice=input("Would you like to continue? ")
