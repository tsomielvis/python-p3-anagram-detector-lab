# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, word_list):
        return [word for word in word_list if sorted(word) == self.sorted_word]
