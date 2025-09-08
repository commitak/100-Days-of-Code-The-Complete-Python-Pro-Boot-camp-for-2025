# Age= int(input("ENTER YOUR AGE"))

# x = (Age * 12)

# y = (Age * 52)

# z = (Age * 365)

# print(f"You have {x} months {y} weeks {z} days lived ")


max_age = 60

user = int(input("ENTER YOUR AGE: \n"))


years_left = max_age - user

months_left = years_left * 12

Weeks_left = years_left * 52

Days_left = years_left * 365

print(f"You age is {user}.You have {months_left} months left {Weeks_left} weeks left and {Days_left} days left  ")


