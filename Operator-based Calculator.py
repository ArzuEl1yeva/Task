 #Operator-based Calculator
a = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if a == "+":
    result = num1 + num2
    print(num1+num2)
elif a == "-":
    print(num1-num2)
elif a == "*":
    print(num1*num2)
elif a == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1/num2)
else:
    print("Please enter one of (+, -, *, /).")