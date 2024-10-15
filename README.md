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
  
---

# Lab 4 Task

## Titanic Dataset Analysis

**Titanic Dataset Analysis** is a Python program that explores the famous Titanic dataset to predict passenger survival based on various features. The program implements data preprocessing, visualization, and machine learning models (k-Nearest Neighbors and Decision Trees) to achieve this goal.

## Task Description

Implement an analysis workflow that:

1. Downloads the Titanic dataset from Kaggle.
2. Preprocesses the data by handling missing values and encoding categorical variables.
3. Visualizes the data distributions and relationships.
4. Trains and evaluates k-NN and Decision Tree classifiers.
5. Visualizes decision boundaries and compares model performance.

## Game Features

- **Data Exploration**: Visualizes the distribution of key features such as passenger class, age, and gender.
- **Missing Value Handling**: Automatically fills missing values and drops unnecessary columns.
- **Feature Encoding**: Converts categorical variables into numerical format for model training.
- **Machine Learning Models**: Implements k-NN and Decision Trees for predicting survival.
- **Model Evaluation**: Computes performance metrics like accuracy, precision, recall, and F1-score.
- **Visualization**: Displays decision boundaries and performance comparison charts.

## Features Breakdown

1. **Data Loading and Visualization**
   - Loads the Titanic dataset and visualizes distributions of features such as `Pclass`, `Age`, and `Sex`.

2. **Data Preprocessing**
   - Handles missing values by filling in `Age` with the median and dropping the `Cabin` column.
   - Encodes categorical features like `Sex` and `Embarked` into numerical values.

3. **Feature Standardization**
   - Standardizes numerical features (`Age` and `Fare`) to improve model performance.

4. **Machine Learning Implementation**
   - Splits the dataset into training and testing sets.
   - Trains a k-Nearest Neighbors (k-NN) classifier and a Decision Tree classifier.
   - Evaluates both models using performance metrics.

5. **Decision Boundary Visualization**
   - Visualizes decision boundaries for both models using scatter plots.
   - Displays the decision-making process of the models based on `Age` and `Fare`.

6. **Performance Comparison**
   - Compares the performance of both models using bar charts to visualize accuracy, precision, recall, and F1-score.

## How It Works

1. **Dataset Download**
   - The program uses the Kaggle API to download the Titanic dataset.

2. **Data Preprocessing**
   - It processes the dataset to handle missing values and convert categorical features into a suitable format for modeling.

3. **Model Training and Evaluation**
   - The program splits the data, trains k-NN and Decision Tree models, and evaluates their performance on the test set.

4. **Visualization**
   - After evaluation, it visualizes the decision boundaries and performance metrics, providing insights into the models' behavior.

## Usage

1. **Run the Program**:
   - Execute the notebook in Google Colab after uploading the `kaggle.json` file for authentication.

2. **Data Exploration**:
   - The program automatically displays visualizations of data distributions and missing values.

3. **Model Training**:
   - The models are trained and evaluated automatically, with results printed in the output.

4. **Visualizations**:
   - After model evaluation, various visualizations of decision boundaries and performance metrics are displayed for analysis.

## Requirements

- Python 3.x
- Libraries: Pandas, NumPy, Seaborn, Matplotlib, scikit-learn

---

Here's a detailed README file for your k-Means clustering project:

---

# Lab 6 Task
## K-Means Clustering with Visualizations

## **Overview**

This project implements a k-Means clustering algorithm from scratch using Python. It generates a synthetic dataset with three features—Age, Height, and CGPA—and clusters the data points into groups based on their similarities. The project includes step-by-step visualizations to illustrate how the algorithm works at each stage, making the clustering process easier to understand.

## **Task Description**

The task involves implementing a k-Means clustering algorithm with the following objectives:

- Generate a synthetic dataset with features: Age, Height, and CGPA.
- Standardize the dataset to ensure all features are on the same scale.
- Implement the k-Means algorithm, which includes initializing centroids, assigning data points to the closest centroids, and updating the centroids based on the mean of assigned points.
- Visualize each step of the k-Means algorithm to show how data points are clustered and centroids are updated.
- Return the final cluster assignments and centroids after convergence.

## **Key Steps**

### 1. **Data Generation**
The project generates a dataset with 150 samples and three features:
- **Age**: Random integers between 18 and 35.
- **Height**: Random integers between 150 cm and 200 cm.
- **CGPA**: Random floating-point numbers between 2.0 and 4.0.

The features are combined into a single dataset, which will be used for clustering.

### 2. **Feature Standardization**
Before applying k-Means, the features are standardized using `StandardScaler`. This ensures that all features have the same scale, preventing one feature from dominating the clustering process due to larger numerical values.

### 3. **K-Means Algorithm**
The k-Means clustering algorithm involves three main steps:
1. **Initialization**: Randomly select initial centroids from the data points.
2. **Assignment**: Assign each data point to the nearest centroid based on Euclidean distance.
3. **Update**: Update centroids by calculating the mean of all data points assigned to each centroid.

These steps are repeated until the centroids stop changing, indicating that the algorithm has converged.

### 4. **Visualization**
At each step of the k-Means process, visualizations are generated to illustrate:
- Initial placement of centroids.
- Assignment of data points to the closest centroids.
- Centroid movement as the algorithm progresses through iterations.
The visualizations help to understand how the algorithm works and how clusters are formed.

## **Features**

### **Synthetic Data Generation**
- The dataset is randomly generated with three features: Age, Height, and CGPA, simulating real-world data.

### **Feature Scaling**
- The `StandardScaler` is used to standardize the features, ensuring that they are on the same scale, which is critical for accurate distance calculations in k-Means clustering.

### **K-Means Clustering Implementation**
- The clustering process is implemented from scratch using Python. It includes the initialization of centroids, assignment of data points to clusters, and updating of centroids.

### **Step-by-Step Visualizations**
- The algorithm includes visualizations after each major step, showing:
  - Initial centroid placement.
  - Data points assigned to clusters.
  - Centroid movement during iterations.
- The visualizations provide an intuitive understanding of how the algorithm clusters data.

## **How to Run the Code**

1. **Setup the Environment**:
   - Make sure you have Python 3.x installed.
   - Install necessary libraries:
     ```bash
     pip install numpy matplotlib scikit-learn
     ```

2. **Run the k-Means Clustering Algorithm**:
   - Execute the provided Python code in a Jupyter notebook or Google Colab.
   - The code will generate a synthetic dataset and run the k-Means algorithm with visualizations at each step.

3. **View Visualizations**:
   - After running the code, you will see visualizations showing the progress of the k-Means algorithm, from the initialization of centroids to the final clustering result.

## **Expected Output**

- **Synthetic Data**: A dataset with 150 samples and three features (Age, Height, CGPA).
- **Clustering Result**: The final centroids and cluster assignments of data points after the algorithm converges.
- **Visualizations**: Step-by-step visualizations of the clustering process, including centroid initialization, data point assignments, and centroid updates.

## **Conclusion**

This project demonstrates how the k-Means algorithm works in a step-by-step manner, highlighting key stages of the process with visualizations. The project effectively showcases the use of machine learning in clustering data points based on their similarities, with a focus on how the algorithm iteratively refines cluster centers.

## **Dependencies**

- **Python 3.x**
- **NumPy**: For numerical operations.
- **Matplotlib**: For visualizing the clustering process.
- **scikit-learn**: For standardizing the dataset using `StandardScaler`.


---

