from SMR_helpers.Objects import *
from SMR import *
import pickle

def make_obstacle():
    #obstacle = Obstacle(x_min, y_min, width, height)
    obstacle_1 = Obstacle(-15, -15, 1, 30) # Left boundary
    obstacle_2 = Obstacle(-15, -15, 30, 1) # Bottom boundary
    obstacle_3 = Obstacle(-15, 14, 30, 1) # Top boundary
    obstacle_4 = Obstacle(14, -15, 1, 30) # Right boundary

    obstacle_5 = Obstacle(-4, 3, 8, 2) # Environment 2
    obstacle_6 = Obstacle(2, -2, 2, 5) # Environment 2

    obstacles = [obstacle_1, obstacle_2, obstacle_3, obstacle_4, obstacle_5, obstacle_6]
    return obstacles

#Planning for Needle
obstacles = make_obstacle() # Make Obstacles
cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles) # Generate cpace
controlvect = [0, 1] # Define Control Vector

# Actual Planning
if __name__ == "__main__":
    print("Sampling...")
    my_valid_states = sample(cspace)

    print("Building TP...")
    my_tp = get_transition_probabilities(cspace, my_valid_states, controlvect)
    tp_to_file(my_tp)

    print("Value iteration...")
    value_iteration(my_valid_states, my_tp)
    for idx, state in enumerate(my_valid_states):
        val = state.v
        print("Value of State " + str(idx+1) +":" + str(val))

    print("Extracting Policy...")
    my_policy = get_policy(my_valid_states, my_tp)
    policy_to_file(my_policy)
