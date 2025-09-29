def spiralTraverse(array):
    traverse = []
    i=0
    j=0
    while array != []:
        
        for i in array:
            if i == []:
                array.pop(i)
            else: continue
        
        while array[i]!=[]:
            traverse.append(array[i][j])
            array[i].pop(0)
            
        array.pop(0)
        print(array)
        
        if array == []:
            break
        
        j = -1
        while len(array) > i:
            traverse.append(array[i][j])
            array[i].pop(j)
            i+=1
        print(array)
        
        if array == []:
            break
        i-=1
        while array[i]!=[]:
            traverse.append(array[i][j])
            array[i].pop(j)
        
        
        array.pop(j)
        if array == []:
            break
        
        print(array)
        j = 0
        i = len(array)-1
        while i!=0:
            traverse.append(array[i][j])
            array[i].pop(0)
            i-=1
            
        print(array)
        if array==[]:
            break

    return print(traverse)

array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]

array2 = [["A", "L", "I", " ",],
          ["I","<3","U","T"],
          [" ","!","!","A"],
          ["E","S","A","M"]]

array3 = [[1,2,3],
          [8,9,4],
          [7,6,5]]

array4 = [
    [1, 11],
    [2, 12],
    [3, 13],
    [4, 14],
    [5, 15],
    [6, 16],
    [7, 17],
    [8, 18],
    [9, 19],
    [10, 20]]

spiralTraverse(array4)
#spiralTraverse(array)

#spiralTraverse(array2)
        
#spiralTraverse(array3)