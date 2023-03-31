def selectionSort(array):
    for i in range(len(array)):
        minIndex=i
        for j in range(i+1,len(array)-1):
            if array[j] < array[minIndex] :
                minIndex=j
        temp=array[i]
        array[i]=array[minIndex]
        array[minIndex]=temp

    return array    



unsorted=[15,0,-9,88,3]
selectionSort(unsorted)
print(unsorted)