import random

# Take user input and normalize it (lowercase)
user_input = input("Choose heads or tails: \n").lower()

# Random choice
computer_choice = random.choice(["heads", "tails"])

# Check outcomes
if user_input == computer_choice:
    print("IT'S A TIE!")

elif user_input == "heads" and computer_choice == "tails":
    print("You win! (heads beats tails)")

elif user_input == "tails" and computer_choice == "heads":
    print("You win! (tails beats heads)")

else:
    print("Computer wins!")

print(f"user = {user_input}, computer = {computer_choice}")
