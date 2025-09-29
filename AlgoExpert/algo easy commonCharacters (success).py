def commonCharacters(strings):
    #Since we need to find a common string in all the elements in the list of strings. We can take any element
    #for this problem let's take the first element.
    firstE = strings[0]
    i = 0
    Common = []
    while i<len(firstE):
        k = 0
        while k<len(strings):
            if firstE[i] not in strings[k]:
                break
            else:
                k+=1
        
        if k == len(strings) and firstE[i] not in Common:
            Common.append(firstE[i])
            i+=1
        else:
            i+=1
    return Common
