'''
gridworld/__init__.py

This __init__.py file marks the gridworld directory as a Python package. 

It handles package-level imports and configuration.
'''

# Import GridWorldEnv from envs module
from gridworld.envs.gridworld_env import GridWorldEnv

# Define __version__ based on 'version' in setup.py
__version__ = '0.1' 

# Optional utility functions

def get_config():
    """Get configuration dictionary"""
    return {
        'grid_size': 5
    }