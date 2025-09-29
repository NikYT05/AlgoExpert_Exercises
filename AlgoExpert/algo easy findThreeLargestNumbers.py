def findThreeLargestNumbers(array):
    Largest = []
    biggest = array[0]
    bigger = array[1]
    big = array[2]
    for i in range(3):
        array.pop(0)
    
    for i in array:

        if i>biggest:
            big = bigger
            bigger = biggest
            biggest = i
            
        elif i>big and i>bigger and i<=biggest:
            big = bigger
            bigger = i
            
        elif i>big and i<=bigger and bigger==biggest:
            big = i
            
        elif i>big and i == bigger and i < biggest:
            big = i
            
        elif i>big and i < bigger:
            big = i
            
        elif i == big and i < bigger:
            continue
        
        else:
            continue
        
    if big <= bigger and bigger <= biggest:
        Largest.append(big)
        Largest.append(bigger)
        Largest.append(biggest)
        
    elif big <= biggest and biggest <= bigger:
        Largest.append(big)
        Largest.append(biggest)
        Largest.appned(bigger)
        
    elif bigger <= big and big <= biggest:
        Largest.append(bigger)
        Largest.append(big)
        Largest.append(biggest)
        
    elif bigger <= biggest and biggest <= big:
        Largest.append(bigger)
        Largest.append(biggest)
        Largest.append(big)
        
    elif biggest <= bigger and bigger <= big:
        Largest.append(biggest)
        Largest.append(bigger)
        Largest.apppend(big)
        
    elif biggest <= big and big <=bigger:
        Largest.append(bigger)
        Largest.append(big)
        Largest.append(bigger)
        
    
    return Largest

assert findThreeLargestNumbers([10, 40, 20, 104, -12, 104]) == [40, 104, 104]