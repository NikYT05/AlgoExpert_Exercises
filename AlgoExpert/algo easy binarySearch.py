def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    m = 0
    while True:
        m = (left+right)//2
        if array[m] == target:
            return m
        elif right == left:
            break
        elif target < array[m]:
            right = m-1
        elif target > array[m]:
            left = m + 1
    return -1
            
binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 34)
binarySearch([1,5,23,111], 111)
binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0)
binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354)