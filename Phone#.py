def function(num):
    if len(num)==11 and num.isdigit():
        for i in range (11):
            if  i<7:
                print("*",end="")
            else:
                print(num[i],end="")
    else:
        print("It should be eleven digit and no letters")
        num=input("Enter number: ")
        function(num)
num=input("Type your phone Number: ")
function(num)
