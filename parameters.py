class RRT_Params:
    def __init__(self):
        self.animate = 1  # show RRT construction, set 0 to reduce time of the RRT algorithm
        self.visualize = 1  # show constructed paths at the end of the RRT and path smoothing algorithms
        self.max_it = 5000  # max number of samples to build the RRT
        self.goal_prob = 0.05  # with probability goal_prob, sample the goal
        self.min_d_to_goal = 0.25  # [m], min distance of samples from goal to add goal node to the RRT
        self.extension = 0.2  # [m], extension parameter: this controls how far the RRT extends in each step.
        self.world_bounds_x = [-2.5, 2.5]  # [m], map size in X-direction
        self.world_bounds_y = [-2.5, 2.5]  # [m], map size in Y-direction

class BiRRT_Params:
    def __init__(self):
        self.animate = 1  # show RRT construction, set 0 to reduce time of the RRT algorithm
        self.visualize = 1  # show constructed paths at the end of the RRT and path smoothing algorithms
        self.max_it = 5000  # max number of samples to build the RRT
        self.start_tree_prob = 0.5  # with probability alt_tree_prob, sample the start tree
        self.min_d = 0.25  # [m], min distance of samples from goal to add goal node to the RRT
        self.extension = 0.2  # [m], extension parameter: this controls how far the RRT extends in each step.
        self.world_bounds_x = [-2.5, 2.5]  # [m], map size in X-direction
        self.world_bounds_y = [-2.5, 2.5]  # [m], map size in Y-direction

class BiRRT_MRS_Params:
    def __init__(self):
        self.animate = 1  # show RRT construction, set 0 to reduce time of the RRT algorithm
        self.visualize = 1  # show constructed paths at the end of the RRT and path smoothing algorithms
        self.max_it = 5000  # max number of samples to build the RRT
        self.start_tree_prob = 0.5  # with probability alt_tree_prob, sample the start tree
        self.min_d = 0.25  # [m], min distance of samples from goal to add goal node to the RRT
        self.extension = 0.2  # [m], extension parameter: this controls how far the RRT extends in each step.
        self.world_bounds_x = [-2.5, 2.5]  # [m], map size in X-direction
        self.world_bounds_y = [-2.5, 2.5]  # [m], map size in Y-direction

class Prioritized_BiRRT_MRS_Params:
    def __init__(self):
        self.animate = 0  # show RRT construction, set 0 to reduce time of the RRT algorithm
        self.visualize = 0  # show constructed paths at the end of the RRT and path smoothing algorithms
        self.max_it = 5000  # max number of samples to build the RRT
        self.start_tree_prob = 0.5  # with probability alt_tree_prob, sample the start tree
        self.min_d = 0.25  # [m], min distance of samples from goal to add goal node to the RRT
        self.extension = 0.1  # [m], extension parameter: this controls how far the RRT extends in each step.
        self.world_bounds_x = [-2.5, 2.5]  # [m], map size in X-direction
        self.world_bounds_y = [-2.5, 2.5]  # [m], map size in Y-direction

class CA_P_BiRRT_MRS_Params:
    def __init__(self):
        self.animate = 1  # show RRT construction, set 0 to reduce time of the RRT algorithm
        self.visualize = 1  # show constructed paths at the end of the RRT and path smoothing algorithms
        self.max_it = 5000  # max number of samples to build the RRT
        self.start_tree_prob = 0.5  # with probability alt_tree_prob, sample the start tree
        self.min_d = 0.25  # [m], min distance of samples from goal to add goal node to the RRT
        self.extension = 0.4  # [m], extension parameter: this controls how far the RRT extends in each step.
        self.world_bounds_x = [-2.5, 2.5]  # [m], map size in X-direction
        self.world_bounds_y = [-2.5, 2.5]  # [m], map size in Y-direction
        self.d_min = 0.1
        self.d_max = 0.4