#reverse v1
x=input("Enter a word:")
l=len(x)-1

for i in range(l,-1,-1):
    print(x[i])

#reverse v2  
print(input("Enter a word:")[::-1])
