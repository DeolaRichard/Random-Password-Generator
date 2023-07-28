# ask if user wants to get random password
# if yes, ask how long the password should
# generate the password
# print the password

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&()^")

def generate_password():
    password_length = int(input("How long do you want your password to be? "))

    random.shuffle(characters)

