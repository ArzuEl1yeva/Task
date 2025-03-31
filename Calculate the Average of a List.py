#Calculate the Average of a List
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

#Example
print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
