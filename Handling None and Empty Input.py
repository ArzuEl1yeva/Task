#Handling None and Empty Input
a=input("Enter a value:")
if not a:
    value=None
    print("Not input provided")
else:
    value=a
    print((a),type(a))