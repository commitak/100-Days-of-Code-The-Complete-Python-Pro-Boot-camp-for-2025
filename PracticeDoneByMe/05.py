print("Welcome to the Guess Game ")

guess = 100

guess_count = 0
user_input = int(input("Guess a number: "))

while guess != user_input:

    if guess_count == 10:
        print("Out of guesses!")
        break

    elif user_input < guess:
        print("Too low! Try again.")
        guess_count +=1
    elif user_input > guess:
        print("Too high! Try again.")
        guess_count +=1
    

    user_input = int(input("Guess a number: "))

if user_input == guess:
    print("Welldone Correct Guess!")
