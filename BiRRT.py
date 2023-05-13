import numpy as np
import time
from numpy.linalg import norm
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from random import random
from matplotlib import path

from node import Node
from RRT import NodeIsCollisionFree
from RRT import ClosestNode
from RRT import EdgeIsCollisionFree
from RRT import construct_path


def bidirectional_rrt_path(obstacles, xy_start, xy_goal, params):
    start_tree = [Node(xy_start, 0, 0)]  # Initialize start tree with the start node
    goal_tree = [Node(xy_goal, 0, 0)]  # Initialize goal tree with the goal node
    min_d = params.min_d  # Min distance between two nodes from the trees to connect them
    d = params.extension  # Extension parameter: this controls how far the RRT extends in each step.

    # RRT algorithm
    start_time = time.time()
    it_start_tree = 0
    it_goal_tree = 0
    sample_start_tree = 1
    print('Configuration space sampling started ...')

    while it_start_tree + it_goal_tree < params.max_it:
        # Sample configuration uniform over the C-space
        q_samp = np.array([np.random.uniform(params.world_bounds_x[0], params.world_bounds_x[1]), np.random.uniform(params.world_bounds_y[0], params.world_bounds_y[1])])

        # Check if sample is collision free, if it's not collision free -> continue with loop
        # if random() < params.start_tree_prob:
        if sample_start_tree:
            sample_start_tree = 0
            if not NodeIsCollisionFree(obstacles, q_samp):
                it_start_tree += 1
                continue

            # Find the closest node in the RRT to the sample
            closest_node = ClosestNode(start_tree, q_samp)

            # Extend the tree towards the sample
            new_node_p = closest_node.p + d * (q_samp - closest_node.p) / np.linalg.norm(q_samp - closest_node.p)
            if not EdgeIsCollisionFree(obstacles, closest_node.p, new_node_p):
                it_start_tree += 1
                continue

            # new node is added to the tree
            new_node = Node(new_node_p, len(start_tree), closest_node.id)
            start_tree.append(new_node)

            if params.animate:
                # plt.plot(xy[0], xy[1], 'ro', color='k')
                plt.plot(new_node.p[0], new_node.p[1], 'o', color='orange', markersize=3, alpha=0.8)  # VERTICES
                plt.plot([closest_node.p[0], new_node.p[0]], [closest_node.p[1], new_node.p[1]], color='orange', alpha=0.8)  # EDGES
                plt.draw()
                plt.pause(0.001)

            # Find the closest node in the goal tree to the new node
            q_goal_ast = ClosestNode(goal_tree, new_node_p)

            # Try to connect the trees
            if EdgeIsCollisionFree(obstacles, q_goal_ast.p, new_node_p) and np.linalg.norm(new_node_p - q_goal_ast.p) < min_d:
                it_start_tree += 1
                end_time = time.time()
                print('Reached the goal after %.2f seconds:' % (end_time - start_time))
                print('Number of iterations passed: %d / %d' % (it_start_tree + it_goal_tree, params.max_it))
                path_birrt = [xy_start] + construct_path(start_tree, new_node.id) + construct_path(goal_tree, q_goal_ast.id)[::-1] + [xy_goal]
                print('BiRRT length: ', len(path_birrt))
                return np.array(path_birrt)
        else:
            sample_start_tree = 1
            if not NodeIsCollisionFree(obstacles, q_samp):
                it_goal_tree += 1
                continue

            # Find the closest node in the RRT to the sample
            closest_node = ClosestNode(goal_tree, q_samp)

            # Extend the tree towards the sample
            new_node_p = closest_node.p + d * (q_samp - closest_node.p) / np.linalg.norm(q_samp - closest_node.p)
            if not EdgeIsCollisionFree(obstacles, closest_node.p, new_node_p):
                it_goal_tree += 1
                continue

            # new node is added to the tree
            new_node = Node(new_node_p, len(goal_tree), closest_node.id)
            goal_tree.append(new_node)

            if params.animate:
                # plt.plot(xy[0], xy[1], 'ro', color='k')
                plt.plot(new_node.p[0], new_node.p[1], 'o', color='blue', markersize=3, alpha=0.8)  # VERTICES
                plt.plot([closest_node.p[0], new_node.p[0]], [closest_node.p[1], new_node.p[1]], color='blue',
                         alpha=0.8)  # EDGES
                plt.draw()
                plt.pause(0.001)

            # Find the closest node in the goal tree to the new node
            q_start_ast = ClosestNode(start_tree, new_node_p)

            # Try to connect the trees
            if EdgeIsCollisionFree(obstacles, q_start_ast.p, new_node_p) and np.linalg.norm(
                    new_node_p - q_start_ast.p) < min_d:
                it_goal_tree += 1
                end_time = time.time()
                print('Reached the goal after %.2f seconds:' % (end_time - start_time))
                print('Number of iterations passed: %d / %d' % (it_start_tree + it_goal_tree, params.max_it))
                path_birrt = [xy_start] + construct_path(start_tree, q_start_ast.id) + construct_path(goal_tree,
                                                                                                   new_node.id)[
                                                                                    ::-1] + [xy_goal]
                print('BiRRT length: ', len(path_birrt))
                return np.array(path_birrt)

    print('Ran out of iterations')
    return None