'''
def mergeOverlappingIntervals(intervals):
    
    intervals = sorted(intervals)
    finals = []
    i = 1
    x = intervals[0][0]
    y = intervals[0][1]

    while i < len(intervals):
        bounds = []

        if y < intervals[i][0]:
            bounds.append(x)
            bounds.append(y)
            finals.append(bounds)
            x = intervals[i][0]
            y = intervals[i][1]
            i += 1
                
        else:
            #y = intervals[i][1]
            i += 1
    if len(intervals) > 1 and finals == []:
        return [[intervals[0][0], intervals[-1][1]]]
    
    elif len(intervals) == 0 or len(intervals) == 1:
        return intervals
    
    
    elif x > finals[-1][1]:
        finals.append([x,y])
        
    else:
        finals[-1][1] = y
    x = intervals[0][0]
    y = intervals[0][1]
    final = []
    for i in range(1, len(intervals)):
        bound = []
        if y >= intervals[i][0]:
            continue
        else:
            bound.append(x)
            bound.append(y)
            final.append(bound)
            x = intervals[i][0]
            y = intervals[i][1]
    
    return final

            
                
    #return finals

print(mergeOverlappingIntervals([[1,2], [3,4], [5,6]]))# == [[1,2], [3,4], [5,6]]
print(mergeOverlappingIntervals([[1,2], [2,3], [2,5], [6,7]]))
print(mergeOverlappingIntervals([[1,2], [2,3], [3,8]]))

print(mergeOverlappingIntervals([
  [2, 3],
  [4, 5],
  [6, 7],
  [8, 9],
  [1, 10]
]))



def mergeOverlappingIntervals(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    ints = []
    i = 0
    current_lower = intervals[0][0]
    for j in range(1, len(intervals)):
        if intervals[i][0] + intervals[i][1] <= intervals[j][0]:
            ints.append([current_lower, intervals[j-1][1]])
            current_lower = intervals[j][0]
            i+=1
        else:
            continue
    return ints'''

def mergeOverlappingIntervals(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals = sorted(intervals)
    # print(intervals)
    ints = []
    lower_bound = intervals[0][0]
    upper_bound = intervals[0][1]

    for i in range(1, len(intervals)):
        # if upper_bound < intervals[i][0] and i == len(intervals) - 1:
        #     ints.append([lower_bound, upper_bound])
        #     lower_bound = intervals[i][0]
        #     upper_bound = intervals[i][1]

        if upper_bound < intervals[i][0]:
            ints.append([lower_bound, upper_bound])
            lower_bound = intervals[i][0]
            upper_bound = intervals[i][1]

        else:
            if upper_bound > intervals[i][1]:
                continue
            else:
                upper_bound = intervals[i][1]
 
    ints.append([lower_bound, upper_bound])
    return ints
    
    
#print(mergeOverlappingIntervals([[1,2], [3,4], [5,6]]))# == [[1,2], [3,4], [5,6]]
print(mergeOverlappingIntervals([[1,2], [2,3], [2,5], [6,7]]))
#print(mergeOverlappingIntervals([[1,2], [2,3], [3,8]]))

mergeOverlappingIntervals([
  [2, 3],
  [4, 5],
  [6, 7],
  [8, 9],
  [1, 10]
])
