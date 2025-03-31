#Guess the Number Game
import random
s=random.randint(1,10)
atempts=3
for i in range(atempts):
    a=int(input("Enter a number: "))
    if a==s:
        print("correct!")
    elif a>s:
        print("too high!")
    else:
        print("too low!")
print(s)


