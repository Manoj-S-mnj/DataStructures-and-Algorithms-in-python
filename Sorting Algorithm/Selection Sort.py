# Selection Sort Algorithm

def SelectionSort(array):
    for i in range(0,len(array)):
        minimum = i
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                minimum = j
        array[i],array[minimum] = array[minimum],array[i]
        
    return array 

a = [2,1,3,4,8,6,5,9]
print(SelectionSort(a))