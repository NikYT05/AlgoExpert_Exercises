def generate_string(string, frequency):
    for i in string:
        yield i * frequency
        


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        return StringGen(self.string, self.frequency)

class StringGen():
    def __init__(self, string, freq):
        self.string = string
        self.freq = freq
        self.counter = -1 # this will detect where we are in the string

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.string):
            return self.string[self.counter] * self.freq
        else:
            raise StopIteration


for val in generate_string("dog", 3):
    print(val, end="")


for val in GenerateString("dog", 3):
    print(val, end="")

# Programming Expert Solution
# Copyright © 2022 AlgoExpert LLC. All rights reserved.

# def generate_string(string, frequency):
#     for char in string:
#         for _ in range(frequency):
#             yield char


# class GenerateString:
#     def __init__(self, string, frequency):
#         self.string = string
#         self.frequency = frequency

#     def __iter__(self):
#         self.current_char_index = 0
#         self.char_counter = 0
#         return self

#     def __next__(self):
#         if self.char_counter >= self.frequency:
#             self.char_counter = 0
#             self.current_char_index += 1

#         if self.current_char_index >= len(self.string):
#             raise StopIteration

#         self.char_counter += 1
#         return self.string[self.current_char_index]
