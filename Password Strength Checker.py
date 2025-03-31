#Password Strength Checker
a=input("Please enter a password: ")
if len(a)<8:
    print("password is weak,must be least 8 character! ")
elif a.islower() or a.isupper():
    print("password weak,must be uppercase and lowercase letter both of them!")
elif not any(char.isdigit() for char in a):
    print("password weak,must be least one number!")
else:
    print("password strong!")
