#Rock-Paper-Scissors Game
choices = ["rock", "paper", "scissors"]

a = input("Player 1, enter your choice (rock, paper, scissors): ")
b = input("Player 2, enter your choice (rock, paper, scissors): ")

if a not in choices or b not in choices:
    print("Invalid input")
elif a == b:
    print("It's a tie!")
elif (a == "rock" and b == "scissors") or \
     (a == "scissors" and b == "paper") or \
     (a == "paper" and b == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

