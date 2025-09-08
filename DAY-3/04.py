# Nested if statement and elif statements 


user_input = int(input("ENTER YOUR AGE \n"))

if user_input <= 12:
    
    print("you have to pay 5 dollar")

elif user_input >=13 and user_input <=17:
    
    print("you have to pay 7 dollar")

elif user_input >=18:
        
    print("you have to pay 12 dollar ")

else:
    
    print("you have to grow taller ")