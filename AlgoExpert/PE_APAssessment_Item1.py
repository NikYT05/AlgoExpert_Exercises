# The function should take in as many arguments
# the function should return a list containing only a list of squares of even positive integers.

def positive_even_squares(*args):
    new_lst = list()
    for i in list(args):
        filtered = filter(lambda x: x > 0, i)
        filtered = filter(lambda x: x % 2 == 0, filtered)
        new_lst.append(list(filtered))
        
    int_lst = list()
    for i in new_lst:
        for j in i:
            int_lst.append(j)

    int_lst = map(lambda x : x**2, int_lst)

    return list(int_lst)


