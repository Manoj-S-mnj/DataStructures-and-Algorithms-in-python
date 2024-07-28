# Linear Search in Python 

def Linearsearch(a,TargetElement):
    for i in range(0,len(a)):
        if a[i] == TargetElement:
            return "Element found at ",i,"position"
    return "Element not present in the given array "

array = [23,4,5,22,45,67,89,90,12]
target = int(input("Enter target Element : "))
result = Linearsearch(array,target)
print(result)