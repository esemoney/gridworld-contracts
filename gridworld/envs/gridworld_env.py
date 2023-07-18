'''
gridworld/envs/gridworld_env.py

This contains the GridWorldEnv class that implements the core environment 
simulation and mechanics for our gridworld game.

The key responsibilities are:

- Generating the grid map of cells
- Tracking agent and target locations
- Managing valid actions like movement
- Implementing the environment step logic
- Handling episode termination and rewards
- Supporting rendering of the grid

This encapsulates all the logic needed to simulate the gridworld game. 
The environment will be used by agents and for running experiments, so it
needs to be well-defined.


tl:dr - Contains GridWorldEnv class implementing full environment
simulation and mechanics for the gridworld game.
'''

import gymnasium as gym
import numpy as np

class GridWorldEnv(gym.Env):

  def __init__(self, size=5):

    # Grid size
    self.size = size

    # Observation space - (x,y) for agent, target
    self.observation_space = gym.spaces.Box(
      low=np.array([0,0,0,0]),
      high=np.array([self.size-1, self.size-1, self.size-1, self.size-1]),
      dtype=int
    )

    # Action space - left, right, up, down
    self.action_space = gym.spaces.Discrete(4) 

    # Keep track of agent, target locations
    self.reset()

  def reset(self):
    
    # Reset agent to random location
    self._agent_pos = self.np_random.integers(0, self.size, size=2)

    # Reset target to random location
    self._target_pos = self.np_random.integers(0, self.size, size=2)
    while np.array_equal(self._target_pos, self._agent_pos):
      self._target_pos = self.np_random.integers(0, self.size, size=2)

    # Return observation
    return self._get_obs()

  def step(self, action):
    
    # Map action to direction
    direction = self._get_direction(action)

    # Move agent in that direction
    self._agent_pos = np.clip(
      self._agent_pos + direction, 
      0, 
      self.size - 1
    )

    # Check if agent reached target
    done = np.array_equal(self._agent_pos, self._target_pos)

    # Zero reward if not done, 1 if done
    reward = 1.0 if done else 0.0

    # Return observation, reward, done, info
    return self._get_obs(), reward, done, {}
  
  def render(self):

    # Print the grid

    print('-----')
    for j in range(self.size):
      for i in range(self.size):
        if np.array_equal(self._agent_pos, [i,j]):
          print('A', end=' ') # Print A for agent
        elif np.array_equal(self._target_pos, [i,j]): 
          print('T', end=' ') # Print T for target
        else:
          print('=', end=' ') # Empty cell
      print() # Newline
    print('-----')

  def _get_obs(self):
    return np.copy(np.hstack((self._agent_pos, self._target_pos)))
  
  def _get_direction(self, action):
    # Map action (0,1,2,3) to direction vector
    if action == 0: return np.array([1, 0]) 
    elif action == 1: return np.array([0, 1])
    elif action == 2: return np.array([-1, 0])
    elif action == 3: return np.array([0, -1])

# Test resets and steps  
env = GridWorldEnv()

print(env.reset())
# [1 2 4 0] 

print(env.step(1)) 
# ([1 3 4 0], 0.0, False, {})

env.render()
# =====
# =A =
# ===T
# =====