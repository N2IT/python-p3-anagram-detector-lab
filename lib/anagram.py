class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        if self not in list:
            return []