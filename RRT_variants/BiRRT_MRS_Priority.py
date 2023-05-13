import numpy as np
import time
from numpy.linalg import norm
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from random import random
from matplotlib import path

from node import Node
from tree import Tree
from RRT import NodeIsCollisionFree
# from RRT import ClosestNode
from RRT import EdgeIsCollisionFree
# from RRT import construct_path


def ClosestNode(rrt, p):
    rrt_array = np.array([node.p for node in rrt])
    distances = norm(rrt_array - p, axis=1)  # calculate distances using numpy broadcasting
    ind_min = np.argmin(distances)
    closest_node = rrt[ind_min]
    return closest_node


def construct_path(rrt, i):
    path = []
    while i != 0:
        path.append(rrt[i].p)
        i = rrt[i].id_parent
    return path[::-1]

def sort_trees_by_priority(trees, priorities):
    sorted_trees = sorted(trees, key=lambda tree: getattr(tree, priorities))
    return sorted_trees


def prioritized_mrs_bidirectional_rrt_path(obstacles, xy_start, xy_goal, params, priorities):
    NoP = len(xy_start)
    start_trees = []
    goal_trees = []
    connected_nodes = np.zeros([2, NoP])
    for i in range(NoP):
        start_node = Node(xy_start[i], 0, 0)
        goal_node = Node(xy_goal[i], 0, 0)
        tree_id = i + 1
        start_trees.append(Tree(start_node, tree_id, [start_node]))  # Initialize start tree with the start nodes
        goal_trees.append(Tree(goal_node, tree_id, [goal_node]))  # Initialize goal tree with the goal nodes

        #priority assignment for trees
        if all(prior == 0 for prior in priorities):
            start_trees[i].tree_priority = tree_id
            goal_trees[i].tree_priority = tree_id
        else:
            start_trees[i].tree_priority = priorities[i]
            goal_trees[i].tree_priority = priorities[i]

    # sort the trees based on priority
    start_trees = sort_trees_by_priority(start_trees, 'tree_priority')
    goal_trees = sort_trees_by_priority(goal_trees, 'tree_priority')

    min_d = params.min_d  # Min distance between two nodes from the trees to connect them
    d = params.extension  # Extension parameter: this controls how far the RRT extends in each step.

    # RRT algorithm
    start_time = time.time()
    max_it = NoP * params.max_it
    it_start_tree = np.zeros(NoP)
    it_goal_tree = np.zeros(NoP)

    print('Configuration space sampling started ...')

    tree_pointer = NoP - 1
    active_tree_id = start_trees[tree_pointer].tree_id - 1
    while np.sum(it_start_tree) + np.sum(it_goal_tree) < max_it:
        all_trees_connected = 1
        for i in range(NoP):
            all_trees_connected = all_trees_connected * start_trees[i].trees_connected
        if not all_trees_connected:
            # Sample configuration uniform over the C-space
            q_samp = np.array([np.random.uniform(params.world_bounds_x[0], params.world_bounds_x[1]), np.random.uniform(params.world_bounds_y[0], params.world_bounds_y[1])])
            start_tree = start_trees[active_tree_id]
            goal_tree = goal_trees[active_tree_id]

            if start_tree.trees_connected:
                continue

            # Sample start tree
            if not NodeIsCollisionFree(obstacles, q_samp):
                it_start_tree[active_tree_id] += 1
                continue

            # Find the closest node in the RRT to the sample
            closest_node = ClosestNode(start_tree.tree_list, q_samp)

            # Extend the tree towards the sample
            new_node_p = closest_node.p + d * (q_samp - closest_node.p) / np.linalg.norm(q_samp - closest_node.p)
            if not EdgeIsCollisionFree(obstacles, closest_node.p, new_node_p):
                it_start_tree[active_tree_id] += 1
                continue

            # new node is added to the tree
            new_node = Node(new_node_p, len(start_tree.tree_list), closest_node.id)
            start_tree.tree_list.append(new_node)

            if params.animate:
                # plt.plot(xy[0], xy[1], 'ro', color='k')
                plt.plot(new_node.p[0], new_node.p[1], 'o', color='orange', markersize=3, alpha=0.8)  # VERTICES
                plt.plot([closest_node.p[0], new_node.p[0]], [closest_node.p[1], new_node.p[1]], color='orange', alpha=0.8)  # EDGES
                plt.draw()
                plt.pause(0.001)

            # Find the closest node in the goal tree to the new node
            q_goal_ast = ClosestNode(goal_tree.tree_list, new_node_p)

            # increase iterations by one
            it_start_tree[active_tree_id] += 1

            # Try to connect the trees
            if EdgeIsCollisionFree(obstacles, q_goal_ast.p, new_node_p) and np.linalg.norm(new_node_p - q_goal_ast.p) < min_d:
                it_start_tree[active_tree_id] += 1
                start_tree.trees_connected = 1
                goal_tree.trees_connected = 1
                tree_pointer -= 1
                active_tree_id = start_trees[tree_pointer].tree_id - 1
                connected_nodes[0][start_tree.tree_id - 1] = new_node.id
                connected_nodes[1][goal_tree.tree_id - 1] = q_goal_ast.id
                continue

            # Sample goal tree
            q_samp = np.array([np.random.uniform(params.world_bounds_x[0], params.world_bounds_x[1]), np.random.uniform(params.world_bounds_y[0], params.world_bounds_y[1])])
            if not NodeIsCollisionFree(obstacles, q_samp):
                it_goal_tree[active_tree_id] += 1
                continue

            # Find the closest node in the RRT to the sample
            closest_node = ClosestNode(goal_tree.tree_list, q_samp)

            # Extend the tree towards the sample
            new_node_p = closest_node.p + d * (q_samp - closest_node.p) / np.linalg.norm(q_samp - closest_node.p)
            if not EdgeIsCollisionFree(obstacles, closest_node.p, new_node_p):
                it_goal_tree[active_tree_id] += 1
                continue

            # new node is added to the tree
            new_node = Node(new_node_p, len(goal_tree.tree_list), closest_node.id)
            goal_tree.tree_list.append(new_node)

            if params.animate:
                # plt.plot(xy[0], xy[1], 'ro', color='k')
                plt.plot(new_node.p[0], new_node.p[1], 'o', color='blue', markersize=3, alpha=0.8)  # VERTICES
                plt.plot([closest_node.p[0], new_node.p[0]], [closest_node.p[1], new_node.p[1]], color='blue',
                         alpha=0.8)  # EDGES
                plt.draw()
                plt.pause(0.001)

            # Find the closest node in the goal tree to the new node
            q_start_ast = ClosestNode(start_tree.tree_list, new_node_p)

            # increase iterations by one
            it_goal_tree[active_tree_id] += 1

            # Try to connect the trees
            if EdgeIsCollisionFree(obstacles, q_start_ast.p, new_node_p) and np.linalg.norm(
                    new_node_p - q_start_ast.p) < min_d:
                it_goal_tree[active_tree_id] += 1
                start_tree.trees_connected = 1
                goal_tree.trees_connected = 1
                tree_pointer -= 1
                active_tree_id = start_trees[tree_pointer].tree_id - 1
                connected_nodes[1][goal_tree.tree_id - 1] = new_node.id
                connected_nodes[0][start_tree.tree_id - 1] = q_start_ast.id
                continue

        elif all_trees_connected:
            #for j in range(NoP):
                # print(start_trees[j])
                # print(goal_trees[j])
            end_time = time.time()
            print('Reached the goal after %.4f seconds:' % (end_time - start_time))
            print('Number of iterations passed: %d / %d' % (np.sum(it_start_tree) + np.sum(it_goal_tree), max_it))
            print('it_start_tree: ', it_start_tree)
            print('it_goal_tree: ', it_goal_tree)
            # paths = [np.empty((0, 2)) for _ in range(NoP)]
            paths = []
            pad_lengths = []
            max_pathlength = 0
            for i in range(NoP):
                counter = 0
                j = start_trees[i].tree_list[int(connected_nodes[0][i])].id
                while j != 0:
                    counter += 1
                    j = start_trees[i].tree_list[j].id_parent
                start_trees[i].tree_length = counter + 1
                k = goal_trees[i].tree_list[int(connected_nodes[1][i])].id
                while k != 0:
                    counter += 1
                    k = goal_trees[i].tree_list[k].id_parent
                goal_trees[i].tree_length = counter - start_trees[i].tree_length + 1
                if counter + 2 > max_pathlength:
                    max_pathlength = counter + 2
            #print(max_pathlength)
            for i in range(NoP):
                start_tree = start_trees[i]
                #print('start tree length: ', start_tree.tree_length)
                goal_tree = goal_trees[i]
                #print('goal tree length: ', goal_tree.tree_length)
                p = [start_tree.start_node.p] + construct_path(start_tree.tree_list, int(connected_nodes[0][i])) + construct_path(goal_tree.tree_list, int(connected_nodes[1][i]))[::-1] + [goal_tree.start_node.p]
                #print('Shape of p:', p)
                #print('Length of p:', len(p))
                #print('BiRRT path %d length: ' % (i+1), len(p))
                padding_length = max_pathlength - len(p)
                pad_lengths.append(padding_length)
                #print(padding_length)

                pad_value = np.array([0, 0])
                padded_p = np.pad(p, [(0, padding_length), (0, 0)], mode='constant', constant_values=pad_value)
                #paths.append(p)
                paths.append(np.array(padded_p))
            return paths, pad_lengths

    print('Ran out of iterations')
    return None