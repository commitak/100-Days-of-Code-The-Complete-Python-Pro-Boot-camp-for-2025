weight = int(input("ENTER YOUR WEIGHT BELOW \n"))

height = float(input("ENTER YOU HEIGHT IN METER BELOW \n"))

BMI = round(weight / height ** 2)

print(BMI)




if  BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 and BMI <25:
    print("they have a normal weight")
elif BMI >= 25 and BMI < 30:
    print("they are overweight")
elif BMI > 30 and BMI < 35:
    print("they are obse")
elif BMI > 35:
    print("they are clinically obese")