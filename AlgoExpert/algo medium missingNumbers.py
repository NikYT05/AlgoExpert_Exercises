def missingNumbers(nums):
    missing = []
    nums = sorted(nums)
    
    i = 1
    while i<=len(nums)+2:
        if i not in nums:
            missing.append(i)
            i+=1
        else:
            i+=1
    
    return missing

missingNumbers([2,3])
missingNumbers([1,3])
missingNumbers([1,2])