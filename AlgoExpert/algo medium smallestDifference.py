def smallestDifference(arrayOne, arrayTwo):
    smallest = abs(arrayOne[0]-arrayTwo[0])
    pairs = []
    a = arrayOne[0]
    b = arrayTwo[0]
    
        
    i  = 0
    while i<len(arrayOne):
        j = 0
        while j < len(arrayTwo):
            cole = abs(arrayOne[i]-arrayTwo[j])
            if cole>=smallest:
                j+=1
            else:
                a=arrayOne[i]
                b=arrayTwo[j]
                smallest = cole
        i+=1
        
    pairs.append(a)
    pairs.append(b)
    return pairs