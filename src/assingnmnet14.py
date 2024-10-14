import random

# Generate a random number between 1 and 20
random_number = random.randint(1, 20)
guess = None  # Initialize guess variable

# While loop to prompt user for guesses until they get it right
while guess != random_number:
    guess = int(input("Guess the number between 1 and 20: "))  # Get user input

    if guess < random_number:
        print("Your guess is too low. Try again!")
    elif guess > random_number:
        print("Your guess is too high. Try again!")
    else:
        print("Congratulations! You've guessed the correct number:", random_number)