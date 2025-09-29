def selectionSort(array):

    k = 0
    smallest = array[k]
    index_of_smallest = 0
    
    while k < len(array)-1:
        for i in range(k, len(array)):
            if smallest > array[i]:
                smallest = array[i]
                index_of_smallest = i
            else:
                continue
        
        array[index_of_smallest] = array[k]
        array[k] = smallest
        print(smallest)
        print(array)
        
        k += 1
        smallest = array[k]

    return array
#The problem with the first implementation is it will keep swapping the numbers regardless of whether a swap is needed
#selectionSort([8, 5, 2, 9, 5, 6, 3])
#selectionSort(([1,2,3]))

def SS(array):
    
    k = 0
    smallest = array[k]
    index_of = 0
    
    while k < len(array):
        smallest = array[k]
        for i in range(k, len(array)):
            if smallest > array[i]:
                smallest = array[i]
                index_of = i
            else:
                continue
            
        if smallest < array[k]:
            array[index_of] = array[k]
            array[k] = smallest
            k += 1

        else:
            k += 1

            
    return array

SS([8, 5, 2, 9, 5, 6, 3])
SS(([1,2,3]))