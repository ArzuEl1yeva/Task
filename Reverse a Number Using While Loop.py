#Reverse a Number Using While Loop
def reverse_number(n):

    return int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
#Example
print(reverse_number(1234))   # Output: 4321
print(reverse_number(-9876))  # Output: -6789
