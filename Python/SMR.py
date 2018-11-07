from SMR_helpers.Objects import *

from collections import defaultdict
import random
from math import pi

m = 100 # number of iterations to get transition probabilities
n = 50 # number of valid samples states (50000)


def initialize():
    # initialize space bounds
    cspace = CSpace(-15, 15, -15, 15, -pi/4, pi/4, 0, 1)
    start = State(0, 0, 0, 0)
    goal = State(10, 10, 0, 0)
    controlvect = [0, 1]
    return cspace, start, goal, controlvect


def sample(cspace):
    # sample n valid states from CSpace
    valid_states = set()
    for i in range(n):
        x = random.uniform(cspace.x_min, cspace.x_max)
        y = random.uniform(cspace.y_min, cspace.y_max)
        theta = random.uniform(cspace.theta_min, cspace.theta_max)
        b = random.choice([0,1])

        r_state = State(x,y,theta,b)
        valid_states.add(r_state)
    print(valid_states)
    return valid_states


def get_nearest_neighbor(valid_states, state):
    max_distance = 0
    max_idx = 0
    for idx, state in enumerate(valid_states):
        #insert equation
        result = 1+2
        if result > max_distance:
            max_distance = result
            max_idx = idx

    nearest_neighbor = valid_states[max_idx]
    return nearest_neighbor


def get_transition_probabilities(cspace, valid_states, controlvect):
    tp = {}
    # initialize tp dict

    for state in valid_states:
        tp[state] = {}
        for control in controlvect:
            tp[state][control] = {}
            state_count = defaultdict(int)
            for idx in range(m):
                # get arc length and arc radius from gaussian dist with prespecified mean and stdev
                arc_length = 0.3
                arc_radius = 2
                next_state = state.applymotion(arc_length, arc_radius, control)
                nearest_state = get_nearest_neighbor(valid_states, next_state)
                state_count[nearest_state] += 1
            for next_state in state_count.keys():
                tp[state][control][next_state] = state_count[next_state]/m

    return tp


def get_policy():
    policy = {}
    return policy



if __name__ == "__main__":
    cspace, start, goal, controlvect = initialize()
    valid_states = sample(cspace)

    #get_transition_probabilities(cspace, valid_states, controlvect)
    #policy = get_policy()