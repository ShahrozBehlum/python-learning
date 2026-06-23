import random

num = random.randint(1, 10)
no_input = int(input("Enter any number (1-10): "))

if no_input == num:
    print("Thanks, correct guess!")
else:
    print("Wrong! The correct number was:", num)