# This is a number guessing game.
import random

quesesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print(f'Well, {myName}, I guess a number from 1 to 20.')

for quesesTaken in range(6):
    print('Try to guess.')  # Four spaces before the print function name
    quess = int(input())

    if quess < number:
        print('Your number is too low.')  # Eight spaces before the print function name

    if quess > number:
        print('Your number is too big')

    if quess == number:
        break

if quess == number:
    quesesTaken = str(quesesTaken + 1)
    print(f'Fine, {myName}! Did you manage {quesesTaken} attempts!')

if quess != number:
    number = str(number)
    print(f'Alas. I made a number {number}.')
