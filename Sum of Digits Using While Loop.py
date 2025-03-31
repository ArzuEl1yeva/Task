#Sum of Digits Using While Loop
def sum_digits_while(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Example
print(sum_digits_while(1234))  # Output: 10
print(sum_digits_while(987))   # Output: 24
