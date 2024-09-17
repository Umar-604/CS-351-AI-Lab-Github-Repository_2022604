import heapq  # For the priority queue implementation in A*
import random  # For random enemy placement


# Function to create the game grid and place the player, enemies, and winning line
def create_grid(size, num_enemies):
    grid = [[' ' for _ in range(size)] for _ in range(size)]  # Create an empty grid filled with spaces

    # Set the winning line on the top row
    for col in range(size):
        grid[0][col] = '-'

    winning_positions = [(0, col) for col in range(size)]

    # Place the player ('P') at the bottom center of the grid
    player_position = (size - 1, size // 2)
    grid[player_position[0]][player_position[1]] = 'P'  # 'P' marks the player position

    # Place enemies ('E') at random positions below the winning line
    enemies = []
    while len(enemies) < num_enemies:
        enemy_x, enemy_y = random.randint(1, size - 1), random.randint(0,
                                                                       size - 1)  # Enemies must be below the winning line
        if (enemy_x, enemy_y) != player_position and grid[enemy_x][enemy_y] == ' ':
            grid[enemy_x][enemy_y] = 'E'
            enemies.append((enemy_x, enemy_y))

    return grid, player_position, enemies, winning_positions


# Function to check if a position is valid (within bounds)
def is_valid_position(grid, x, y):
    size = len(grid)
    return 0 <= x < size and 0 <= y < size


# A* heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* algorithm for pathfinding
def astar(grid, start, goal):
    size = len(grid)
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {(x, y): float('inf') for x in range(size) for y in range(size)}
    g_score[start] = 0
    f_score = {(x, y): float('inf') for x in range(size) for y in range(size)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current_cost, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            next_state = (next_x, next_y)

            if is_valid_position(grid, next_x, next_y) and grid[next_x][next_y] != 'E':
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[next_state]:
                    came_from[next_state] = current
                    g_score[next_state] = tentative_g_score
                    f_score[next_state] = tentative_g_score + heuristic(next_state, goal)
                    heapq.heappush(open_set, (f_score[next_state], tentative_g_score, next_state))

    return []


# Function to print the grid with enemies', player's, and winning line's positions
def print_grid(grid):
    print("\nGrid:")
    for row in grid:
        print(' '.join(row))
    print()


# Update the grid with enemies' movements
def update_enemies(grid, enemies, player_position):
    size = len(grid)
    new_enemies = []
    for enemy in enemies:
        path = astar(grid, enemy, player_position)
        if path and len(path) > 1:
            next_position = path[1]  # Move to the next step towards the player
            # Ensure that enemies don't overlap with each other
            if grid[next_position[0]][next_position[1]] == ' ':
                grid[enemy[0]][enemy[1]] = ' '
                grid[next_position[0]][next_position[1]] = 'E'
                new_enemies.append(next_position)
            else:
                new_enemies.append(enemy)
        else:
            new_enemies.append(enemy)
    return new_enemies


# Move player in multiple directions
def move_player(grid, player_position, moves):
    direction_map = {
        'W': (-1, 0),
        'S': (1, 0),
        'A': (0, -1),
        'D': (0, 1)
    }
    for move in moves:
        if move in direction_map:
            dx, dy = direction_map[move]
            new_pos = (player_position[0] + dx, player_position[1] + dy)
            if is_valid_position(grid, new_pos[0], new_pos[1]):
                # Check if the new position is an enemy
                if grid[new_pos[0]][new_pos[1]] == 'E':
                    return player_position, True
                # Move player to the new position
                grid[player_position[0]][player_position[1]] = ' '
                player_position = new_pos
                grid[player_position[0]][player_position[1]] = 'P'
                # Check for winning condition
                if grid[player_position[0]][player_position[1]] == '-':
                    return player_position, False  # No collision, winning condition met
            else:
                print(f"Invalid move! You can't move to ({new_pos[0]}, {new_pos[1]}).")
    return player_position, False


# Main function to play the game
def maze_chase():
    size = int(input("Enter the grid size (e.g., 6 for a 6x6 grid): "))
    num_enemies = int(input(f"Enter the number of enemies (e.g., 3): "))

    # Create the grid and place the player, enemies, and winning line
    grid, player_position, enemies, winning_positions = create_grid(size, num_enemies)

    while True:
        # Print the grid
        print_grid(grid)

        # Update enemies' positions
        enemies = update_enemies(grid, enemies, player_position)

        # Check if the player has reached any position in the winning line
        if player_position in winning_positions:
            print("Congratulations! You have reached the winning line.")
            break

        # Player movement
        moves = input("Move (WASD): ").strip().upper()
        player_position, collided = move_player(grid, player_position, moves)

        if collided:
            print("Game Over! You collided with an enemy.")
            break


if __name__ == "__main__":
    maze_chase()
