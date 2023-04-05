
def linearSearch(array,key):
    for i in range(len(array)):
        if(array[i]==key):
            return i

    return -1



array=[2,4,8,7,10,-5]
print(linearSearch(array,4))
print(linearSearch(array,100))