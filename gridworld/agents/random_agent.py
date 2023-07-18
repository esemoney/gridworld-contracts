'''
gridworld/agents/random_agent.py 

Implements a simple RandomAgent class that takes 
random actions at each timestep.

This allows quickly testing the GridWorldEnv.

Can later create agents with different goals and
policies to study emergent cooperation.
'''

import numpy as np

class RandomAgent():

    def __init__(self, action_space):
        
        self.action_space = action_space

    def act(self, observation):
        
        # Choose random action
        action = self.action_space.sample()
        
        return action