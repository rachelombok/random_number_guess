#Rachel Ombok
# CS - UY 1114
# 10 Oct 2018
# Homework 4

import random

randnum = random.randint(1,100)

print("I'm thinking of a number between 1 and 100, try to guess it.")

user_num = int(input("Please enter a number between 1 and 100: "))

while user_num > 0:
    
    if user_num < randnum:
        user_num = int(input("your guess was too low, try again: "))
        
    if user_num > randnum:
        user_num = int(input("your guess was too high, try again: "))

    if type(user_num) != int:
        user_num = int(input("not a good number"))
                       
    if user_num == randnum:
        print("Congratulations, you guessed the number!")
        break
