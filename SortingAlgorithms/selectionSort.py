def selectionSort(array):
    for i in range(len(array)):
        minIndex=i
        for j in range(i+1,len(array)):
            if array[j] < array[minIndex] :
                minIndex=j
        temp=array[i]
        array[i]=array[minIndex]
        array[minIndex]=temp

    return array    



unsorted=[8,-9,1,3,83,5]
sorted=selectionSort(unsorted)
print(sorted)