name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

combined_names = (name1 + name2 ).lower()



t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true_score = t + r + u + e



l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e2 = combined_names.count("e")


love_score = l + o + v + e2

score = int (str(true_score) + str(love_score))


if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
