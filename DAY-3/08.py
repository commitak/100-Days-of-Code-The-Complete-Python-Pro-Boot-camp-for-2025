print("WELCOME TO PYTHON PIZZA DELIVERIES !")

size = input("What size of pizza do you want? \n S for small, M for medium, L for large:\n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N:\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N:\n").lower()

bill = 0

# Base price depending on size
if size == 's':
    bill = 15
    
elif size == 'm':
    bill = 20
   
elif size == 'l':
    bill = 25
    
else:
    print("Invalid size entered")

# Add pepperoni
if add_pepperoni == 'y' and size == 's':
    bill += 2
    print(f"Pepperoni charge +2 = {bill}")
elif add_pepperoni == 'y' and (size == 'm' or size == 'l'):
    bill += 3
    print(f"Pepperoni charge +3 = {bill}")

# Add cheese
if extra_cheese == 'y':
    bill += 1
    print(f"Extra Cheese charge +1 = {bill}")

# Final amount
print(f"YOUR FINAL BILL IS = {bill}")
