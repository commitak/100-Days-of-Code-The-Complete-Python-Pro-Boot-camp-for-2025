print("WELCOME TO PYTHON PIZZA DELIVERIES !")

size = input("What size of pizza do you want? S for small, M for medium, L for large:\n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N:\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N:\n").lower()

bill = 0

if size == 's':
    bill = 15
elif size == 'm':
    bill = 20
elif size == 'l':
    bill = 25
else: 
    print("Invalid size!")
    exit()


if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is: ${bill}")
