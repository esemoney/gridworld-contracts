 concept doc for v1 of the gridworld contracts project:

# Gridworld Contracts v1

Gridworld Contracts aims to evaluate if introducing simulated "smart contracts" increases emergent coordination between agents in a simple gridworld environment.

## v1 Scope

For the initial v1 prototype, the scope will be:

- Implement a basic gridworld environment based on Gymnasium/MiniGrid

- The environment will be a simple 2D grid map with spaces, walls, tokens

- There will be pre-programmed software agents with hard-coded behaviors

- Agents will have actions like move, collect tokens, propose/accept contracts

- Key parameters like grid size, number of agents, agent behaviors will be configurable

- A new "contract" action will be implemented for agents to transfer tokens. This will simulate execution of a smart contract

- Experiments will be run with and without the contract actions enabled
  
- Metrics like number of contract executions, tokens exchanged, steps to goals will be tracked

- Results with and without contracts will be analyzed to evaluate the impact on emergent coordination

## Implementation

The core code components:

- `GridWorldEnv` - Defines environment mechanics and gameplay

- `RandomAgent` - Example simple agent that takes random actions

- `Contract` - Simulates contract proposals and transfers between agents

- `run_experiments.py` - Executes simulations and collects results

Key technical choices:

- Python for implementation 

- Gymnasium for environment base class

- NumPy for computation

- Matplotlib for visualization

## Running Experiments

To run experiments:

1. Install package locally

2. Execute `run_experiments.py` 

3. Configure parameters like epochs, episodes, agents

4. Analyze plotted results and metrics

## Next Steps

For v2 and beyond, potential extensions:

- More complex gridworld mechanics and agent behaviors

- Integrate real ERC-20 smart contracts deployed to testnets

- Expanded analysis of emergent dynamics

- Study how blockchain factors like gas costs influence behaviors