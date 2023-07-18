'''
gridworld/experiments/run_experiments.py

This script runs gridworld simulation experiments and collects results.

It will:

- Instantiate environments, agents, contracts
- Run multiple episodes with variations 
- Aggregate metrics on cooperation

This allows us to evaluate if introducing contracts improves
cooperation between agents.

Key steps:

- Initialize environment and agent classes
- Define experiment parameters (epochs, episodes per epoch) 
- Create rewards array to store results
- Loop through epochs:
  - Create environment and agent instances
  - Toggle contract usage on/off
  - Run specified number of episodes
  - Compute cooperation metrics
  - Append to rewards array
- Plot rewards array to visualize results  
- Perform statistical tests on cooperation with vs. without contracts
'''

import numpy as np
import matplotlib.pyplot as plt

from gridworld.envs import GridWorldEnv
from gridworld.agents import RandomAgent
from gridworld.contracts import Contract

# Experiment parameters
EPOCHS = 10
EPISODES = 100 

# Initialize environment, agent, contract classes
env = GridWorldEnv()
agent = RandomAgent(env.action_space)
contract = Contract()

# Array to store rewards
rewards = []

for epoch in range(EPOCHS):

  print(f'Epoch {epoch}')
  
  # Toggle contract usage on/off
  use_contract = epoch % 2 == 0  

  for episode in range(EPISODES):

    # Run episode
    ep_reward = 0 
    done = False

    # Initialize state
    obs = env.reset()

    while not done:

      # Agent takes action   
      action = agent.act(obs)

      # Take step in environment
      obs, reward, done, info = env.step(action)

      # Execute contract
      if use_contract:
        contract.execute_contract()

      # Accumulate rewards   
      ep_reward += reward

    # Track cooperation metrics
    cooperation = info['cooperation'] 
    rewards.append(cooperation) 

# Plot results
plt.plot(rewards)
plt.show()

# Statistical tests on effect of contracts  
print(f'Mean cooperation without contract: {np.mean(rewards[::2])}') 
print(f'Mean cooperation with contract: {np.mean(rewards[1::2])}')