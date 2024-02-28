import numpy as np
import random


class FrozenLake():
    def __init__(self, size):
        # Left, right, up, down
        self.possible_actions = [1, 2, 3, 4]
        self.size = size
        self.reset()
   
    # Returns observation/state 
    def reset(self):
        self.grid, self.player_position, self.goal_position = self.generate_grid()
        return self.grid

    # Returns observation/state
    def step(self, action):
        if action not in self.possible_actions:
            return self.grid, 0, False
        
        match action:
            case 1: # Going left
                # Checking if the player is at the left edge
                if self.player_position[0] == 0:
                    return self.grid, 0, False
                
                self.old_player_position = self.player_position.copy()
                self.player_position[0] = self.player_position[0] - 1

                return self.check_if_done()
            case 2: # Going right
                # Checking if the player is at the right edge
                if self.player_position[0] == self.size - 1:
                    return self.grid, 0, False
                
                self.old_player_position = self.player_position.copy()
                self.player_position[0] = self.player_position[0] + 1

                return self.check_if_done()
            case 3: # Going up
                # Checking if the player is at the top
                if self.player_position[1] == 0:
                    return self.grid, 0, False
                
                self.old_player_position = self.player_position.copy()
                self.player_position[1] = self.player_position[1] - 1

                return self.check_if_done()
            case 4: # Going down
                # Checking if the player is at the edge
                if self.player_position[1] == self.size - 1:
                    return self.grid, 0, False
                
                self.old_player_position = self.player_position.copy()
                self.player_position[1] = self.player_position[1] + 1

                return self.check_if_done()

    def check_if_done(self):
        reward = 0
        done = False
        player_icon = 1

        # Check if player has fallen through ice
        if self.grid[self.player_position[1]][self.player_position[0]] == 2:
            done = True
            reward = -1
            player_icon = 8 # For Greeks the number 8 represents death https://populscience.blogspot.com/2019/06/symbol-of-death.html
        
        # Check if player has finished
        if self.player_position == self.goal_position:
            done = True
            reward = 1
            player_icon = 111

        self.grid[self.old_player_position[1]][self.old_player_position[0]] = 0
        self.grid[self.player_position[1]][self.player_position[0]] = player_icon 
        
        return self.grid, reward, done

    def generate_grid(self):
        # Create empty grid
        grid = np.zeros((self.size, self.size), dtype=int)

        # Set player position
        player_x_position = random.randint(0, self.size-1)
        grid[0][player_x_position] = 1

        # Set goal position
        goal_x_position = random.randint(0, self.size-1)
        grid[3][goal_x_position] = 3

        # I believe something is bugged here. I had an environment with only 2 holes
        for _ in range(self.size):
            position_not_player_or_goal = True

            while(position_not_player_or_goal):
                random_row = random.randint(0, self.size-1)
                random_column = random.randint(0, self.size-1)

                # Check if broken lake piece is on top of player or goal
                if (random_row == 0 and random_column == player_x_position or random_row == self.size -1 and random_column == goal_x_position):
                    continue

                # There is no check for if the environment is actually solvable
                
                position_not_player_or_goal = False

            grid[random_row, random_column] = 2
        
        # Hardcoding y for both goal and player
        return grid, [player_x_position, 0], [goal_x_position, self.size-1]

    def print_grid(self):
        # Translation from 0, 1, 2 and 3s to letters and dashes that make the print readable.
        print_grid = self.grid.astype(str)

        # TODO: Add colours here?
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

    def print_history(self):
        "Something about saving the grid history and being able to print it?"