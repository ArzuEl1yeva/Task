#Count of Positive Numbers in a List
def count_positive_numbers(lst):
    return len([num for num in lst if num > 0])

# Example
print(count_positive_numbers([1, -2, 3, 0, -5, 6]))  #Output: 3