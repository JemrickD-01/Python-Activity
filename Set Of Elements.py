def addElement(setName):
    aSet= set(())
    only=['y','n']
    choice='y'
    while choice=='y':
        Elem=int(input("Enter element: "+setName+": "))
        aSet.add(Elem)
        choice=input("Enter more?[y or n]: ").lower()
        while choice not in only:
            print("Enter y or n only")
            choice=input("Enter more?[y or n]: ")
    return aSet
def setOps(A,B):
    print("The union of set A and set B: ", A.union(B))
    print("The intersection of set A and set B: ", A.intersection(B))
    print("The difference of set A and set B: ", A.difference(B))
set1=addElement('A')
print("The element of set A is: ",set1)
set2=addElement('B')
print("The element of set B is:",set2)
setOps(set1,set2)
