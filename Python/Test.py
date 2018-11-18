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
if __name__ == "__main__":
    # Import Policy
    policy = {}
    with open("Policy" + '.pkl', 'rb') as f:
        policy = pickle.load(f)


    fail_count = 0
    for i in range(100):

        x_state = start # Current State
        while x_state != goal:
            arc_length = random.gauss(mu_al, sig_al)
            arc_radius = random.gauss(mu_r, sig_r)
            action = policy[(x_state.x, x_state.y, x_state.theta)]
            new_state = x_state.apply_motion(arc_lengh, arc_radius, action)
