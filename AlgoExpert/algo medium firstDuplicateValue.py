#In this activity we will return the first duplicate value
def firstDuplicateValue(array):
    if len(array) == 0 or len(array) == 1:
        return -1
    #we start with the base case where there is no value or no duplicate
    
    from sys import maxsize
    duplicate = 0
    distance = maxsize
    final = 0
    index = len(array)
    current_element = 0
    found = 0
    #distance is the distance between the number and its duplicate
    #we'll use the index to find the duplicate to return
    
    #in this loop we shorten our array to to save time. When the first duplicate comes out, we return the array between those numbers.
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                array = array[:j+1]
                index = j+1
                break
            break
        
    #this is where we find the duplicate value now
    for i in range(len(array)):
        for j in range(i + 1,index):
            if array[i] == array[j]:
                final = j - i
                current_element = j
                found = 1
                break
            else:
                pass
        
        #we check the distance and the index to see if the current element has a lesser distance and index values.
        #if yes, then we replace these
        if final < distance and current_element < index and found == 1:
            distance = final
            index = current_element
            duplicate = array[index]
        else:
            pass
    
    if found == 0:
        return -1
    else:
        return duplicate


assert firstDuplicateValue([4, 7, 7, 14, 14, 10, 15, 14, 14, 16, 14, 11, 5, 12, 17, 7, 1, 6, 13]) == 7
assert firstDuplicateValue([21, 17, 1, 8, 22, 8, 22, 8, 23, 3, 21, 5, 18, 2, 8, 21, 21, 22, 10, 24, 13, 4, 20, 24]) == 8