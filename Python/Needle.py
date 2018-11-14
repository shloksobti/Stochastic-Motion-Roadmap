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
goal = State(10, 10, 0, 0, 1, 1)
controlvect = [0, 1]

# Actual Planning
valid_states = sample(cspace)
tp = get_transition_probabilities(cspace, valid_states, controlvect)
value_iteration(valid_states, tp)
# policy = get_policy(valid_states, tp)
# print (policy)
#
# state_1 = State(1,1,0,0)
# state_2 = State(9,9,0,0)
# valid_states = [start, state_1, state_2, goal]
# tp = {start: {0: {state_1: 0.2, start: 0.8}, 1:{state_1: 0.8, start: 0.2}}, state_1: {0:{start: 0.8, state_2: 0.1, state_1: 0.1}, 1:{state_2:1}}, state_2: {1:{goal:0.7, state_1: 0.3}}}
# value_iteration(valid_states, tp)
