# def longestPeak(array):
#     longest = 0
#     counter = 0
#     prev = array[0]
#     increasing = True
#     for i in range(1, len(array)):
#         if array[i] > prev and increasing == True:
#             counter += 1
#         elif array[i] < prev and increasing == True:
#             increasing == False
#             counter += 1
#         elif array[i] > prev and increasing == False:
#             counter += 1

def longestPeak(array):
    peak = 0
    peaks = []
    for i in range(len(array)):
        if i == 0 or i == len(array) - 1:
            continue
        elif array[i] > array[i+1] and array[i] > array[i-1]:
            peaks.append(i)
        else:
            continue
    
    if len(peaks) == 0:
        return 0
    
    # peaks indices correct
    

    current = 0
    for i in peaks:
        prev = array[i]
        for j in range(i, -1, -1):
            if i == j or array[j] < prev:
                #print(j, array[j], current, prev, "1st")
                current += 1
                prev = array[j]
                #print(array[j], current, prev, "1st")
            else:
               # print(j, array[j])
                break
        
        prev = array[i]
       # print(array[i:])
        for j in array[i+1:]:
            if j < prev:
                #print(j, current, prev, "2nd")
                current += 1
                prev = j
                #print(j, current, prev, "2nd")
            else:
                
                #print(j, prev, "break")
                break
        
        peak = max(current, peak)
        current = 0
        
    return peak
                
                
                    
print(longestPeak([5, 4, 3, 2, 1, 2, 1, 0]))
#print(longestPeak([-1, 0, 10, 6, 5, -1, -3, 2, 3]))

# assert longestPeak([5, 4, 3, 2, 1, 2, 1]) == 3
#assert longestPeak([-1, 0, 10, 6, 5, -1, -3, 2, 3]) == 7
