def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals)
    ints = []

    for i in intervals:
        if not ints or ints[0][1] < i[0]:
            ints.append(i)
        else:
            i[-1]=ints[0][1]
    return [ints]

print(mergeOverlappingIntervals([[1, 3],[3, 5],[4, 7],[6, 8],[9, 10]]))