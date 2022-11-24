# Program which guessing numbers from 1 to 100 with

import random


def tring():
    try:
        return int(input("Enter your number: \n"))
    except(ValueError):
        print("Your input is not the number.")
        quit()


def bravo():
    for n in range(10):
        print(' '*n, '!')


num = random.randint(1, 100)
guess = tring()
attempt = 1
while True:
    if(guess == num):
        print("It's correct number\n HURRAAAA!!!")
        bravo()
        print("You had", attempt, "attempts")
        break
    elif(guess < num):
        print("Your number is below.")
        attempt += 1
        guess = tring()
    elif(guess > num):
        print("Your number is above.")
        attempt += 1
        guess = tring()
