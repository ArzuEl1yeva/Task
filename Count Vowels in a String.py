#Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example
print(count_vowels("hello"))  # Output: 2 (e, o)
print(count_vowels("python")) # Output: 1 (o)
