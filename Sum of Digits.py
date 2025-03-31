#Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example
print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(987))   # Output: 24
