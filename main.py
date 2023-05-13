import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

# Classes to use
from parameters import RRT_Params
from parameters import BiRRT_Params
from parameters import BiRRT_MRS_Params
from parameters import Prioritized_BiRRT_MRS_Params
from parameters import CA_P_BiRRT_MRS_Params

# Functions to use
from RRT import rrt_path
from BiRRT import bidirectional_rrt_path
from BiRRT_MRS import mrs_bidirectional_rrt_path
from BiRRT_MRS_Priority import prioritized_mrs_bidirectional_rrt_path
from BiRRT_MRS_P_DE import de_p_mrs_bidirectional_rrt_path
from RRT import SmoothPath


def draw_map(obstacles, params):
    # Draw obstacles
    fig = plt.figure(figsize=(5, 5))
    # plt.grid()
    plt.xlabel('x position [m]')
    plt.ylabel('y position [m]')
    ax = plt.gca()
    ax.set_xlim(params.world_bounds_x)
    ax.set_ylim(params.world_bounds_y)
    for k in range(len(obstacles)):
        ax.add_patch(Polygon(obstacles[k], facecolor='black', alpha=1, edgecolor='black'))


if __name__ == '__main__':
    # choose algorithm to use
    algorithm = "birrt"  # Choose between "rrt" or "birrt" or "mrs_birrt" or "p_mrs_birrt" or "de_p_mrs_birrt"

    # Obstacles. An obstacle is represented as a convex hull of a number of points.
    # First row is x, second is y (position of vertices)
    w = 0.2
    obstacles_1 = [
        np.array([[0, 0], [1, 0], [1, 0.1], [0, w]]),
        np.array([[0, 0], [w, 0.2], [0.1, 2], [0.0, 2.0]]),
        np.array([[0, 2 - w], [1, 2], [1, 2 + w], [0, 2 + w]]),
        np.array([[1 - w, 0], [1 + w, 0], [1 + w, 1], [1, 1]]),
        np.array([[1 - w, 2 + w], [1 + w, 2 + w], [1 + w, 1.5], [1, 1.5]]),
        np.array([[0.8, 1], [1 + w, 1], [1 + w, 1 + w], [0.8, 1 + w]]),
        np.array([[0.8, 1.5], [1 + w, 1.5], [1 + w, 1.5 + w], [0.8, 1.5 + w]]),

        np.array([[-0.5, -0.5], [-1.5, -0.5], [-1 - w, -1.5 - w], [-0.8, -1.5 - w]]),

        np.array([[0.5, -1.2], [2.0, -1.2], [1 + w, -1.5 - w], [0.8, -1.5 - w]])
    ]

    obstacles_2 = [
        np.array([[-2, -1], [-2, -1+w], [-1+w, -1+w], [-1+w, -1]]),
        np.array([[-1+w, -2], [-1+w, -1+w], [-1, -1+w], [-1, -2]]),

        np.array([[2, 1], [2, 1 - w], [1 - w, 1 - w], [1 - w, 1]]),
        np.array([[1 - w, 2], [1 - w, 1 - w], [1, 1 - w], [1, 2]]),

        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[-1, 1.5], [-1, 2], [-0.5, 2], [-0.5, 1.5]])
    ]

    obstacles_3 = [
        np.array([[-2, -1], [-2, -1 + w], [-1 + w, -1 + w], [-1 + w, -1]]),
        np.array([[-1 + w, -2], [-1 + w, -1 + w], [-1, -1 + w], [-1, -2]]),

        np.array([[2, 1], [2, 1 - w], [1 - w, 1 - w], [1 - w, 1]]),
        np.array([[1 - w, 2], [1 - w, 1 - w], [1, 1 - w], [1, 2]]),

        np.array([[-2, 1 - w], [-2, 1], [-1 + w, 1], [-1 + w, 1 - w]]),
        np.array([[-1 + w, 1 - w], [-1 + w, 2], [-1, 2], [-1, 1 - w]]),

        np.array([[2, -1 + w], [2, -1], [1 - w, -1], [1 - w, -1 + w]]),
        np.array([[1 - w, -1 + w], [1 - w, -2], [1, -2], [1, -1 + w]]),
    ]

    obstacles_4 = [
        #np.array([[-2, -1], [-2, -1+w], [-1+w, -1+w], [-1+w, -1]]),
        #np.array([[-1+w, -2], [-1+w, -1+w], [-1, -1+w], [-1, -2]]),

        #np.array([[2, 1], [2, 1 - w], [1 - w, 1 - w], [1 - w, 1]]),
        #np.array([[1 - w, 2], [1 - w, 1 - w], [1, 1 - w], [1, 2]]),

        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[-1, 1.5], [-1, 2], [-0.5, 2], [-0.5, 1.5]])
    ]

    obstacles_5 = [
    ]

    obstacles_6 = [
        np.array([[0, -0.75], [0, 1], [0.5, 1], [0.5, -0.75]]),
        np.array([[-2.2, -0.5], [-2.2, 0], [-0.8, 0], [-0.8, -0.5]]),
    ]

    obstacles_7 = [
        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[0, -0.75], [0, 1], [0.5, 1], [0.5, -0.75]]),
        np.array([[-1, -2], [-1, -1.25], [0, -1.25], [0, -2]]),
        np.array([[-2.2, -0.5], [-2.2, 0], [-0.8, 0], [-0.8, -0.5]]),
    ]

    obstacles_8 = [
        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[0, -0.75], [0, 1], [0.5, 1], [0.5, -0.75]]),
        np.array([[-1, -2], [-1, -1.25], [0, -1.25], [0, -2]]),
        np.array([[-2.2, -0.5], [-2.2, 0], [-0.8, 0], [-0.8, -0.5]]),
        np.array([[-1.5, 0.5], [-1.5, 1.25], [-1, 1.25], [-1, 0.5]]),
        np.array([[2, 0.5], [2, -0.25], [1, -0.25], [1, 0.5]]),
    ]

    obstacles_9 = [
        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[-1, 1.5], [-1, 2], [-0.5, 2], [-0.5, 1.5]]),
        np.array([[0, -0.75], [0, 1], [0.5, 1], [0.5, -0.75]]),
        np.array([[-1, -2], [-1, -1.25], [0, -1.25], [0, -2]]),
        np.array([[-2.2, -0.5], [-2.2, 0], [-0.8, 0], [-0.8, -0.5]]),
        np.array([[-1.5, 0.5], [-1.5, 1.25], [-1, 1.25], [-1, 0.5]]),
        np.array([[1, 2], [1, 1.25], [0, 1.25], [0, 2]]),
        np.array([[2, 0.5], [2, -0.25], [1, -0.25], [1, 0.5]]),
        np.array([[-0.25, 0.25], [-0.25, 0.5], [-0.5, 0.5], [-0.5, 0.25]]),
        np.array([[-2.25, -2.25], [-2.25, -1.75], [-1.5, -1.75], [-1.5, -2.25]])
    ]

    # x = 0.55
    # y = 1.25

    obstacles_10 = [
        np.array([[0.5, -1.5], [0.5, -1], [1, -1], [1, -1.5]]),
        np.array([[-1, 1.5], [-1, 2], [-0.5, 2], [-0.5, 1.5]]),
        np.array([[0, -0.75], [0, 1], [0.5, 1], [0.5, -0.75]]),
        np.array([[-1, -2], [-1, -1.25], [0, -1.25], [0, -2]]),
        np.array([[-2.2, -0.5], [-2.2, 0], [-0.8, 0], [-0.8, -0.5]]),
        np.array([[-1.5, 0.5], [-1.5, 1.25], [-1, 1.25], [-1, 0.5]]),
        np.array([[1, 2], [1, 1.25], [0, 1.25], [0, 2]]),
        np.array([[2, 0.5], [2, -0.25], [1, -0.25], [1, 0.5]]),
        np.array([[-0.25, 0.25], [-0.25, 0.5], [-0.5, 0.5], [-0.5, 0.25]]),
        np.array([[-2.25, -2.25], [-2.25, -1.75], [-1.5, -1.75], [-1.5, -2.25]]),
        np.array([[-0.75, - 1.], [-0.75, - 0.5], [-0.25, - 0.5], [-0.25, - 1.]]),
        np.array([[-0.6, 2.], [-0.6, 2.5], [0.1, 2.5], [0.1, 2.]]),
        np.array([[-0.1, - 2.5], [-0.1, - 2.], [0.5, - 2.], [0.5, -2.5]]),
        np.array([[0.6, 0.7], [0.6, 1.2], [1.2, 1.2], [1.2, 0.7]]),
        np.array([[-0.6, 0.8], [-0.6,  1.3], [-0.1, 1.3], [-0.1, 0.8]]),
        np.array([[0.05, - 1.25], [0.05, - 0.85], [0.45, - 0.85], [0.45, - 1.25]]),
        np.array([[0.55, - 2.25], [0.55, - 1.55], [1.25, - 1.55], [1.25, - 2.25]]),
        #np.array([[x, y], [x, y+0.7], [x+0.7, y+0.7], [x+0.7, y]])
    ]

    w = 0.1
    l = 0.5
    a = 0.03
    x1 = -1.5
    y1 = -1.5

    obstacles_11 = [
        np.array([[x1-l, y1+l], [x1-l, y1+l+w], [x1+l-a, y1+l+w], [x1+l-a, y1+l]]),
        np.array([[x1 - l - w, y1 - l], [x1 - l - w, y1 - l - w], [x1 + l + w, y1 - l - w], [x1 + l + w, y1 - l]]),
        np.array([[x1 + l, y1 - l], [x1 + l, y1 + l - a], [x1 + l + w, y1 + l - a], [x1 + l + w, y1 - l]]),
        np.array([[x1 - l, y1 - l - w], [x1 - l, y1 + l + w], [x1 - l - w, y1 + l + w], [x1 - l - w, y1 - l - w]]),

        np.array([[-(x1 - l), y1 + l], [-(x1 - l), y1 + l + w], [-(x1 + l - a), y1 + l + w], [-(x1 + l - a), y1 + l]]),
        np.array([[-(x1 - l - w), y1 - l], [-(x1 - l - w), y1 - l - w], [-(x1 + l + w), y1 - l - w],
                  [-(x1 + l + w), y1 - l]]),
        np.array([[-(x1 + l), y1 - l], [-(x1 + l), y1 + l - a], [-(x1 + l + w), y1 + l - a], [-(x1 + l + w), y1 - l]]),
        np.array([[-(x1 - l), y1 - l - w], [-(x1 - l), y1 + l + w], [-(x1 - l - w), y1 + l + w],
                  [-(x1 - l - w), y1 - l - w]]),

        np.array([[x1 - l, -(y1 + l)], [x1 - l, -(y1 + l + w)], [x1 + l - a, -(y1 + l + w)], [x1 + l - a, -(y1 + l)]]),
        np.array([[x1 - l - w, -(y1 - l)], [x1 - l - w, -(y1 - l - w)], [x1 + l + w, -(y1 - l - w)],
                  [x1 + l + w, -(y1 - l)]]),
        np.array([[x1 + l, -(y1 - l)], [x1 + l, -(y1 + l - a)], [x1 + l + w, -(y1 + l - a)], [x1 + l + w, -(y1 - l)]]),
        np.array([[x1 - l, -(y1 - l - w)], [x1 - l, -(y1 + l + w)], [x1 - l - w, -(y1 + l + w)],
                  [x1 - l - w, -(y1 - l - w)]]),

        np.array([[-(x1 - l), -(y1 + l)], [-(x1 - l), -(y1 + l + w)], [-(x1 + l - a), -(y1 + l + w)],
                  [-(x1 + l - a), -(y1 + l)]]),
        np.array([[-(x1 - l - w), -(y1 - l)], [-(x1 - l - w), -(y1 - l - w)], [-(x1 + l + w), -(y1 - l - w)],
                  [-(x1 + l + w), -(y1 - l)]]),
        np.array([[-(x1 + l), -(y1 - l)], [-(x1 + l), -(y1 + l - a)], [-(x1 + l + w), -(y1 + l - a)],
                  [-(x1 + l + w), -(y1 - l)]]),
        np.array([[-(x1 - l), -(y1 - l - w)], [-(x1 - l), -(y1 + l + w)], [-(x1 - l - w), -(y1 + l + w)],
                  [-(x1 - l - w), -(y1 - l - w)]])
    ]

    #print(np.array([[x, y], [x, y+0.5], [x+0.5, y+0.5], [x+0.5, y]]))
    # Choose the obstacles
    obstacles = obstacles_9

    if algorithm == "rrt":
        # Initialization
        params = RRT_Params()

        # Draw map
        draw_map(obstacles, params)

        # Set font size
        plt.rcParams.update({'font.size': 12})

        # Start and goal positions
        xy_start = np.array([-1.5, -1.5])
        plt.plot(xy_start[0], xy_start[1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
        xy_goal = np.array([1.5, 1.5])
        plt.plot(xy_goal[0], xy_goal[1], marker='o', color='green', markersize=10, fillstyle='none', markeredgewidth=3,
                 label='Goal')

        # xy_start = np.array([0.5, 0.5])
        # plt.plot(xy_start[0], xy_start[1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
        # xy_goal = np.array([-1.5, 0.8])
        # plt.plot(xy_goal[0], xy_goal[1], marker='o', color='green', markersize=10, fillstyle='none', markeredgewidth=3,
        #          label='Goal')
        # plt.legend()

        # Plot RRT path and plot it
        P = rrt_path(obstacles, xy_start, xy_goal, params)
        plt.plot(P[:, 0], P[:, 1], color='red', linewidth=2.5, label='Path from RRT')

        # Smooth RRT path and plot it
        # P_smooth = SmoothPath(P, obstacles, smoothiters=100)
        # plt.plot(P_smooth[:, 0], P_smooth[:, 1], linewidth=2.5, color='orange', label='Smoothened path')

        if params.visualize:
            # plt.legend()
            plt.show()

        # plt.savefig('plot.png', dpi=300, bbox_inches='tight')

    elif algorithm == "birrt":
        # Initialization
        params = BiRRT_Params()

        # Draw map
        draw_map(obstacles, params)

        # Set font size
        plt.rcParams.update({'font.size': 12})

        # Start and goal positions
        xy_start = np.array([-1.5, -1.5])
        plt.plot(xy_start[0], xy_start[1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
        xy_goal = np.array([1.5, 1.5])
        plt.plot(xy_goal[0], xy_goal[1], marker='o', color='green', markersize=10, fillstyle='none', markeredgewidth=3,
                 label='Goal')

        # xy_start = np.array([0.5, 0.5])
        # plt.plot(xy_start[0], xy_start[1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
        # xy_goal = np.array([-1.5, 0.8])
        # plt.plot(xy_goal[0], xy_goal[1], marker='o', color='green', markersize=10, fillstyle='none', markeredgewidth=3,
        #          label='Goal')
        # plt.legend()

        # Plot RRT path and plot it
        P = bidirectional_rrt_path(obstacles, xy_start, xy_goal, params)
        plt.plot(P[:, 0], P[:, 1], color='red', linewidth=2.5, label='Path from RRT')

        # Smooth RRT path and plot it
        # P_smooth = SmoothPath(P, obstacles, smoothiters=100)
        # plt.plot(P_smooth[:, 0], P_smooth[:, 1], linewidth=2.5, color='orange', label='Smoothened path')

        if params.visualize:
            # plt.legend()
            plt.show()

        # plt.savefig('plot.png', dpi=300, bbox_inches='tight')

    elif algorithm == "mrs_birrt":
        # Initialization
        params = BiRRT_MRS_Params()

        # Draw map
        draw_map(obstacles, params)

        # Set font size
        plt.rcParams.update({'font.size': 12})

        # Start and goal positions
        xy_start = [np.array([-1.5, -1.5]), np.array([1.5, -1.5])]
        xy_goal = [np.array([1.5, 1.5]), np.array([-1.5, 1.5])]
        NoP = len(xy_start)
        for i in range(NoP):
            plt.plot(xy_start[i][0], xy_start[i][1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
            plt.plot(xy_goal[i][0], xy_goal[i][1], marker='o', color='green', markersize=10, fillstyle='none',
                     markeredgewidth=3,
                     label='Goal')

        # Plot RRT path and plot it
        paths, pad_lengths = mrs_bidirectional_rrt_path(obstacles, xy_start, xy_goal, params)
        for i in range(len(paths)):
            limit = len(paths[i]) - pad_lengths[i]
            colors = ['red', 'cyan', 'lime', 'purple']
            plt.plot(paths[i][:limit, 0], paths[i][:limit, 1], color=colors[i], linewidth=2.5)

        # Smooth RRT path and plot it
        # P_smooth = SmoothPath(P, obstacles, smoothiters=100)
        # plt.plot(P_smooth[:, 0], P_smooth[:, 1], linewidth=2.5, color='orange', label='Smoothened path')

        if params.visualize:
            # plt.legend()
            plt.show()

        # plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    elif algorithm == "p_mrs_birrt":
        # Initialization
        params = Prioritized_BiRRT_MRS_Params()

        # Draw map
        draw_map(obstacles, params)

        # Set font size
        plt.rcParams.update({'font.size': 12})

        # Start and goal positions
        xy_start = [np.array([-1.5, -1.5]), np.array([1.5, -1.5])]
        xy_goal = [np.array([1.5, 1.5]), np.array([-1.5, 1.5])]
        NoP = len(xy_start)
        for i in range(NoP):
            plt.plot(xy_start[i][0], xy_start[i][1], 'x', color='green', markersize=10, label='Start', markeredgewidth=3)
            plt.plot(xy_goal[i][0], xy_goal[i][1], marker='o', color='green', markersize=10, fillstyle='none',
                     markeredgewidth=3,
                     label='Goal')

        # assign priorities
        priorities = [0, 0]

        # Plot RRT path and plot it
        paths, pad_lengths = prioritized_mrs_bidirectional_rrt_path(obstacles, xy_start, xy_goal, params, priorities)
        for i in range(len(paths)):
            limit = len(paths[i]) - pad_lengths[i]
            colors = ['red', 'cyan', 'lime', 'purple']
            plt.plot(paths[i][:limit, 0], paths[i][:limit, 1], color=colors[i], linewidth=2.5)

        # Smooth RRT path and plot it
        # P_smooth = SmoothPath(P, obstacles, smoothiters=100)
        # plt.plot(P_smooth[:, 0], P_smooth[:, 1], linewidth=2.5, color='orange', label='Smoothened path')

        if params.visualize:
            # plt.legend()
            plt.show()

    elif algorithm == "de_p_mrs_birrt":
        # Initialization
        params = CA_P_BiRRT_MRS_Params()

        # Draw map
        draw_map(obstacles, params)

        # Set font size
        plt.rcParams.update({'font.size': 12})

        # Start and goal positions
        xy_start = [np.array([-1.5, -1.5]), np.array([1.5, -1.5])]
        xy_goal = [np.array([1.5, 1.5]), np.array([-1.5, 1.5])]
        NoP = len(xy_start)
        colors = ['red', 'green', 'lime', 'purple']
        for i in range(NoP):
            plt.plot(xy_start[i][0], xy_start[i][1], 'x', color=colors[i], markersize=10, label='Start', markeredgewidth=3)
            plt.plot(xy_goal[i][0], xy_goal[i][1], marker='o', color=colors[i], markersize=10, fillstyle='none',
                     markeredgewidth=3,
                     label='Goal')

        # assign priorities
        priorities = [0, 0]

        # Plot RRT path and plot it
        paths, pad_lengths = de_p_mrs_bidirectional_rrt_path(obstacles, xy_start, xy_goal, params, priorities)

        for i in range(len(paths)):
            limit = len(paths[i]) - pad_lengths[i]
            colors = ['red', 'green', 'lime', 'purple']
            plt.plot(paths[i][:limit, 0], paths[i][:limit, 1], color=colors[i], linewidth=2.5)

        # Smooth RRT path and plot it
        # P_smooth = SmoothPath(P, obstacles, smoothiters=100)
        # plt.plot(P_smooth[:, 0], P_smooth[:, 1], linewidth=2.5, color='orange', label='Smoothened path')

        if params.visualize:
            # plt.legend()
            plt.show()
    else:
        print("Algorithm not defined")
