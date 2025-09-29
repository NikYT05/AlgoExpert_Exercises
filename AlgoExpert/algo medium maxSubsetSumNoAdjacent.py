def maxSubsetSumNoAdjacent(array):
    
    #The following three conditions are base cases.
    if array == []:
        return 0
    
    if len(array) == 1:
        return array[0]
    
    if len(array) == 2:
        return max(array[0], array[1])
    
    #To get the max possible sum in an array one must make an array of non-adjacent sums
    #which will increment as it is being added up
    max_nums = [array[0], max(array[1], array[0])]
    for i in range(2, len(array)):
        maximum = max(max_nums[i-1], max_nums[i-2] + array[i])
        max_nums.append(maximum)
        
    return max_nums[-1]
        
assert maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]) == 330
#ex. [75, 105, 120, 90, 135] the list of maxSums is [75, 105, 195, 195, 285, 330]