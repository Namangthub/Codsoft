import random

def operation(user_input):
    global password
    
    for x in range(user_input):
        l = random.randint(0,3)
        if l == 0:
            w = random.randint(0,25)
            password = password + upper_case[w]
        elif l == 1:
            x = random.randint(0,25)
            password = password + lower_case[x]
        elif l == 2:
            y = random.randint(0,9)
            password = password + number[y]
        else:
            z = random.randint(0,11)
            password = password + symbols[z]
        
    print("Generated password is : " + password)

def main():
    global password , upper_case , lower_case , number , symbols
        
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case = list(upper_case)

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    lower_case = list(lower_case)

    number = "0123456789"
    number = list(number)

    symbols = "-1@#&^*()$_!"
    symbols = list(symbols)

    password = ""

    user_input = int(input("Enter the lenght of the password : " )) 

    operation(user_input)

main()