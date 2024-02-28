from frozen_lake_environment import FrozenLake
from neural_network import DQNAgent

env = FrozenLake(4)

state_size = 16 # Size of the state space (4x4 grid flattened)
action_size = 4 # Number of possible actions (left, right, up, down)
hidden_size = 64 # Size of the hidden layer in the neural network
learning_rate = 0.001
gamma = 0.99 # Discount factor for future rewards
epsilon = 1.0 # Exploration rate
epsilon_min = 0.01 # Minimum exploration rate
epsilon_decay = 0.995 # Decay rate for exploration rate
batch_size = 32 # Size of the mini-batch for experience replay

agent = DQNAgent(state_size, action_size, hidden_size, learning_rate, gamma, epsilon, epsilon_min, epsilon_decay)

num_episodes = 200
for episode in range(num_episodes):
    state = env.reset().flatten()
    done = False
    total_reward = 0

    training_iteration = 0

    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(env.possible_actions[action])
        next_state = next_state.flatten()
        total_reward += reward
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        agent.replay(batch_size)

        if training_iteration > 250:
            env.print_grid()
            training_iteration = 240

        training_iteration += 1
    
    print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

state = env.reset().flatten
done = False
while not done:
    action = agent.act(state)
    next_state, reward, done = env.step(env.possible_actions[action])
    next_state = next_state.flatten()
    state = next_state
    if done:
        env.print_grid()
        print("--------------")