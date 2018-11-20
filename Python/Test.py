from SMR_helpers.Objects import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from SMR import *
import pickle
from Needle import *

# Method that writes the pathfile to external text file.
def write_to_file(pathvect):
    pathfile = open("path.txt", 'w+')
    pathfile.write("SE2 \n")
    for path in pathvect:
        pathfile.write(str(path[0]) + ' ' + str(path[1]) + ' ' + str(path[2]) + '\n')
    pathfile.close()


# Method that plans path.
def plan_path(policy, tp, start_state, goal_state, cspace):
    found_path = [(start_state.x, start_state.y, start_state.theta, start_state.is_obstacle)] # Initialized found_path
    x_state = (start_state.x, start_state.y, start_state.theta, start_state.is_obstacle)  # Current State

    while not (abs(x_state[0] - goal_state.x) < 1.0 and abs(x_state[1] - goal_state.y) < 1.0): # Runs until goal region is found
        action = policy[(x_state[0], x_state[1], x_state[2])] # Suggested Action
        stt_tp = tp[(x_state[0], x_state[1], x_state[2], x_state[3])][action] #{state': 0.8, state': 0.2}

        # Lines 27-35 simulate a probability, and based on that find the resulting state.
        range = {} # Dict mapping probability bound to resulting state. Used with random number generator.
        lower_bound = 0
        for qp, tp_ in stt_tp.items():
            range[(lower_bound, tp_+lower_bound)] = qp
            lower_bound = tp_+lower_bound
        r = random.uniform(0,1)
        for k,v in range.items():
            if k[0] < r <= k[1]:
                new_state = v # State acheived!

        if new_state[3]: # Obstacle hit!
            print("Path Failed!!")
            return False, found_path
        else:
            x_state = new_state # Update current state.
            found_path.append(x_state)
            write_to_file(found_path)
    return True, found_path


if __name__ == "__main__":
    # Import Policy
    policy = {}
    with open("Policy" + '.pkl', 'rb') as f:
        policy = pickle.load(f)

    # Import TP
    tp = {}
    with open("Transition Probabilities" + '.pkl', 'rb') as f:
        tp = pickle.load(f)

    fail_count = 0
    for i in range(100):
        print("Trial: ", i+1)
        goal_reached, found_path = plan_path(policy, tp, start, goal, cspace)
        if not goal_reached:
            print("Trial: ", i+1, "Failed")
            fail_count += 1
    print("Fail Count is: ", fail_count)
    print("Success Count is: ", 100-fail_count)
