def subarraySort(array):
    start, end = 0, 0
    # These will tell us if we found the unsorted index
    start_u = False
    for i in range(len(array)):
        #print(start_u)
        if i == 0:
            if array[i] > array[i+1]:
                start_u = True
            else:
                continue
            
        elif i == len(array) - 1:
            if array[i] < array[i-1]:
                end = i
            else:
                continue
        else:
            if (array[i] > array[i+1] or array[i] < array[i-1]) and not start_u:
                start_u = True
                start = i
            elif array[i] > array[i+1] or array[i] < array[i-1]:
                end = i
            else:
                continue
            
    if start == 0 and end == 0:
        return [-1, -1]
    
    minimum, maximum = min(array[start:end+1]), max(array[start:end+1])
    
    start_u = False
    end_u = False
    for i in range(len(array)):
        if i == len(array) - 1:
            if array[i] < maximum and not end_u:
                end = i
                end_u = True
                
        # Check if we are at the start.
        elif i == 0:
            if array[i] > minimum:
                start = 0
                start_u = True
            
        else:
            if array[i] > minimum and not start_u:
                start = i
                start_u = True
            elif array[i] > maximum and not end_u:
                end = i - 1
                end_u = True
            else:
                continue
    
    return [start, end]
            
    
A = [1,2,4,7,10,11,7,12,6,7,16,18,19]
B = [1,2,8,4,5]
print(subarraySort(A))
print(subarraySort(B))
print(len(A))