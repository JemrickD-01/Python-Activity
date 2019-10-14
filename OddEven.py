def numberEvenOdd(x):
    
    if (x%2==0):
        print("Its an even number")
    else:
        print("Its an odd number")
choices=["y","n","Y","N"]        
ans="y" or "Y"
while ans=="y":
    a=int(input ("Enter your number: "))
    numberEvenOdd(a)
    ans=input ("Would you like to continue?[Y or N]: ")
    if ans not in choices:
        print("Enter y or n only")
        ans=input ("Would you like to continue?: ")
else:
    print("Done")

    
