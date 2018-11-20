from SMR_helpers.Objects import *

from collections import defaultdict
import random
from math import pi, sqrt, inf
import time
import numpy as np
import pickle

m = 10 # number of iterations to get transition probabilities
n = 20000 # number of valid samples states (20,000)

# means and stdev of arc length and radius from the Paper
mu_al = 0.5
sig_al = 0.2
mu_r = 2.5
sig_r = 1
start = State(-10, -10, 0, 0, 0, 0)
goal = State(10, 10, 0, 0, 1, 1)

def sample(cspace):
    # sample n valid states from CSpace
    valid_states = [start]
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
    valid_states.append(goal)
    return valid_states


def get_nearest_neighbor(valid_states, state, previous_state):
    min_distance = inf
    min_idx = None
    for idx, valid_state in enumerate(valid_states):
        if valid_state == previous_state:
            continue
        distance = state.get_distance(valid_state)
        if distance < min_distance:
            min_distance = distance
            min_idx = idx

    nearest_neighbor = valid_states[min_idx]
    return nearest_neighbor


def state_collides(cspace, state):
    obstacles = cspace.obstacles
    # check whether state is in collision (whether a point / square is in a rectangular obstacle)
    for obstacle in obstacles:
        x_min = obstacle.x_min
        x_max = obstacle.x_min + obstacle.width
        y_min = obstacle.y_min
        y_max = obstacle.y_min + obstacle.height
        if (state.x >= x_min and state.x <= x_max) and (state.y >= y_min and state.y <= y_max):
            return True
    return False


def path_collides(cspace, path):
    collision = False
    for state in path:
        if state_collides(cspace, state) and not state.is_valid_state(cspace):
            return True
    return collision


def get_transition_probabilities(cspace, valid_states, controlvect):
    tp = {}  # transition probabilities table

    for I, state in enumerate(valid_states):
        start = time.time()
        print("State: ",I+1)
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
                resolution = 0.01
                path = state.get_path(arc_radius, arc_length, control, resolution)
                if state_collides(cspace, next_state) or (not next_state.is_valid_state(cspace)) or path_collides(cspace, path):
                    next_state.is_obstacle = True
                    nearest_state = next_state
                else:
                    nearest_state = get_nearest_neighbor(valid_states, next_state, state)
                state_count[nearest_state] += 1
            for next_state in state_count.keys():
                tp[state][control][next_state] = state_count[next_state]/m
                #print("Start state: ", state.to_string())
        end = time.time()
        print("Total RunTime: ", (end-start)*1000)
    return tp


def value_iteration(valid_states, tp):
    epsilon = 0.00001 #use some epsilon
    diff = [inf] #initialize list
    while max(diff) > epsilon: # Convergence check.
        print("Max diff is:", max(diff))
        diff = []
        # print("Length of Valid States:",len(valid_states))
        for idx, state in enumerate(valid_states[0:-1]): # All valid states except goal.
            #value iteration function

            # Left control
            q_ast_left = tp[state][0].keys() #list of possible states acheived
            P_V_left = 0
            for stt in q_ast_left:
                P_V_left = P_V_left + tp[state][0][stt] * stt.v # From Bellman's equation.

            # Right Control
            q_ast_right = tp[state][1].keys()
            P_V_right = 0
            for stt in q_ast_right:
                P_V_right = P_V_right + (tp[state][1][stt] * stt.v)

            P_V = max(P_V_left, P_V_right) # Max PV for both the controls

            new_v = state.r + P_V # Bellman's Equation
            diff.append(new_v - state.v) # Update difference to check convergence

            state.v = new_v # Update value.

    return


def get_policy(valid_states, tp):
    # Extract policy from TP map
    policy = {}
    for state in valid_states:

        max_v = 0
        best_action = None
        p = 0
        for action,v in tp[state].items():
            for q_prime, prob in v.items():
                if q_prime.v >= max_v and prob > p:
                    best_action = action
                    max_v = q_prime.v
                    p = prob
        policy[state] = best_action
        # tp = {state1 : {action1: {state1' : 0.8}, action2: {state1': 0.8}}, state2: {action2: {state2': TP2}}}
    return policy

# Method that outputs TP as a pickle file.
def tp_to_file(tp):
    tp_file = {}
    for state, value in tp.items():
        tp_file[(state.x, state.y, state.theta, state.is_obstacle)] = {}
        for action, dict in value.items():
            tp_file[(state.x, state.y, state.theta, state.is_obstacle)][action] = {}
            for stt, trp in dict.items():
                tp_file[(state.x, state.y, state.theta, state.is_obstacle)][action][(stt.x, stt.y, stt.theta, stt.is_obstacle)] = trp
    with open("Transition Probabilities" + '.pkl', 'wb') as f:
        pickle.dump(tp_file, f, pickle.HIGHEST_PROTOCOL)
    return

# Method that outputs Policy as a pickle file.
def policy_to_file(policy):
    policy_file = {}
    for k,v in policy.items():
        state = (k.x,k.y,k.theta)
        action = v
        policy_file[state] = action
    with open("Policy" + '.pkl', 'wb') as f:
        pickle.dump(policy_file, f, pickle.HIGHEST_PROTOCOL)
    return
