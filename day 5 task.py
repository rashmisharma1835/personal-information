import random


def number_guessing_game():
    # Generate a random integer between 1 and 100 inclusive
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("=" * 40)

    while True:
        user_input = input("Enter your guess: ")

        # Validate that the input is a valid integer
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid whole number.\n")
            continue

        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed the number {secret_number}!")
            print(f"It took you {attempts} attempt(s) to win.\n")
            break

if __name__ == "__main__":
    number_guessing_game()