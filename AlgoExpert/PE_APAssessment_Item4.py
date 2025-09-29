"""
Write a WordCounter calss that is meant to be able to count words in large texts,
so that a user of that class can quickly calculate how many times a specific word occrus in a string.

WordCounter should implement the following methods:

- process_text(text) should take in a string, text, and update the internal attributes in a thread-safe manner.
You may assume naively that text.split(" ") is good enough to return the list of words in the passed text.
- get_word_count(word) should take in a string, word, and check how many times that word has been seen, you should return 0.

note: This class must be thread-safe, meaning that many threads should be able to use the WordCounter at the same time,
and the calculations must remain accurate as id only a single thread was using the instance of WordCounter.

note: You may not use the Counter class of the collections standard library.

Example
>>> wc.WordCounter()
>>> wc.process_text("the cat is in the bag")
>>> wc.get_word_count("the")
2
>>> wc.get_word_count("bag")
1
>>> wc.get_word_acount("dog")
0
"""

import threading

class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        for word in words:
            self._increment_word_count(word)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count
    
    def _increment_word_count(self, word):
        self.lock.acquire()
        self.word_counts[word] = self.word_counts.get(word, 0) + 1
        self.lock.release()

