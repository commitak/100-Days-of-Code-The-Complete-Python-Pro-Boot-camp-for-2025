import random

print("Welcome to Rock, Paper, Scissors!")

user_input = input("Enter Rock or Paper or Scissors :\n").lower()

computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"Computer chose: {computer_choice}")

# tie condition
if user_input == computer_choice:
    print("It's a tie!")

# winning conditions for user
elif user_input == "rock" and computer_choice == "scissors":
    print("You win! Rock breaks Scissors.")
elif user_input == "scissors" and computer_choice == "paper":
    print("You win! Scissors cut Paper.")
elif user_input == "paper" and computer_choice == "rock":
    print("You win! Paper covers Rock.")

# otherwise, computer wins
else:
    print("Computer wins!")
