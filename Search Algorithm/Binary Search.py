# Search an diven Element by using Binary search Algorithm

def binarySearch(b,element):
    low = 0
    high = len(b)-1
    while low <= high:
        mid = int((high + low)/2)
        if b[mid] == element:
            return "Element found"
        elif element < b[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Element Not found"

a = [2,3,5,1,6,7,9,8,4,10,12,11]
#Binary search Needs a Sorted array
a = sorted(a)
element = int(input("Enter element to be find : "))
print(binarySearch(a,element))