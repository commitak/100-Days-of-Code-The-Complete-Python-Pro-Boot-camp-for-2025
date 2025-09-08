feet = int(input("Enter height (feet): "))

inches = int(input("Enter remaining height (inches): "))

bill = 0

height_cm = (feet * 30.48) + (inches * 2.54)
 

if height_cm >120 :
    print("YOU CAN RIDE THE ROLLERCOASTER !")
    age = int(input("ENTER YOUR AGE \n"))

    if age <= 12 :
        bill = 5
        print("YOU HAVE TO PAY 5 DOLLAR ")
        want_photos = input("WNAT PHOTO'S WRITE Y FOR NO WRITE N : ")
        if want_photos == "Y" or want_photos == "y":
            bill += 3
            print(f"YOUR FINAL BILL WITH PHOTO'S IS {bill}")

            if age <=13 and age <=17:
                bill = 7
                print("YOU HAVE TO PAY 7 DOLLAR ")
                want_photos = input("WNAT PHOTO'S WRITE Y FOR NO WRITE N : ")
            if want_photos == 'Y' or want_photos =='y':
                print(f"YOUR FINALBILL IS WITH PHORO'S IS {bill}")

            if age >= 18:
                bill = 12
                want_photos = input("WNAT PHOTO'S WRITE Y FOR NO WRITE N :")
                if want_photos == 'Y' or want_photos == 'y':
                    print(f"YOUR FINALBILL IS WITH PHORO'S IS {bill}")

        