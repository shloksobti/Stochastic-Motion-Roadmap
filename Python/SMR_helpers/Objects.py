from math import pi, cos, sin, sqrt, inf
LEFT = 0
RIGHT = 1

# State class
class State:
    def __init__(self, x, y, theta, b, v=0, r=0, is_obstacle = False):
        self.x = x
        self.y = y
        self.theta = theta
        self.b = b
        self.v = v
        self.r = r
        self.is_obstacle = is_obstacle

    def __bounded__(self, angle):
        if angle < -pi:
            return angle + 2*pi
        if angle > pi:
            return angle - 2*pi
        else:
            return angle

    def __get_circle_angle__(self, control):
        if control == LEFT:
            return self.theta - pi/2
        if control == RIGHT:
            return self.theta + pi/2

    def __get_circle_center__(self, radius, circle_angle):
        # TODO left or right
        return (self.x - radius*cos(circle_angle), self.y - radius*sin(circle_angle))

    def __get_new_state__(self, radius, arc_angle, circle_angle, control):
        new_theta = float('NaN')
        new_x = float('NaN')
        new_y = float('NaN')
        circle_center = self.__get_circle_center__(radius, control)
        if control == LEFT:
            new_theta = self.theta + arc_angle
            new_x = radius * cos(circle_angle + arc_angle) + circle_center[0]
            new_y = radius * sin(circle_angle + arc_angle) + circle_center[1]
        if control == RIGHT:
            new_theta = self.theta - arc_angle
            new_x = radius * cos(circle_angle - arc_angle) + circle_center[0]
            new_y = radius * sin(circle_angle - arc_angle) + circle_center[1]
        return State(new_x, new_y, self.__bounded__(new_theta), control)

    def to_string(self):
        print("x = ", self.x, ", y =", self.y, ", theta =", self.theta, ", direction =", self.b, "\n")

    def apply_motion(self, arc_length, arc_radius, control):
        # calculate x, y, theta for each state through math
        arc_angle = arc_length / arc_radius
        circle_angle = self.__get_circle_angle__(control)
        return self.__get_new_state__(arc_radius, arc_angle, circle_angle, control)

    def get_distance(self, some_state):
        if self.b == some_state.b:
            M = 0
        else:
            M = inf
        distance = sqrt((self.x-some_state.x)**2 + (self.y-some_state.y)**2 + 2*(self.theta-some_state.theta)**2) + M
        return distance

    def get_path(self, arc_radius, arc_length, control, resolution):
        path = []
        range = (0, 2*pi)
        arc_angle = arc_length / arc_radius
        circle_angle = self.__get_circle_angle__(control)

        if control == LEFT:
            range = (circle_angle, circle_angle + arc_angle)
        if control == RIGHT:
            range = (circle_angle - arc_angle, circle_angle)

        t = range[0]
        while t < range[1]:
            check_state = self.__get_new_state__(arc_radius, arc_angle, circle_angle, control)
            path.append(check_state)
            t += resolution
        return path

class Obstacle:
    def __init__(self, x_min, y_min, width, height):
        self.x_min = x_min
        self.y_min = y_min
        self.width = width
        self.height = height

# Space class
class CSpace:
    def __init__(self, x_min, x_max, y_min, y_max, theta_min, theta_max, b_min, b_max, obstacles):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.theta_min = theta_min
        self.theta_max = theta_max
        self.b_min = b_min
        self.b_max = b_max
        self.obstacles = obstacles

    def set_obstacles(self, obstaclevect):
        self.obstacles = obstaclevect
