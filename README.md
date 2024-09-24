# Lab 1 Task


# Task Description

**Lab 1 Task:** Implement a number guessing game where the AI uses different search algorithms to guess a number chosen by the player. The task involves utilizing various search techniques to determine the most efficient way to guess the number.

# Overview

AI Number Guessing Game is an interactive game where the AI attempts to guess a number between 1 and 100 that the player is thinking of. The game leverages a binary search algorithm to make educated guesses efficiently. The AI refines its guesses based on feedback provided by the player.

# Features

**Binary Search Algorithm:** Uses binary search to efficiently guess the number.

**Interactive Feedback:** Player provides feedback on whether the guess is too high, too low, or correct.

**Attempt Tracking:** Tracks and displays the number of attempts taken by the AI.

# Gameplay

**Start the Game:** The player thinks of a number between 1 and 100.

**AI Guessing:** The AI makes guesses using binary search and requests feedback.

**Feedback:** The player provides feedback with:

'h' if the guess is too high

'l' if the guess is too low

'c' if the guess is correct

**Winning:** The game concludes when the AI guesses the correct number and displays the number of attempts.

# Algorithm Implementations

# 1. Binary Search
**Description:** The AI uses binary search to guess the number. It divides the search range in half with each guess, adjusting the bounds based on feedback.

**Time Complexity:** O(log n)

**Implementation:** The provided script uses binary search to efficiently narrow down the possible number range.

# 2. Depth-First Search (DFS)
**Description:** DFS explores guesses as far as possible along a single path before backtracking. Though not the most efficient for this problem, it systematically explores guesses.

**Time Complexity:** O(b^d) where b is the branching factor and d is the depth.

**Implementation:** Can be adapted to guess numbers by recursively exploring each possible guess.

# 3. Breadth-First Search (BFS)
**Description:** BFS explores all possible guesses level by level. It uses a queue to track guesses and bounds.

**Time Complexity:** O(b^d) where b is the branching factor and d is the depth.

**Implementation:** Can be used to systematically explore each guess in breadth-first fashion.

# 4. Uniform Cost Search
**Description: **Expands the least-cost node first. In guessing, the "cost" could be the number of attempts.

**Time Complexity:** O(b^d) where b is the branching factor and d is the depth.

**Implementation:** Can prioritize guesses based on attempts or other cost metrics.

---

# Lab 2 Task

# Task Description

**Lab 2 Task:** Implement a grid-based strategy game where the player moves within a grid to avoid enemies and reach a winning line. The game features a player that starts at the bottom center of the grid, enemies that move towards the player, and a winning line that spans the entire top row of the grid. The player must navigate through the grid, avoid collisions with enemies, and reach the winning line to win the game.

# Game Features

**Grid-Based Movement:** Move the player around a grid using WASD controls.

**Enemies:** Enemies are placed below the winning line and move towards the player.

**Winning Line:** The top row of the grid is the winning line, which the player must reach to win the game.

**Collision Detection:** The game ends if the player collides with an enemy.

# Maze chase Game

# Overview

Maze chase is a grid-based strategy game where the player controls a character on a grid. The objective is to navigate to the top row of the grid (the winning line) while avoiding enemies that move towards the player. The game ends if the player collides with an enemy or successfully reaches the winning line.

# Features

**Grid-Based Movement:** Move the player around a grid using WASD controls.

**Enemies:** Enemies are randomly placed below the winning line and move towards the player.

**Winning Line:** The first complete row of the grid is marked with dashes (-) and serves as the winning line.

**Collision Detection:** The game ends if the player collides with an enemy.

# Gameplay

**Start Position:** The player starts at the bottom center of the grid.

**Enemies:** Enemies are randomly placed below the winning line and move towards the player.

**Winning Line:** The first complete row of the grid is marked with dashes (-) and serves as the winning line.

**Movement:** Use the W, A, S, D keys to move the player up, left, down, or right respectively.

**Objective:** Reach any position on the top row to win the game. Avoid collisions with enemies.

---

# Lab 3 Task

---

# Crossword Puzzle Solver

**Crossword Puzzle Solver** is a Python program that allows you to create and solve crossword puzzles. The program generates a grid with random blocked cells, takes a list of words from the user, and attempts to place them into the grid using a constraint propagation selection algorithm. It also visualizes word relationships using a graph.

## Task Description

Implement a crossword puzzle solver that:
- Accepts a random grid with blocked cells.
- Takes a list of words as input from the user.
- Places the words into horizontal and vertical slots in the grid, using constraint propagation for efficient word placement.
- Visualizes the relationships between words placed in the grid using a network graph.

## Game Features

- **Random Grid Generation**: A grid is randomly generated with a specified number of blocked cells.
- **Word Input**: The user provides a list of words to be placed in the crossword grid.
- **Slot Extraction**: The program automatically identifies valid horizontal and vertical word slots in the grid.
- **Constraint Propagation Selection Algorithm**: Words are placed efficiently in available slots, and intersections are maintained using a constraint propagation method.
- **Graph Visualization**: A graph visualization of the word relationships is created, showing intersections between words.

## Features Breakdown

### 1. Grid-Based Word Placement

- The grid is initialized with random blocks (`#`) and empty spaces (`-`) where words can be placed.
- Words are placed in available horizontal or vertical slots, respecting the grid constraints.

### 2. Word Slot Extraction

- The program automatically extracts available horizontal and vertical slots from the grid based on sequences of empty cells.
- Each slot is characterized by its direction (horizontal or vertical), starting position, and length.

### 3. Constraint Propagation Selection Algorithm

- **Constraint Propagation** is used to place words efficiently in the crossword.
- The algorithm checks available slots and words, applying constraints based on slot size and intersections with other words.
- Words are only placed in slots if they meet the length and intersection constraints. If no valid slot is found for a word, the program reports that no solution was found for that word.
  
This approach reduces the search space and improves the efficiency of word placement by minimizing conflicts and ensuring word intersections adhere to the crossword puzzle rules.

### 4. Graph Visualization

- A graph is created using the `networkx` library to visualize the relationships between words.
- Words that intersect in the grid are connected by edges in the graph.
- The graph is displayed using `matplotlib`.

## How It Works

### 1. Random Grid Generation

The program generates a grid of a specified size (e.g., 5x5) with random blocked cells (`#`). The number of blocked cells can be customized.

### 2. Word Input

The user is prompted to enter words, one per line. The input continues until the user provides an empty line, indicating the end of input.

### 3. Solving the Crossword Using Constraint Propagation

The program:
- Extracts word slots from the grid.
- Attempts to place each word into the grid using the constraint propagation selection algorithm.
- The algorithm ensures that words meet the size and intersection constraints for each slot.
- Updates the grid as words are placed.
- Displays the grid after each successful placement.

### 4. Visualization

After solving, the program visualizes the word relationship graph, where:
- Nodes represent words.
- Edges represent intersections between words.

## Usage

1. **Run the Program**:
    - The program starts by generating a random grid with blocked cells and displaying it.
  
2. **Input Words**:
    - Enter words you want to place in the crossword, one per line.
    - Press Enter on an empty line to finish input.

3. **View the Crossword**:
    - The program attempts to place the words in the grid using the constraint propagation algorithm.
    - After each successful word placement, the current state of the grid is displayed.

4. **View the Graph**:
    - After all words have been placed, a visual representation of the word relationships is displayed as a graph.

## Example Game Flow

1. A random 5x5 grid is generated with 10 blocked cells.
2. The user inputs a list of words.
3. The program places the words into available slots using the constraint propagation algorithm.
4. The current state of the crossword grid is printed after each successful word placement.
5. A graph of the word relationships is displayed.

## Customization

- **Grid Size**: You can modify the `rows` and `cols` variables to change the size of the grid.
- **Number of Blocked Cells**: The `num_blocks` variable controls the number of blocked cells in the grid.
- **Word List**: The user can provide a different set of words in each run.
  
---
