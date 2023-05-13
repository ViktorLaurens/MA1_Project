import numpy as np
from numpy.linalg import norm
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from random import random
from matplotlib import path
import time

# Classes to use
from node import Node

# Functions
def ClosestNode(rrt, p):
    rrt_array = np.array([node.p for node in rrt])
    distances = norm(rrt_array - p, axis=1)  # calculate distances using numpy broadcasting
    ind_min = np.argmin(distances)
    closest_node = rrt[ind_min]

    return closest_node


def NodeIsCollisionFree(obstacles, xy):
    for obstacle in obstacles:
        hull = path.Path(obstacle)
        if hull.contains_points([xy]):
            return False
    return True


def EdgeIsCollisionFree(obstacles, closest_vert, xy, map_resolution=0.01):
    closest_vert = np.array(closest_vert)
    xy = np.array(xy)
    l_line = norm(closest_vert - xy)
    n_samp = max(int(l_line / map_resolution), 3)  # number of straight-line motion samples must be at least 3.
    for i in np.linspace(0, 1, n_samp)[1:-1]:
        p = (1-i)*closest_vert + i*xy  # calculate straight-line motion sample.
        if not NodeIsCollisionFree(obstacles, p):
            return False
    return True


def rrt_path(obstacles, xy_start, xy_goal, params):
    rrt = [Node(xy_start, 0, 0)]  # Initialize RRT with the start node
    min_d_to_goal = params.min_d_to_goal  # Convergence criterion: success when the tree reaches within 0.25 in distance from the goal.
    d = params.extension  # Extension parameter: this controls how far the RRT extends in each step.

    # RRT algorithm
    start_time = time.time()
    iters = 0
    print('Configuration space sampling started ...')

    for i in range(params.max_it):
        # Sample a point
        if random() < params.goal_prob:
            xy = xy_goal
        else:
            xy = np.array([np.random.uniform(params.world_bounds_x[0], params.world_bounds_x[1]), np.random.uniform(params.world_bounds_y[0], params.world_bounds_y[1])])

        # Check if sample is collision free, if it's not collision free -> continue with loop
        if not NodeIsCollisionFree(obstacles, xy):
            iters += 1
            continue

        # Find the closest node in the RRT to the sample
        closest_node = ClosestNode(rrt, xy)

        # Extend the tree towards the sample
        new_node_p = closest_node.p + d * (xy - closest_node.p) / np.linalg.norm(xy - closest_node.p)
        if not EdgeIsCollisionFree(obstacles, closest_node.p, new_node_p):
            iters += 1
            continue

        # new node is added to the tree
        new_node = Node(new_node_p, len(rrt), closest_node.id)
        rrt.append(new_node)

        if params.animate:
            # plt.plot(xy[0], xy[1], 'ro', color='k')
            plt.plot(new_node.p[0], new_node.p[1], 'o', color='blue', markersize=3, alpha=0.8)  # VERTICES
            plt.plot([closest_node.p[0], new_node.p[0]], [closest_node.p[1], new_node.p[1]], color='blue', alpha=0.8)  # EDGES
            plt.draw()
            plt.pause(0.001)

        # Check if the goal has been reached
        if np.linalg.norm(xy_goal - new_node_p) < min_d_to_goal and EdgeIsCollisionFree(obstacles, new_node_p, xy_goal):
            goal_node = Node(xy_goal, len(rrt), new_node.id)
            rrt.append(goal_node)
            end_time = time.time()
            print('Reached the goal after %.2f seconds:' % (end_time - start_time))
            iters += 1
            print('Number of iterations passed: %d / %d' % (iters, params.max_it))
            print('RRT length: ', len(rrt))
            return np.array([xy_start] + construct_path(rrt, goal_node.id_parent) + [xy_goal])

    print('Ran out of iterations')
    return None


def construct_path(rrt, i):
    path = []
    print('Constructing the path...')
    while i != 0:
        path.append(rrt[i].p)
        i = rrt[i].id_parent
    return path[::-1]


def SmoothPath(P, obstacles, smoothiters):
    m = P.shape[0]
    l = np.zeros(m)
    for k in range(1, m):
        l[k] = norm(P[k, :] - P[k - 1, :]) + l[k - 1]  # find cumulative straight-line distances

    for _ in range(smoothiters):
        s1 = np.random.random() * l[m - 1]
        s2 = np.random.random() * l[m - 1]
        if s2 < s1:
            s1, s2 = s2, s1

        i = np.searchsorted(l, s1) - 1
        j = np.searchsorted(l, s2) - 1

        if j <= i:
            continue

        t1 = (s1 - l[i]) / (l[i + 1] - l[i])
        gamma1 = (1 - t1) * P[i, :] + t1 * P[i + 1, :]
        t2 = (s2 - l[j]) / (l[j + 1] - l[j])
        gamma2 = (1 - t2) * P[j, :] + t2 * P[j + 1, :]

        if not EdgeIsCollisionFree(obstacles, gamma1, gamma2):
            continue

        P = np.vstack([P[:(i + 1), :], gamma1, gamma2, P[(j + 1):m, :]])
        m = P.shape[0]
        l = np.zeros(m)
        l[1:] = norm(P[1:, :] - P[:-1, :], axis=1)
        l = np.cumsum(l)

    P_smooth = P
    return P_smooth