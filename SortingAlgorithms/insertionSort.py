def insertionSort(array):
    for i in range(1,len(array)-1):
        key=array[i]
        for j in range(i-1,0,-1):    #mistake
            if(key>array[j]):      
                temp=array[j]
                array[j]=array[j-1]
                array[j-1]=temp
                        
    return array



unsorted=[-3,-9,0,8,2,11]
insertionSort(unsorted)
print(unsorted)

