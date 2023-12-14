# stolen from here: https://gymnasium.farama.org/api/utils/#gymnasium.utils.save_video.save_video
import gym
import time
from gym.utils.save_video import save_video


env = gym.make("FrozenLake-v1", render_mode="rgb_array_list")
_ = env.reset()
step_starting_index = 0
episode_index = 0

for step_index in range(10): 
   action = env.action_space.sample()

   _, _, terminated, truncated, _ = env.step(action)

   obs_space = env.observation_space
   action_space = env.action_space
   print("The observation space: {}".format(obs_space[0]))
   print("The action space: {}".format(action_space))

   # save_video(
   #    env.render(),
   #    f"{time.strftime('%Y-%m-%d-%H-%M')}/videos",
   #    fps=env.metadata["render_fps"],
   #    step_starting_index=step_starting_index,
   #    episode_index=episode_index
   # )
   step_starting_index = step_index + 1
   episode_index += 1
   print(env.reset())

env.close()