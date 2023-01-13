# PASSWORD GENERATOR
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789!@#$%^&*()~"

while 1:
    password_len = int(input("Length of your password would be? :"))
    password_count = int(input("How many password you would like to generate? :"))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Generated password: ", password)
