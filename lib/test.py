class Anagram:
        def __init__(self, word):
            self.word = word
            self.list = list

        def sort_self(self):
            word_srtd = [letter for letter in self]
            word_srtd.sort()
            # set variable to new sorted, joined self
            srtd_self = "".join(word_srtd)
            return srtd_self

        def sort_list(list):
            breakpoint()
            # new_list = []
            new_dict = {}
            for words in list:
                w_sorted = [letter for letter in words]
                w_sorted.sort()
                sorted_key = "".join(w_sorted)
                new_dict = {sorted_key : words} 
           
            print(new_dict)

        def match(sort_self, sort_list):
            # breakpoint()
            if sort_self in sort_list:
                return sort_list == sort_self
            else:
                return []

# sort_list(['fuck', 'this', 'lab', 'for', 'real'])

Anagram("fuck")