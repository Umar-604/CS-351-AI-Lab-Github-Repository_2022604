import random


def dfs(low, high, attempts):
    # AI makes a random guess within the given range
    guess = random.randint(low, high)
    print("Think of number between 1 and 100, and I (the AI) will try to guess it.")

    # Output the AI's current guess
    print(f"AI's guess is: {guess}")

    # Increment the number of attempts
    attempts += 1
    # Get feedback from the user
    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

    if feedback == 'c':
        # If correct, print the number of attempts and end the game
        print(f"I (AI) guessed the number in {attempts} attempts!")
        return
    elif feedback == 'h':
        # If guess is too high, search in the lower half
        dfs(low, guess - 1, attempts)
    elif feedback == 'l':
        # If guess is too low, search in the upper half
        dfs(guess + 1, high, attempts)


def dfs_game():
    # Initialize range and attempt count
    low = 1
    high = 100
    attempts = 0
    # Start the guessing game
    dfs(low, high, attempts)


# Run the game
dfs_game()
