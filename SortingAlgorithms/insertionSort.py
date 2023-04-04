def insertionSort(array):
    for i in range(1,len(array)):  
        key=array[i]
        for j in range(i-1,-1,-1):    # if you want don't use while like this
            if(key > array[j]):
                break
            temp=array[j]
            array[j]=key
            array[j+1]=temp

        
                        
    return array



unsorted=[-3,-9,0,8,2,11,-100,7,777,-1000]
sorted=insertionSort(unsorted)
print(sorted)

