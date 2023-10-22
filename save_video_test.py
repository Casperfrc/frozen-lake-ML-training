# stolen from here: https://gymnasium.farama.org/api/utils/#gymnasium.utils.save_video.save_video
import gym
import time
from gym.utils.save_video import save_video


env = gym.make("FrozenLake-v1", render_mode="rgb_array_list")
_ = env.reset()
step_starting_index = 0
episode_index = 0

for step_index in range(199): 
   action = env.action_space.sample()
   _, _, terminated, truncated, _ = env.step(action)

   if terminated or truncated:
      save_video(
         env.render(),
         f"{time.strftime("%Y-%m-%d-%H-%M")}/videos",
         fps=env.metadata["render_fps"],
         step_starting_index=step_starting_index,
         episode_index=episode_index
      )
      step_starting_index = step_index + 1
      episode_index += 1
      env.reset()

env.close()