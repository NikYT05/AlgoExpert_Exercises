def fourNumberSum(array, targetSum):
    # we can create a list of pairs to do this. 
    n = len(array)
    pairs = []
    answer = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            pairs.append({array[i], array[j]})
    
    # this indeed returns the pairs of integers
    """
    The problem with this implementation is that it repeats numbers that were inside the array
    print(pairs)
    print("\n")
    m = len(pairs)
    x = []
    for i in range(m - 1):
        for j in range(i + 1, m):
            if sum(pairs[i]) + sum(pairs[j]) == targetSum:
                x.extend(pairs[i])
                x.extend(pairs[j])
                answer.append(x)
                x = []
        
        print(f'this is x: {x}\n')
    return answer
    """
    # upon reading the problem, the input takes in a set of DISTINCT integers
    m = len(pairs)
    for i in range(m - 1):
        for j in range(i + 1, m):
            z = sorted(pairs[j].union(pairs[i]), reverse=True)
            if sum(z) == targetSum and len(z) == 4 and z not in answer:
                answer.append(z)
            
            x = {}
    return answer
    
print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))