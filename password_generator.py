import random

chars = "abcdefghijklmnopqrstuvwxyzABDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"

pass_length=int(input("enter length of password:"))
password=""
for i in range(1,pass_length+1):
    password+=random.choice(chars)

print(password)

