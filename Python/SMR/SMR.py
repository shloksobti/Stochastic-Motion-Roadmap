from SMR.Objects import *
from collections import defaultdict

m = 10000

def initialize():
    # initialize space bounds
    cspace = CSpace()
    start = State()
    goal = State()
    controlvect = [0, 1]
    return cspace, start, goal, controlvect

def sample(cspace):
    # sample n valid states from CSpace
    valid_states = set()
    return valid_states

def get_nearest_neighbor(valid_states, state):
    nearest_neighbor = valid_states[0]
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



if __name__ == "main":
    cspace, start, goal, controlvect = initialize()
    valid_states = sample(cspace)
    get_transition_probabilities(cspace, valid_states, controlvect)
    policy = get_policy()