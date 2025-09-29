# class Digit:
#     def __init__(self, number):
#         self.number = number
    
#     def __isdigit__(self):
#         if type(self.number) == type(int):
#             return True
#         else:
#             return False

def flatten_lists(func):
    flattened = []
    def wrapper(*args):
        for i in args:
            if isinstance(i, list):
                flattened.extend(i)
            else:
                flattened.append(i)

        result = func(*flattened)
        return result
    return wrapper

def convert_strings_to_ints(func):
    converted = list()
    def wrapper(*args):
        for i in args:
            if str(i).isdigit() and isinstance(i, str):
                # There lies the problem here. Initially, we tried to use i/isdigit() but it does not work. It raises a AttributeError: 'float' object has no attribute 'isdigit'.
                # The work around is to cast the digit in a string to that it can work properly.
                converted.append(int(i))
            else:
                converted.append(i)
        result = func(*converted)
        return result
    return wrapper

def filter_integers(func):
    filtered = list()
    def wrapper(*args):
        for i in args:
            if isinstance(i, int):
                filtered.append(i)
            else:
                continue
        result = func(*filtered)
        return result
    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)





print(integer_sum("1","2", -0.9, 4, [5, "hi", "3"]))
