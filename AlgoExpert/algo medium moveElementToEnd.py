def moveElementToEnd(array, toMove):
    for j in array:
        if j == toMove:
            array.remove(j)
            array.append(toMove)
        else:
            continue
    return array

#The function here will tell the array to move a certain element (isolate the element) to the end of the list