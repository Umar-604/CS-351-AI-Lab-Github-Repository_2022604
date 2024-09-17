Lab 1 Task
Task Description

Lab 1 Task: Implement a number guessing game where the AI uses different search algorithms to guess a number chosen by the player. The task involves utilizing various search techniques to determine the most efficient way to guess the number.

Overview

AI Number Guessing Game is an interactive game where the AI attempts to guess a number between 1 and 100 that the player is thinking of. The game leverages a binary search algorithm to make educated guesses efficiently. The AI refines its guesses based on feedback provided by the player.

Features

Binary Search Algorithm: Uses binary search to efficiently guess the number.
Interactive Feedback: Player provides feedback on whether the guess is too high, too low, or correct.
Attempt Tracking: Tracks and displays the number of attempts taken by the AI.
Gameplay

Start the Game: The player thinks of a number between 1 and 100.
AI Guessing: The AI makes guesses using binary search and requests feedback.
Feedback: The player provides feedback with:
'h' if the guess is too high
'l' if the guess is too low
'c' if the guess is correct
Winning: The game concludes when the AI guesses the correct number and displays the number of attempts.

Algorithm Implementations

1. Binary Search
Description: The AI uses binary search to guess the number. It divides the search range in half with each guess, adjusting the bounds based on feedback.
Time Complexity: O(log n)
Implementation: The provided script uses binary search to efficiently narrow down the possible number range.
2. Depth-First Search (DFS)
Description: DFS explores guesses as far as possible along a single path before backtracking. Though not the most efficient for this problem, it systematically explores guesses.
Time Complexity: O(b^d) where b is the branching factor and d is the depth.
Implementation: Can be adapted to guess numbers by recursively exploring each possible guess.
3. Breadth-First Search (BFS)
Description: BFS explores all possible guesses level by level. It uses a queue to track guesses and bounds.
Time Complexity: O(b^d) where b is the branching factor and d is the depth.
Implementation: Can be used to systematically explore each guess in breadth-first fashion.
4. Uniform Cost Search
Description: Expands the least-cost node first. In guessing, the "cost" could be the number of attempts.
Time Complexity: O(b^d) where b is the branching factor and d is the depth.
Implementation: Can prioritize guesses based on attempts or other cost metrics.


Lab 2 Task

Task Description

Lab 2 Task: Implement a grid-based strategy game where the player moves within a grid to avoid enemies and reach a winning line. The game features a player that starts at the bottom center of the grid, enemies that move towards the player, and a winning line that spans the entire top row of the grid. The player must navigate through the grid, avoid collisions with enemies, and reach the winning line to win the game.

Game Features

Grid-Based Movement: Move the player around a grid using WASD controls.
Enemies: Enemies are placed below the winning line and move towards the player.
Winning Line: The top row of the grid is the winning line, which the player must reach to win the game.
Collision Detection: The game ends if the player collides with an enemy.
Space Shooter Game

Overview

Space Shooter is a grid-based strategy game where the player controls a character on a grid. The objective is to navigate to the top row of the grid (the winning line) while avoiding enemies that move towards the player. The game ends if the player collides with an enemy or successfully reaches the winning line.

Features

Grid-Based Movement: Move the player around a grid using WASD controls.
Enemies: Enemies are randomly placed below the winning line and move towards the player.
Winning Line: The first complete row of the grid is marked with dashes (-) and serves as the winning line.
Collision Detection: The game ends if the player collides with an enemy.
Gameplay

Start Position: The player starts at the bottom center of the grid.
Enemies: Enemies are randomly placed below the winning line and move towards the player.
Winning Line: The first complete row of the grid is marked with dashes (-) and serves as the winning line.
Movement: Use the W, A, S, D keys to move the player up, left, down, or right respectively.
Objective: Reach any position on the top row to win the game. Avoid collisions with enemies.
