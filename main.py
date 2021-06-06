# Importing the relevant modules
from random import randint


def main():
    password = upper_case()
    print(f"Here is your password: {password}")


def upper_case():
    # All uppercase password
    password = ""
    for i in range(10):
        i = chr(randint(65, 90))
        password = str(password) + i
    return password


def upper_and_lowercase():
    # Upper and lowercase password
    password = ""
    for i in range(5):
        i = chr(randint(65, 90))
        j = chr(randint(65, 90)).lower()
        password = str(password) + i + j
    return password


if __name__ == "__main__":
    main()
