# Importing the relevant modules
from random import randint
from random import sample

def main():
    password_choice = input("Type 1 if you want uppercase only\n"
                            "Type 2 if you want both uppercase and lowercase\n"
                            "Type 3 if you want more symbols\n")
    length = int(input("Choose the length of your password (number only): "))
    if password_choice == "1":
        password = upper_case(length)
        print(f"\nHere is your password: {password}")
    elif password_choice == "2":
        password = upper_and_lowercase(length)
        print(f"\nHere is your password: {password}")
    elif password_choice == "3":
        password = more_symbols(length)
        print(f"\nHere is your password: {password}")
    else:
        print("That is not a valid input. ")

    # password = more_symbols(length)
    # password = upper_case(length)
    # password = upper_and_lowercase(length)



def upper_case(length):
    # All uppercase password
    password = ""
    for i in range(length):
        i = chr(randint(65, 90))
        password = str(password) + i
    return password

def upper_and_lowercase(length):
    # Upper and lowercase password
    password = ""
    for i in range(int(length / 2)):
        i = chr(randint(65, 90))
        j = chr(randint(65, 90)).lower()
        password = str(password) + i + j
    return password

def more_symbols(length):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!@#$%^&*(){}'/;:"
    upper, lower, nums, syms = True, True, True, True

    all = ""
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols


    password = "".join(sample(all, length))
    return password


if __name__ == "__main__":
    main()
