import random
import tkinter as tk

upper = int(input("What's the upper bound?\n"))
lower = int(input("What's the lower bound?\n"))

print(f'You have 7 guesses to pick the right number between {upper} and {lower}')
number = random.randint(lower,upper)
print(number)
total_chance = 7
guess_counter = 0

while guess_counter < total_chance:
    guess_counter += 1
    guess = int(input("Take a guess"))
    if guess == number:
        print("You're correct!")
        break
    elif guess_counter >= total_chance and guess != number:
        print(f"Sorry the correct number was {number}, you're out of chances. \nTry again!")
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too Low")


