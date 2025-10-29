def minimumCharactersForWords(words):
    # create a dictionary to set key-value pairs of a character and its frequency
    freq = {}
    for i in words:
        for char in i:
            if char not in freq:
                freq[char] = i.count(char)
            
            if freq[char] < i.count(char):
                freq[char] = i.count(char)
             
    chars = []
    for key, value in freq.items():
        for i in range(value):
            chars.append(key)
    return chars


print(minimumCharactersForWords(['hello', 'heh']))