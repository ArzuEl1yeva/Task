#Anagram Group Number Finder
def find_anagram_group_number(word_list):
    anagram_groups = set()
    for word in word_list:
        sorted_word = "".join(sorted(word))
        anagram_groups.add(sorted_word)
    return len(anagram_groups)


example_words = ["listen", "silent", "enlist", "rat", "tar", "art", "cat", "tac"]
print(find_anagram_group_number(example_words))
