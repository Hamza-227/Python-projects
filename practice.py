import random

# Ask for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass  # ignore non-integer input

# Generate a random number between 1 and level (inclusive)
secret = random.randint(1, level)

# Ask user to guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue  # must be a positive number
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break  # exit loop on correct guess
    except ValueError:
        continue  # ignore non-integer input
