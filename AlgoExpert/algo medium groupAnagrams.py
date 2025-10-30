"""
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.
"""

def groupAnagrams(words):
    list_of_groups, sorted_words = [], []
    
    # first, we needed to know the unique characters that form a corresponding word.
    for i in words:
        sorted_words.append(''.join(sorted(i)))
    
    # Hence, we get a unqiue set of words
    set_of_words = list(set(sorted_words))
    
    # Compare this set to each sorted word in the input array.
    for i in set_of_words:
        group = []
        for j in words:
            if ''.join(sorted(j)) == i:
                group.append(j)
                
        list_of_groups.append(group)
        
    return list_of_groups

# Finished in 30 minutes
print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
