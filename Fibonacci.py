def myFibRecurssion(number):
    if number <=2:
       return 1
    return (myFibRecurssion(number-1)+myFibRecurssion(number-2))

while True:
    factor=int(input("Enter your number: "))
    if factor <=0:
        print(0)
    for i in range(1,factor+1):
        print(i,">",myFibRecurssion(i))
        
