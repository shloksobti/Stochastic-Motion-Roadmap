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
obstacles = make_obstacle()
cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles)
start = State(0, 0, 0, 0, 0, 0)
goal = State(10, 10, 0, 0, 0, 1)
controlvect = [0, 1]

# Actual Planning
valid_states = sample(cspace)
tp = get_transition_probabilities(cspace, valid_states, controlvect)
value_iteration(valid_states, tp)
policy = get_policy(valid_states, tp)
print (policy)
