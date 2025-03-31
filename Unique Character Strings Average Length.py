#Unique Character Strings Average Length
def unique_char_strings_average(strings_list):
    unique_strings = [s for s in strings_list if len(s) == len(set(s))]
    if not unique_strings:
        return 0
    return sum(len(s) for s in unique_strings) / len(unique_strings)


example_list = ["apple", "orange", "abc", "hello", "world", "xyz"]
print(unique_char_strings_average(example_list))


