user_input = int(input("ENTER YEAR TO CHECK IT IS A LEAP YEAR OR NOT\n"))

if user_input % 4 !=0:
    print("NOT A LEAP YEAR")
elif user_input %4 == 0 and user_input %100 != 0:
    print("leap year")
elif user_input % 100 == 0 and user_input % 400 == 0:
    print("leap year")
else:
    print("not leap year")