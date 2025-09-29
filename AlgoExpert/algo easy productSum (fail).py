def productSum(array):
    num =0
    SENTRY = 1
    while array != []:
        if type(array[0]) == list:
            SENTRY += 1
            num += SENTRY*(productSum(array[0]))
            array.pop(0)
            
        else: 
            num += array.pop(0)

    return num

#assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12   
assert productSum([5, 2, [7, -1], 3]) == 22
assert productSum([[[3]]]) == 12