import random
from collections import deque


def bfs_game(low, high):
    attempts = 0
    # Initialize the queue with the full range of possible numbers
    queue = deque([(low, high)])

    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")

    while queue:
        # Get the current range from the queue
        current_low, current_high = queue.popleft()
        # Make a random guess within the current range
        guess = random.randint(current_low, current_high)
        print(f"AI's guess is: {guess}")

        # Increment the number of attempts
        attempts += 1
        # Get feedback from the user
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            # If the guess is correct, print the number of attempts and end the game
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            # If the guess is too high, add the lower half of the range to the queue
            if current_low <= guess - 1:  # Ensure the range is valid
                queue.append((current_low, guess - 1))
        elif feedback == 'l':
            # If the guess is too low, add the upper half of the range to the queue
            if guess + 1 <= current_high:  # Ensure the range is valid
                queue.append((guess + 1, current_high))

    # Output the final state of the queue (for debugging or informational purposes)
    print(queue)


# Start the guessing game with the range from 1 to 100
bfs_game(1, 100)
