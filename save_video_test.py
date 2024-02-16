# stolen from here: https://gymnasium.farama.org/api/utils/#gymnasium.utils.save_video.save_video
import gym
import numpy as np
from neural_network import NeuralNetwork, get_device
from gym.utils.save_video import save_video
import time
import torch
from torch import nn
import torch.optim as optim





# Create the FrozenLake environment
env = gym.make('FrozenLake-v1', render_mode="rgb_array_list")

# Global Variavbles
observation_size = env.observation_space.n

# Create the neural network
model = NeuralNetwork(env)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Video stuff
step_starting_index = 0
episode_index = 0
video_folder_name = f"environment_videos/{time.strftime('%Y-%m-%d_%H-%M-%S')}/videos"

# Training variables
num_episodes = 20

for episode in range(num_episodes):
   state = env.reset()[0]
   done = False

   while not done:
      # Convert state to a tensor
      state_tensor = torch.FloatTensor(np.eye(observation_size)[state])

      # Feed environment to model and choose action based on response
      action_logits = model(state_tensor)
      action = torch.argmax(action_logits).item()

      # Take action in the environment
      next_state, reward, done, _, _ = env.step(action)

      print("next_state", next_state)
      print("reward", reward)
      print("done", done)

      # Convert next_state to a tensor
      next_state_tensor = torch.FloatTensor(np.eye(observation_size)[next_state])

      # Compute the loss
      loss = criterion(action_logits.unsqueeze(0), torch.LongTensor([action]))

      # Backpropagation
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

      state = next_state

   save_video(
      env.render(),
      video_folder_name,
      fps=env.metadata["render_fps"],
      step_starting_index=step_starting_index,
      episode_index=episode
   )
   
   step_starting_index = episode + 1
   episode_index += 1

env.close()