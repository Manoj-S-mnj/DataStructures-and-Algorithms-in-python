# Bubble sort algorithm

def BubbleSort(array):
    for i in range(0,len(array)):
        for j in range (i+1,len(array)):
            if array[j] < array[i]:
                array[i] , array[j] = array[j] , array[i]
    return array

a = [2,1,4,5,3,7,0]
print(BubbleSort(a))