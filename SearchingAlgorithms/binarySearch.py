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


def binarySearch(array,key):
    lower=0
    higher=len(array)-1
    while(lower <= higher):
        mid=(higher+lower)//2
        if(array[mid]==key):
            return mid
        elif(array[mid]>key):
            higher=mid-1
        else:
            lower=mid+1
    return -1


unsorted=[3,5,-10,8,11]
sorted=insertionSort(unsorted)
print(binarySearch(sorted,-10))

