# Python program to find the ceiling number 
# The floor of the number is the largest number in the array
# That is smaller than or equal to the target number.

def findCeilingNumber(a,t):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = int((high+low)/2)
        if a[mid] == t:
            return a[mid]
        elif t < a[mid]:
            high = mid - 1
            if a[high] < t:
                return a[high]
        else:
            low = mid + 1
        
array = [2,4,3,1,7,6,10,9]
array = sorted(array)
print(array)
target = int(input("Enter Target Number : "))
print(findCeilingNumber(array,target))