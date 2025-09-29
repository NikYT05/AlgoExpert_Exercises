def laptopRentals(times):
    # We need to find the minimum number of laptops needed so that a student will have a laptop to use.
    # The list of times have been given.
    if times == []:
        return 0
    
    times.sort()
