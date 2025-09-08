weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

bill = 0

user_age = int(input("ENTER YOUR AGE \n"))

which_day = input("ON WHICH DAY YOU WANT \n").capitalize()

glasses = input("DO YOU WANT 3D GLASSES? YES (Y) or NO (N) \n")

# ---- Base ticket price (age + day) ----
if user_age <= 12 and which_day in weekdays:
    bill = 5
elif user_age >= 13 and user_age <= 17 and which_day in weekdays:
    bill = 8
elif user_age >= 13 and user_age <= 17 and which_day in weekend:
    bill = 8 + 3   # weekend extra
elif user_age >= 18 and user_age <= 59 and which_day in weekdays:
    bill = 12
elif user_age >= 18 and user_age <= 59 and which_day in weekend:
    bill = 12 + 3
else:
    bill = 6   # fallback price

# ---- Add glasses if chosen ----
if glasses == 'Y' or glasses == 'y':
    bill += 3

# ---- Print total ----
print(f"YOUR TOTAL BILL IS ${bill}")
