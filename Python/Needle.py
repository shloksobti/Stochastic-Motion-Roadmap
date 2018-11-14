from SMR_helpers.Objects import *
from SMR import *

def make_obstacle():
    #obstacle = Obstacle(x_min, y_min, width, height)
    obstacle_1 = Obstacle(-15, -15, 1, 30) #Left boundary
    obstacle_2 = Obstacle(-15, -15, 30, 1) #Bottom boundary
    obstacle_3 = Obstacle(-15, 14, 30, 1) #Top boundary
    obstacle_4 = Obstacle(14, -15, 1, 30) #Right boundary
    #obstacle_5 = Obstacle(-2, -2, 4, 4)

    obstacles = [obstacle_1, obstacle_2, obstacle_3, obstacle_4]
    return obstacles

#Planning for Needle
# obstacles = make_obstacle()
obstacles = []
# cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles)
cspace = CSpace(-1, 1, -1, 1, -pi, pi, 0, 1, obstacles)
start = State(0, 0, 0, 0, 0, 0)
# goal = State(10, 10, 0, 0, 1, 1)
goal = State(0.5, 0.5, 0, 0, 1, 1)

controlvect = [0, 1]

# Actual Planning
my_valid_states = sample(cspace)
my_tp = get_transition_probabilities(cspace, my_valid_states, controlvect)

for state, v in my_tp.items():
    for action, stt_p_dict in v.items():
        for stt, p in stt_p_dict.items():
            print("State", state.to_string(), "Action",action, "StatePrime", stt.to_string(), "Prob",p)


# value_iteration(my_valid_states, my_tp)
# policy = get_policy(valid_states, tp)
# print (policy)
