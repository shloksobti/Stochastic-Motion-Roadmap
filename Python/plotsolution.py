#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D, art3d
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
from math import sin, cos

# Draw some obstacles
def plotObstacles(ax):
    ax.add_patch(patches.Polygon([(-15.0, 15.0),(-15.0, -15.0),(-14.0, -15.0),(-14.0, 15.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(-14.0, -14.0),(-14.0, -15.0),(14.0, -15.0),(14.0, -14.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(14.0, 15.0),(14.0, -15.0),(15.0, -15.0),(15.0, 15.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(-14.0, 15.0), (-14.0, 14.0), (14.0, 14.0), (14.0, 15.0)], fill=True, color='0.20'))

    ax.add_patch(patches.Polygon([(-2.0, 2.0),(-2.0, -2.0),(2.0, -2.0),(2.0, 2.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(-10.0, 1.0),(-10.0, -6.0),(-7.0, -6.0),(-7.0, 1.0)], fill=True, color='0.20'))
    ax.add_patch(patches.Polygon([(-5.0, -4.0), (-5.0, -8.0), (5.0, -8.0), (5.0, -4.0)], fill=True, color='0.20'))

# Plot a path in R3 with a unit square obstacle centered at the origin
def plotR2(path):
    fig = plt.figure()
    ax = fig.gca()

    plotObstacles(ax)

    # Plotting the path
    X = [p[0] for p in path]
    Y = [p[1] for p in path]
    ax.plot(X, Y)

    plt.show()

def plotSE2(path):
    fig = plt.figure()
    ax = fig.gca()

    plotObstacles(ax)

    # Plotting the path (reference point)
    X = [p[0] for p in path]
    Y = [p[1] for p in path]
    ax.plot(X, Y)

    # Plotting the actual box
    boxVert = [[-0.15, -0.15], [0.15, -0.15], [0.15, 0.15], [-0.15, 0.15], [-0.15, -0.15]]

    for p in path:
        x = []
        y = []
        for v in boxVert:
            x.append(v[0] * cos(p[2]) - v[1] * sin(p[2]) + p[0])
            y.append(v[0] * sin(p[2]) + v[1] * cos(p[2]) + p[1])
        ax.plot(x, y, 'k')

    plt.axis([-15, 15, -15, 15])
    plt.show()

def plotWeird(path):
    fig = plt.figure()
    ax = fig.gca()

    # Translate configuration space path into SE(2) path
    path = [[cos(p[1]) * p[0] - 2, sin(p[1]) * p[0] - 2, p[1]] for p in path]

    plotObstacles(ax)

    # Plotting the path
    X = [p[0] for p in path]
    Y = [p[1] for p in path]
    ax.plot(X, Y)

    # Plotting the actual box
    boxVert = [[-0.15, -0.15], [0.15, -0.15], [0.15, 0.15], [-0.15, 0.15], [-0.15, -0.15]]

    for p in path:
        ax.plot((-2,p[0]), (-2,p[1]), color='b', alpha=0.2)
        x = []
        y = []
        for v in boxVert:
            x.append(v[0] * cos(p[2]) - v[1] * sin(p[2]) + p[0])
            y.append(v[0] * sin(p[2]) + v[1] * cos(p[2]) + p[1])
        ax.plot(x, y, 'k')

    plt.show()


# Read the cspace definition and the path from filename
def readPath(filename):
    lines = [line.rstrip() for line in open(filename) if len(line.rstrip()) > 0]

    if len(lines) == 0:
        print "That file's empty!"
        sys.exit(1)

    cspace = lines[0].strip()
    if (cspace != 'R2' and cspace != 'SE2' and cspace!= 'Weird'):
        print "Unknown C-space Identifier: " + cspace
        sys.exit(1)

    data = [[float(x) for x in line.split(' ')] for line in lines[1:]]
    return cspace, data

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'path.txt'

    cspace, path = readPath(filename)

    if cspace == 'R2':
        plotR2(path)
    elif cspace == 'SE2':
        plotSE2(path)
    elif cspace == 'Weird':
        plotWeird(path)
