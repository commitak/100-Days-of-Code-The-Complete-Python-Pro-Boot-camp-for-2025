while True:
    first_number  = int(input("ENTER YOUR FIRST NUMBER \n"))
    operator=input("ENTER YOUR OPERATOR + - / * ** \n")
    second_number = int(input("ENTER YOUR SECOND NUMBER \n"))
    if operator =='+':
        print(first_number + second_number)
    elif operator == '-':
        print(first_number - second_number)
    elif operator == '/':
        print(first_number / second_number)
    elif operator  == '*' :
        print(first_number * second_number)
    elif operator == '**':
        print(first_number ** second_number)
    else:
        print("ENTER CORRECT OPERATOR OR INAVLID INPUT ")
        break