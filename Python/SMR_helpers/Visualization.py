from mpl_toolkits.mplot3d import Axes3D, art3d
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as anim
import sys
from math import sin, cos
import numpy as np


def plotObstacles(ax):
    # TODO make this our own obstacles
    ax.add_patch(patches.Polygon([(0.0, 10.0), (0.0, 8.0), (8.0, 8.0), (8.0, 10.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(2.0, 6.0), (2.0, 4.0), (10.0, 4.0), (10.0, 6.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(3.0, 4.0), (3.0, 2.0), (6.0, 2.0), (6.0, 4.0)], fill=True, color='0.20'))


def plotSE2old(path):
    fig = plt.figure()
    ax = fig.gca()
    #ax = fig.add_subplot(1, 1, 1)

    plotObstacles(ax)

    # Plotting the path (reference point)
    X = [p[0] for p in path]
    Y = [p[1] for p in path]
    ax.plot(X, Y)

    # # Plotting the actual box
    # boxVert = [[-0.15, -0.15], [0.15, -0.15], [0.15, 0.15], [-0.15, 0.15], [-0.15, -0.15]]
    #
    # for p in path:
    #     x = []
    #     y = []
    #     for v in boxVert:
    #         x.append(v[0] * cos(p[2]) - v[1] * sin(p[2]) + p[0])
    #         y.append(v[0] * sin(p[2]) + v[1] * cos(p[2]) + p[1])
    #     ax.plot(x, y, 'k')

    plt.axis([0, 10, 0, 10])

    plt.show()

def plotSE2(path):
    # X = np.linspace(0, 6 * np.pi, 100)
    # Y = np.sin(X)
    # print(X)
    # print(Y)
    # Plotting the path (reference point)
    X = [p[0] for p in path]
    Y = [p[1] for p in path]
    print(X)
    print(Y)

    print("size X: ", len(X))
    print("size Y: ", len(Y))


    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotObstacles(ax)


    line1, = ax.plot(X, Y, 'r-')  # Returns a tuple of line objects, thus the comma

    # for phase in np.linspace(0, 10 * np.pi, 500):
    #     line1.set_data(phase, np.sin(X + phase))
    #     fig.canvas.draw()
    #     fig.canvas.flush_events()
    next_state = [(2, 2), (1, 2), (3, 3), (4, 4), (3, 4), (5, 5)]*500
    for state in next_state:
        line1.set_data(state[0], state[1])
        fig.canvas.draw()
        fig.canvas.flush_events()


if __name__ == "__main__":
    path = [(0, 0), (1, 1)]
    plotSE2(path)