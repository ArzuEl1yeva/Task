#Digits of a Three-Digit Number
def extract_digits(number):
    if 100 <= number <= 999:
        hundreds = number // 100
        tens = (number // 10) % 10
        units = number % 10
        return (hundreds, tens, units)
    else:
        raise ValueError("The number must be a three-digit integer between 100 and 999.")

# Example usage
number = 352
print(extract_digits(number))  # Output: (3, 5, 2)
