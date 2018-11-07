

# State class
class State:
    def __init__(self, x, y, theta, b):
        self.x = x
        self.y = y
        self.theta = theta
        self.b = b
        self.v = 0

    def to_string(self):
        print("x = ", self.x, ", y =", self.y, ", theta =", self.theta, ", direction =", self.b, "\n")

    def apply_motion(self, arc_length, arc_radius, control):
        # calculate x, y, theta for each state through math
            # CODE HERE

        next_state = State(1, 2, 3, control)
        return next_state

    def get_distance(self, some_state):
        distance = 0
        # get distance to some state
        return distance


# Space class
class CSpace:
    def __init__(self, x_min, x_max, y_min, y_max, theta_min, theta_max, b_min, b_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.theta_min = theta_min
        self.theta_max = theta_max
        self.b_min = b_min
        self.b_max = b_max
        self.obstacles = []

    def set_obstacles(self, obstaclevect):
        self.obstacles = obstaclevect