print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? \n"))

bill = 0

if height >=120:
    print("CAN RIDE")
    age = int(input("ENTER YOUR AGE :\n"))

elif age < 12 :
    bill = 5
    print("YOUR BILL IS 5")

elif age >=12 and age <=18:
    bill = 7
    print("YOUR BILL IS 7")

elif age >=18:
    bill = 12
    print("YOUR BILL IS 12")

else :
    print("CAN'T RIDE")



want_photos =input("DO YOU WANT PHOTO'S for YES Y AND FOR NO N: \n").lower()
if want_photos == 'yes':
    bill +=3
    print(f"YOUR TOTAL BILL IS {bill}")

elif want_photos == 'no' :
     print(f"YOUR TOTAL BILL IS {bill}")

