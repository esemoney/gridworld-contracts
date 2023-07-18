 
'''
setup.py

This setup.py script allows us to install and distribute the gridworld-contracts 
project as a Python package.

Running `pip install -e .` in the root directory will install the package 
in editable mode, allowing us to work on the code locally.

'''

from setuptools import setup, find_packages

# Provide metadata for the package
setup(

    # Name of the package 
    name='gridworld-contracts',

    # Version number
    version='0.1',

    # List core packages required
    install_requires=[
        'gymnasium',
        'numpy'
    ],

    # Root package directory
    packages=find_packages(
        include=['gridworld', 'experiments']
    )
)