from SMR_helpers.Objects import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from SMR import *
import pickle
from Needle import *


# state = State(0,0,pi, 0)
# arc_radius = 2
# arc_length = 2*pi*arc_radius*(3/4)
# resolution = 0.0001
# control = 0
# new_state = state.apply_motion(arc_length, arc_radius, control)
#
# resolution = 0.1
# path = state.get_path(arc_radius, arc_length, control, resolution)
#
# fig = plt.figure()
# ax = fig.gca()
#
# X = [p.x for p in path]
# Y = [p.y for p in path]
#
# ax.plot(X,Y, 'ro')
# plt.show()
#

#
#
# read_dictionary = np.load('my_policy.npy').item()
# print("Start Policy: ",read_dictionary[(start.x,start.y,start.theta)])
#
# state = start
# # loop
# action = policy[(state.x, state.y, state.theta)]
# state = tp[state][action]


def plan_path(policy, tp, start_state, goal_state, cspace):
    found_path = [(start_state.x, state_state.y, start_state.theta, start_state.is_obstacle)]
    x_state = (start_state.x, state_state.y, start_state.theta, start_state.is_obstacle)  # Current State
    while x_state != (goal_state.x, goal_state.y, goal_state.theta, goal_state.is_obstacle):
        action = policy[(x_state.x, x_state.y, x_state.theta)] # Suggested Action
        stt_tp = tp[(x_state.x, x_state.y, x_state.theta, x_state.is_obstacle)][action] #{state': 0.8, state': 0.2}

        range = {}
        lower_bound = 0
        for qp,tp in stt_tp.items():
            range[(lower_bound,tp)] = qp
            lower_bound = tp

        r = random.uniform(0,1)
        for k,v in range.items():
            if k[0] < r <= k[1]:
                new_state = v

        print(new_state)
        if new_state[3]:
            print("Path Failed!!")
            return False, found_path
        else:
            x_state = new_state
            found_path.append(x_state)

    return True, found_path


if __name__ == "__main__":
    # Import Policy
    policy = {}
    with open("Policy" + '.pkl', 'rb') as f:
        policy = pickle.load(f)

    tp = {}
    with open("Transition Probabilities" + '.pkl', 'rb') as f:
        tp = pickle.load(f)

    fail_count = 0
    for i in range(100):
        print("Trial: ", i+1)
        goal_reached, found_path = plan_path(policy, start, goal, cspace)
        if not goal_reached:
            print("Trial: ", i+1, "Failed")
            fail_count += 1
