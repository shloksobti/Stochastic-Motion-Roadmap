from SMR_helpers.Objects import *

from collections import defaultdict
import random
from math import pi, sqrt, inf

m = 100 # number of iterations to get transition probabilities
n = 50 # number of valid samples states (50000)

# means and stdev of arc length and radius from the Paper
mu_al = 0.5
sig_al = 0.2
mu_r = 2.5
sig_r = 1


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
        if state_collides(cspace, r_state): # if the state collides, don't add it
            continue
        if r_state in valid_states: # if the state is already in the list, don't add it
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


def state_collides(cspace, state):
    obstacles = cspace.obstacles
    # check whether state is in collision (whether a point / square is in a rectangular obstacle)
    for obstacle in obstacles:
        x_min = obstacle.x_min
        x_max = obstacle.x_max
        y_min = obstacle.y_min
        y_max = obstacle.y_max
        if (state.x >= x_min and state.x>=x_max) and (state.y>=y_min and state.y>=y_max):
            return True
    return False


def path_collides(cspace, path):
    collision = False
    for state in path:
        if state_collides(cspace, state):
            return True
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
                if not state_collides(cspace, next_state): # if the new state is collision free and if the path is collision free
                    # TODO path collision check
                    # get the nearest neighbor in valid states to the next state
                    nearest_state = get_nearest_neighbor(valid_states, next_state)
                state_count[nearest_state] += 1
            for next_state in state_count.keys():
                tp[state][control][next_state] = state_count[next_state]/m

    return tp


def value_iteration(valid_states, tp):

    epsilon = 0.001 #use some epsilon
    diff = [] #initialize list
    while max(diff) > epsilon:
        for idx, state in enumerate(valid_states):
            #value iteration function

            # Left control
            q_ast_left = tp[state][0].keys #list of possible states acheived
            P_V_left = 0
            for stt in q_ast_left:
                P_V_left = P_V_left + (tp[state][0][stt] * stt.v)

            # Right Control
            q_ast_right = tp[state][1].keys
            P_V_right = 0
            for stt in q_ast_right:
                P_V_right = P_V_right + (tp[state][0][stt] * stt.v)

            P_V = max(P_V_left, P_V_right) # Max PV for both the controls

            new_v = state.r + P_V
            diff[idx] = new_v - state.v
            # Exclude the goal state from updating V
            if state.r != 1:
                state.v = new_v
    return


def get_policy(valid_states, tp):
    # Extract policy from TP map
    policy = {}
    for state in valid_states:
        max_v = 0
        best_action = None
        for action,v in tp[state]:
            for q_prime, prob in v:
                if v > max_v:
                    best_action = action
                    max_v = v
        policy[state] = best_action
        # tp = {state1 : {action1: {state1' : TP1}}, state2: {action2: {state2': TP2}}}
    return policy

def simulate_path(cspace, policy):
    path = []
    return path
