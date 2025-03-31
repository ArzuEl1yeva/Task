#Find the Longest Word
def find_longest_word(words):
    return max(words, key=len)

# Example
print(find_longest_word(["apple", "banana", "cherry", "kiwi"]))  # Output: "banana"
