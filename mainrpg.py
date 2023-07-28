# ask if user wants to get random password
# if yes, ask how long the password should
# generate the password
# print the password
# if answer at line 2 is no, exit the program.

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&()^")


def generate_password():
    password_length = int(input("How long do you want your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        print(password)
