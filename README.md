# CS450-Project-5: Planning Under Uncertainty

## Introduction
In the real world, these is a lot of uncertainty in the robot's environment, its controls, and its sensing ability. Path planning without considering these uncertainties can lead to failure. This repository implements the SMR (Stochastic Motion Planning) algorithm presented by Alterovitz et al. in the Stochastic Motion Planning paper and trains and tests for a Steering needle with motion uncertainty.

## Cloning the Repository and Installing Dependencies
To clone the repository through https:
```
git clone https://github.com/shloksobti/CS450-Project-5
```
This repository is a private repository, so contact sss10@rice.edu for access.

We have packaged our dependencies into a requirements.txt file. To install:
```
cd CS450-Project-5/Python
pip install -r requirements.txt
```

## File Structure
    .
    ├── Python                     # Python source directory where all files are
    │   ├── requirements.txt       # dependencies file
    │   ├── Needle.py              # Sets up the environment and cspace to train for the Steering Needle
    │   ├── Simulate.py            # Uses the pickle files from training to generate paths for Steering Needle
    │   ├── SMR.py                 # SMR implementation
    │   └── plotsolution.py        # etc.
    |   ├── SMR_helpers            # Contains helper functions and classes needed
    |       ├── Objects.py         # Contains State and Cspace objects needed for SMR
    └── README.md                  # Repository manual

## Usage
In order to train the algorithm and obtain a policy for the steerable needle, run the Needle.py file:
```
python Needle.py
```
Make sure to add the obstacles to the obstacle vector in Needle.py. Adjust the start and goal states, the arc length and arc radius distributions, and the number of samples (n) and number of apply motion simulations (m) in the top of SMR.py.
This will generate two pickle files that stores the transition probabilites found and the policy for the Steerable Needle.

The pickle files will be used for testing and generating paths in Simulate.py. We have sample pickle files provided. Move them into the same directory as Simulate.py before running. Run Simulate.py with the desired number of iterations, specified in the file itself:
```
python Simulate.py
```
This file will save the most recent path to path.txt. In order to visualize the path, add the obstacles to plotsolution.py and visualize with:
```
python plotsolution.py
```
This file finds a file to visualize with default name "path.txt". If the filename is different, run:
```
python plotsolution.py filename.txt
```
