import numpy as np
import random

from stolen_implementation.neural_network import NeuralNetwork

# Use this to call:
# python -m project_from_scratch.frozen_lake_environment.py

class FrozenLake():
    def __init__(self, size):
        # Left, right, up, down
        self.possible_actions = [1, 2, 3, 4]
        self.size = size
        self.frozenLakeHelper = FrozenLakeHelper()
        self.grid = self.frozenLakeHelper.generate_grid(self.size)
   
    # Returns observation/state 
    def reset(self):
        self.grid, self.player_position, self.goal_position = self.frozenLakeHelper.generate_grid(self.size)

    # Returns observation/state
    def step(self, action):
        if action not in self.possible_actions:
            return self.grid
        
        match action:
            case 1: # Going left
                # Checking if the player is at the edge
                if self.player_position[1] == 0:
                    return self.grid
            case 2: # Going right
                ""
            case 3: # Going up
                if self.player_position[0] == 0:
                    return self.grid
            case 4: # Going down
                ""

        ""

    def print_grid(self):
        # Translation from 0, 1, 2 and 3s to letters and dashes that make the print readable.
        print_grid = self.grid.astype(str)

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                match self.grid[row][column]:
                    case 0:
                        print_grid[row][column] = "-"
                    case 1:
                        print_grid[row][column] = "P"
                    case 2:
                        print_grid[row][column] = "O"
                    case 3:
                        print_grid[row][column] = "X"

        print(print_grid)


class FrozenLakeHelper():
    def __init__(self):
        ""
    
    def generate_grid(self, size):
        # Create empty grid
        grid = np.zeros((size, size), dtype=int)

        # Set player position
        player_x_position = random.randint(0, size-1)
        grid[0][player_x_position] = 1

        # Set goal position
        goal_x_position = random.randint(0, size-1)
        grid[3][goal_x_position] = 3

        for _ in range(size):
            position_not_player_or_goal = True

            while(position_not_player_or_goal):
                random_row = random.randint(0, size-1)
                random_column = random.randint(0, size-1)

                # Check if broken lake piece is on top of player or goal
                if (random_row == 0 and random_column == player_x_position or random_row == size -1 and random_column == goal_x_position):
                    continue

                # There is no check for if the environment is actually solvable
                
                position_not_player_or_goal = False

            grid[random_row, random_column] = 2
        
        # Hardcoding y for both goal and player
        return grid, (player_x_position, 0), (goal_x_position, size-1)


model = FrozenLake(4)

model.print_grid()