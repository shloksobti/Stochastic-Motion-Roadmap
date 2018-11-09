from SMR_helpers.Objects import *
import SMR.py

def make_obstacle():
    obstacle_1 = Obstacle(x_min, y_min, width, height)

    obstacles = [obstacle_1, obstacle_2, obstacle_3]
    return obstacles

#Planning for Needle
obstacles = make_obstacle()

cspace = CSpace(-15, 15, -15, 15, -pi, pi, 0, 1, obstacles)
start = State(0, 0, 0, 0, 0, 0)
goal = State(10, 10, 0, 0, 0, 1)
controlvect = [0, 1]
