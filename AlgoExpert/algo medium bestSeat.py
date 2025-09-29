#We are looking for the best seat in a theatre
#the best seat is a seat with empty an equal number of empty seats beside you

#example: [1,0,0,1,1,0,0,0,1]
#the best seat is in index 6

#example: [1,0,0,1]
#the bests seat is in index 1

def bestSeat(seats):
    best = 0
    #best counts the seats with the most zeroes
    current = 0
    #current counts the zeroes which can be replaced later on.
    ending_index = 0
    #ending_index just tells us where the consecutive zeroes end.

    for i in range(len(seats)):
        if  seats[i] == 1:
            #if current exceeds best, then we replace it and update our ending index
            if current > best:
                best = current
                ending_index = i - 1
                current = 0
            else:
                current = 0
        else:
            current += 1
    
    #this tells us that there are no best seats
    if best == 0:
        return -1
    
    #if the zeroes are even, then we divide best by 2 to get the center then subtract it from the index
    if best%2 == 0:
        return ending_index - best/2
    #if odd then we floor divide it by 2. (best/2 -1 is also applicable)
    else:
        return ending_index - best//2


assert bestSeat([1, 0, 1, 0, 0, 0, 1]) == 4
assert bestSeat([1,1,1,1]) == -1
assert bestSeat([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]) == 3