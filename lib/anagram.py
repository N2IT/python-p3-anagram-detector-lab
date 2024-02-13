class Anagram:
        # breakpoint()

        def __init__(self, word):
            self.word = word
            self.word_letters = sorted([letter for letter in word])

        def match(self, word_list):
            match_word_list = []
            for word in word_list:
                if sorted([letter for letter in word]) == self.word_letters:
                    match_word_list.append(word)
            # breakpoint()
            return match_word_list
                
            # return [ word for word in word_list if sorted([letter for letter in word]) == self.word_letters ][0]





# # sort self
        # def sort_self(self):
        #     sort_word = [letter for letter in self]
        #     sort_word.sort()
        #     # set variable to new sorted, joined self
        #     self_sort = "".join(sort_word)
        #     # return value to use for comparison in match method
        #     return self_sort

        # # sort list
        # def sort_list(list):
        #     new_dict={}
        #     # iterate through sequence (list)
        #     for words in list:
        #         # iterate through letters of words in list and set new variable
        #         w_sorted = [letter for letter in words]
        #         # return sorted list of w_sorted
        #         w_sorted.sort()
        #         sorted_key = "".join(w_sorted)
        #         # create dictionary with key: values
        #         # sorted_key = key, words = values
        #         new_dict[sorted_key] = words
        #     return new_dict

        # breakpoint()

        # # compare self and list for matches
        # def match(self):
        #     # print(sort_list.keys())
        #     listed_keys = []
        #     matches = []
        #     # breakpoint()
        #     for keys in sort_list:
        #         listed_keys.append(keys)
        #         if sort_self in listed_keys:
        #             matches = sort_list[sort_self]
        #             return matches
        #         else:
        #             return []
        # match("saucey", ["wishy", "washy", "yuascey", "watch"])
# match('eopp', {'eorrtv': 'trevor', 'adny': 'andy', 'eelopp': 'people', 'eopp': 'pope', 'eopp': 'ppoe'})