import gym
import numpy as np
import random

import torch
from torch import nn
import torch.optim as optim


from stolen_implementation.neural_network import NeuralNetwork

class FrozenLake():
    def __init__(self, size):
        frozenLakeHelper = FrozenLakeHelper()
        self.grid = frozenLakeHelper.generate_grid(size)

        env = gym.make('FrozenLake-v1', render_mode="rgb_array_list")
        model = NeuralNetwork(env)

        print(nn.Parameter())
        print(model.parameters())
   
    # Returns observation/state 
    def reset(self):
        ""

    # Returns observation/state
    def step(self):
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
        player_position = random.randint(0, size-1)
        grid[0][player_position] = 1

        # Set goal position
        goal_position = random.randint(0, size-1)
        grid[3][goal_position] = 3

        for _ in range(size):
            position_not_player_or_goal = True

            while(position_not_player_or_goal):
                random_row = random.randint(0, size-1)
                random_column = random.randint(0, size-1)

                # Check if broken lake piece is on top of player or goal
                if (random_row == 0 and random_column == player_position or random_row == size -1 and random_column == goal_position):
                    continue

                # There is no check for if the problem is actually solvable
                
                position_not_player_or_goal = False

            grid[random_row, random_column] = 2
        
        return grid


model = FrozenLake(4)

model.print_grid()