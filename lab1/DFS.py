import random

def dfs(low, high, attempts):

    guess = random.randint(low, high)
    print("Think of number between 1 and 100, and I (the AI) will try to guess it.")

    print(f"AI's guess is: {guess}")

    attempts += 1
    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

    if feedback == 'c':
        print(f"I (AI) guessed the number in {attempts} attempts!")
        return
    elif feedback == 'h':
        dfs(low, guess-1, attempts)
    elif feedback == 'l':
        dfs(guess+1, high, attempts)

def dfs_game():
    low = 1
    high = 100
    attempts = 0
    dfs(low, high, attempts)


dfs_game()