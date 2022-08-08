def kthElement(Arr1, Arr2, k):
    
    #initialize array index at the start position
    i = 0
    j = 0
    x = 0

    #initialize a new array
    newArr = [0] * (len(Arr1) + len(Arr2))
    while(i < len(Arr1) and j < len(Arr2)):
        if(Arr1[i]< Arr2[j]):
            newArr[x] = Arr1[i]
            i+=1
            x+=1
        else:
            newArr[x] = Arr2[j]
            j+=1
            x+=1
    
    while(i < len(Arr1)):
        newArr[x] = Arr1[i]
        i+=1
        x+=1

    while(j < len(Arr2)):
        newArr[x] = Arr2[j]
        j+=1
        x+=1

    return newArr[k-1]
            
array1 = [1, 3, 3, 5, 7]
array2 = [2, 4, 9, 10]

print (kthElement(array1, array2, 5))