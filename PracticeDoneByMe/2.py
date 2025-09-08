guess = ("adventure")
guess_count = 0
max_guess = 5

while guess_count < max_guess :
    user = input("ENTER YOUR GUESS : \n")
    if user == guess:
        print("WELDONE CORRECT GUESS !")
        break
    else:
        print("SORRY You are incorrect")
        guess_count +=1
        print(f"Out of 5 guess You have gussed {guess_count} times")

if guess_count == max_guess:
    print("SORRY YOU ARE OUT OF GUESS ")
       
