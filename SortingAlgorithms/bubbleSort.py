def bubbleSort(array):
    isSorted=True
    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            isSorted=False

    if(isSorted==False):
        for i in range(0,len(array)):    # len(array)-1 koymak algoritmayı değiştirmiyor
            for j in range(0,len(array)-1-i):
                if(array[j]>array[j+1]):
                    n=array[j+1]
                    array[j+1]=array[j]
                    array[j]=n


    

    return array            






#unsorted=[-2,45,0,11,-9,-99,-150,3,955,8,7]
sorted=[0,1,5]
#bubbleSort(unsorted)
bubbleSort(sorted)
print(sorted)