from SMR_helpers.Objects import *

from collections import defaultdict
import random
from math import pi

m = 100 # number of iterations to get transition probabilities
n = 50 # number of valid samples states (50000)

# means and stdev of arc length and radius from the Paper
mu_al = 0
sig_al = 1
mu_r = 0
sig_r = 1


def initialize():
    # initialize space bounds
    cspace = CSpace(-15, 15, -15, 15, -pi/4, pi/4, 0, 1)
    start = State(0, 0, 0, 0)
    goal = State(10, 10, 0, 0)
    controlvect = [0, 1]
    return cspace, start, goal, controlvect


def sample(cspace):
    # sample n valid states from CSpace
    valid_states = [start, goal]
    idx = 0
    while idx<n:
        x = random.uniform(cspace.x_min, cspace.x_max)
        y = random.uniform(cspace.y_min, cspace.y_max)
        theta = random.uniform(cspace.theta_min, cspace.theta_max)
        b = random.choice([0,1])

        r_state = State(x,y,theta,b)

        if r_state in valid_states:
            continue
        else:
            valid_states.append(r_state)
            idx += 1
    return valid_states


def get_nearest_neighbor(valid_states, state):
    max_distance = 0
    max_idx = 0
    for idx, valid_state in enumerate(valid_states):
        distance = state.get_distance(valid_state)
        if distance > max_distance:
            max_distance = distance
            max_idx = idx

    nearest_neighbor = valid_states[max_idx]

    return nearest_neighbor


def collides(cspace, state):
    collision = False
    obstacles = cspace.obstacles
    # check whether state is in collision (whether a point / square is in a rectangular obstacle)
    return collision


def get_transition_probabilities(cspace, valid_states, controlvect):
    tp = {}  # transition probabilities table

    for state in valid_states:
        tp[state] = {}
        for control in controlvect:
            tp[state][control] = {}
            state_count = defaultdict(int)
            for idx in range(m):
                # get arc length and arc radius from gaussian dist with prespecified mean and stdev
                arc_length = random.gauss(mu_al, sig_al)
                arc_radius = random.gauss(mu_r, sig_r)
                # get the next state
                next_state = state.apply_motion(arc_length, arc_radius, control)
                nearest_state = None  # obstacle state representation
                if not collides(cspace, next_state):
                    # get the nearest neighbor in valid states to the next state
                    nearest_state = get_nearest_neighbor(valid_states, next_state)
                state_count[nearest_state] += 1
            for next_state in state_count.keys():
                tp[state][control][next_state] = state_count[next_state]/m

    return tp

def value_iteration(valid_states):

    epsilon = 0.1 #use some epsilon
    diff = [] #initialize list
    while max(diff) > epsilon:
        for idx, state in enumerate(valid_states):
            #value iteration function
            new_v =  #value formula
            diff[idx] = new_v - state.v
            state.v = new_v
    return


def get_policy():
    policy = {}
    return policy

def get_path():
    path = []
    return path

if __name__ == "__main__":
    cspace, start, goal, controlvect = initialize()
    valid_states = sample(cspace)

    tp_map = get_transition_probabilities(cspace, valid_states, controlvect)
    print(tp_map)
    #policy = get_policy()
