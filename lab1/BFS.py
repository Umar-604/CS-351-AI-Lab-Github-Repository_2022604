import random
from collections import deque

def bfs_game(low, high):
    attempts = 0
    queue = deque([(low, high)])  # Initialize the queue with the full range

    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")

    while queue:
        # Get the current range from the queue
        current_low, current_high = queue.popleft()
        guess = random.randint(current_low, current_high)
        print(f"AI's guess is: {guess}")

        attempts += 1
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            if current_low <= guess - 1:  # Make sure the range is valid
                queue.append((current_low, guess - 1))
        elif feedback == 'l':
            if guess + 1 <= current_high:  # Make sure the range is valid
                queue.append((guess + 1, current_high))
    print(queue)

bfs_game(1, 100)