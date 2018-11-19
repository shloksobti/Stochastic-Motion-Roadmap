from SMR_helpers.Objects import *
from SMR import *
import pickle

def make_obstacle():
    #obstacle = Obstacle(x_min, y_min, width, height)
    obstacle_1 = Obstacle(-15, -15, 1, 30) # Left boundary
    obstacle_2 = Obstacle(-15, -15, 30, 1) # Bottom boundary
    obstacle_3 = Obstacle(-15, 14, 30, 1) # Top boundary
    obstacle_4 = Obstacle(14, -15, 1, 30) # Right boundary

    obstacle_5 = Obstacle(-2, -2, 4, 4) # Center Obstacle
    obstacle_6 = Obstacle(-10, -6, 3, 7) # Random Left obstacle
    obstacle_7 = Obstacle(-5, -8, 10, 4)

    obstacles = [obstacle_1, obstacle_2, obstacle_3, obstacle_4, obstacle_5, obstacle_6, obstacle_7]
    return obstacles

#Planning for Needle
# obstacles = make_obstacle()
obstacles = make_obstacle()
# cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles)
cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles)


controlvect = [0, 1]

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

    # # Checking TP
    # for state, v in my_tp.items():
    #     for action, stt_p_dict in v.items():
    #         for stt, p in stt_p_dict.items():
    #             print("State", state.to_string(), "Action",action, "StatePrime", stt.to_string(), "Prob",p)
