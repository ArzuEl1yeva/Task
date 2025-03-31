#Count Divisible Numbers
def count_divisible_numbers(lst, d):
    return sum(1 for num in lst if num % d == 0)

# Example
print(count_divisible_numbers([10, 20, 30, 40, 50], 10))  # Output: 5
print(count_divisible_numbers([15, 22, 35, 48, 50], 5))   # Output: 4
