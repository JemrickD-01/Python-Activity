x=int(input("Enter a number: "))
l=(2*x)-2
for i in range(0,x):
    for j in range(0,l):
        print(end=" ")
    l=l-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
