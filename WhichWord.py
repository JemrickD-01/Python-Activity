def stringLength(fname,lname): 
    if len(fname)>len(lname):
        print(fname,"is longer than",lname)
    elif len(fname)<len(lname):
        print(lname,"is longer than",fname)
    else:         
        print(fname,"and",lname,"have the same size")
choices = ["y","n"]
ans="y"
while ans=="y":
    x=input("enter your first word: ")
    y=input("enter your second word: ")
    stringLength(x,y)
    ans=input("would you like to continue?(y/n): ")
    if ans not in choices:
        print("Enter y or n only")
        ans=input("would you like to continue? y/n")
else:
    print("Done")
     
