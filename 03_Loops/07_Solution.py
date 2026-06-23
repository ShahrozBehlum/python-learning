<<<<<<< HEAD
import random

num = random.randint(1, 10)
no_input = int(input("Enter any number (1-10): "))

if no_input == num:
    print("Thanks, correct guess!")
else:
=======
import random

num = random.randint(1, 10)
no_input = int(input("Enter any number (1-10): "))

if no_input == num:
    print("Thanks, correct guess!")
else:
>>>>>>> 8e7f2e321fefce9d5ac2b428313771f58418cce2
    print("Wrong! The correct number was:", num)