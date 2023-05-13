import numpy as np
import matplotlib.pyplot as plt

#experiment 1
com_time_vs_dens_1_de = [0.0705, 0.0835, 0.0803, 0.0785, 0.0575, 0.0786, 0.0637, 0.0938, 0.0853, 0.1118]
it_vs_dens_1_de = [62, 64, 70, 58, 48, 76, 62, 66, 92, 68]
com_time_vs_dens_1_01 = [0.2629, 0.1792, 0.2480, 0.1621, 0.2759, 0.3264, 0.2823, 0.2674, 0.2194, 0.2920]
it_vs_dens_1_01 = [294, 217, 272, 176, 222, 269, 262, 272, 223, 304]
com_time_vs_dens_1_02 = [0.1184, 0.1003, 0.1070, 0.1164, 0.1431, 0.1215, 0.1665, 0.1178, 0.1389, 0.1335]
it_vs_dens_1_02 = [118, 107, 102, 133, 130, 92, 148, 117, 130, 146]
com_time_vs_dens_1_04 = [0.0648, 0.0793, 0.0628, 0.0449, 0.0562, 0.0437, 0.0860, 0.0579, 0.0516, 0.0905]
it_vs_dens_1_04 = [56, 66, 65, 52, 61, 42, 68, 47, 45, 84]
com_time_vs_dens_2_de = [0.2717, 0.4574, 0.2284, 0.4470, 0.3476, 0.3724, 0.2620, 0.4056, 0.2709, 0.2771]
com_time_vs_dens_2_01 = [0.8008, 0.8928, 0.9271, 0.6559, 0.7945, 0.6858, 0.7991, 0.4622, 0.8873, 0.6993]
com_time_vs_dens_2_02 = [0.4107, 0.3649, 0.3604, 0.4578, 0.4657, 0.5365, 0.4481, 0.4467, 0.4704, 0.4291]
com_time_vs_dens_2_04 = [0.2543, 0.2610, 0.3991, 0.2661, 0.3868, 0.2855, 0.3767, 0.4117, 0.3111, 0.2653]
com_time_vs_dens_3_de = [0.5172, 0.7323, 0.6842, 0.4530, 0.6991, 0.4951, 0.7069, 0.5507, 0.6599, 0.8000]
com_time_vs_dens_3_01 = [1.2151, 1.2735, 1.0538, 1.0344, 1.5759, 1.2382, 1.3269, 1.2288, 1.1930, 1.2742]
com_time_vs_dens_3_02 = [0.6940, 0.8283, 0.6985, 0.6434, 0.6743, 0.7529, 0.7132, 0.8945, 0.9299, 0.9361]
com_time_vs_dens_3_04 = [0.5834, 0.3463, 0.5512, 0.5998, 0.4449, 0.6092, 0.4178, 0.5507, 0.4403, 0.6202]
com_time_vs_dens_4_de = [0.7835, 0.7334, 0.8529, 0.7987, 0.6711, 0.9875, 0.6536, 0.5368, 0.4708, 1.0232]
com_time_vs_dens_4_01 = [1.5787, 1.2719, 1.4135, 1.4094, 1.2788, 1.2531, 1.4556, 1.2486, 1.4836, 1.5749]
com_time_vs_dens_4_02 = [0.8052, 0.9613, 0.6801, 1.2601, 0.7251, 0.7469, 0.7975, 1.0166, 1.1380, 0.7750]
com_time_vs_dens_4_04 = [0.4446, 0.4446, 0.6039, 0.3521, 0.5316, 0.4835, 0.4951, 0.5467, 0.7185, 0.7128]
com_time_vs_dens_5_de = [1.4883, 1.7276, 1.3537, 1.0573, 2.7846, 1.6617, 1.9329, 2.8091, 2.4033, 2.3150]
com_time_vs_dens_5_01 = [2.1207, 1.7750, 1.9300, 2.1717, 1.4875, 1.9782, 2.8039, 2.6656, 2.7537, 2.1169]
com_time_vs_dens_5_02 = [1.7610, 1.5823, 1.1119, 1.6738, 1.5004, 1.8837, 1.5489, 1.6641, 1.8540, 1.5744]
com_time_vs_dens_5_04 = [1.1403, 1.2045, 1.0597, 1.0287, 0.8425, 0.9754, 0.9951, 1.6940, 1.2537, 0.9664]
com_time_vs_dens_6_de = [2.9225, 3.2359, 1.7461, 2.2062, 2.0110, 2.8175, 2.1697, 1.6042, 3.3591, 3.0738]
com_time_vs_dens_6_01 = [4.6091, 2.5970, 4.8296, 4.4278, 6.0808, 2.3625, 2.2595, 5.0136, 3.3415, 3.5943]
it_vs_dens_6_01 = [1635, 4014, 2158, 2339]
com_time_vs_dens_6_02 = [7.4664, 2.3556, 3.0044, 2.5886, 3.9145, 3.9987, 1.9730, 2.3532, 1.5914, 2.4255]
it_vs_dens_6_02 = [4050, 902, 1203, 906, 1700, 2228, 811, 985, 571, 944]
com_time_vs_dens_6_04 = [3.7207, 16.6926, 3.6950, 3.6271, 3.8780, 3.1563, 3.1481, 6.9281, 6.0668, 6.1918]
it_vs_dens_6_04 = [1216, 5328, 1023, 957, 1030, 836, 851, 1856, 1704, 1954]

# density array in procent
density = [0, 6.30, 10.30, 14.80, 20.55, 30.15]
com_time_vs_dens_de = [com_time_vs_dens_1_de, com_time_vs_dens_2_de, com_time_vs_dens_3_de, com_time_vs_dens_4_de, com_time_vs_dens_5_de, com_time_vs_dens_6_de]
com_time_vs_dens_01 = [com_time_vs_dens_1_01, com_time_vs_dens_2_01, com_time_vs_dens_3_01, com_time_vs_dens_4_01, com_time_vs_dens_5_01, com_time_vs_dens_6_01]
com_time_vs_dens_02 = [com_time_vs_dens_1_02, com_time_vs_dens_2_02, com_time_vs_dens_3_02, com_time_vs_dens_4_02, com_time_vs_dens_5_02, com_time_vs_dens_6_02]
com_time_vs_dens_04 = [com_time_vs_dens_1_04, com_time_vs_dens_2_04, com_time_vs_dens_3_04, com_time_vs_dens_4_04, com_time_vs_dens_5_04, com_time_vs_dens_6_04]

y1 = com_time_vs_dens_de
y2 = com_time_vs_dens_01
y3 = com_time_vs_dens_02
y4 = com_time_vs_dens_04

plot = 'limit'

if plot == 'graph':
    # Calculate average and spread
    averages1 = np.mean(y1, axis=1)  # Average of each list in y
    spreads1 = np.std(y1, axis=1)  # Standard deviation of each list in y
    averages2 = np.mean(y2, axis=1)  # Average of each list in y
    spreads2 = np.std(y2, axis=1)  # Standard deviation of each list in y
    averages3 = np.mean(y3, axis=1)  # Average of each list in y
    spreads3 = np.std(y3, axis=1)  # Standard deviation of each list in y
    averages4 = np.mean(y4, axis=1)  # Average of each list in y
    spreads4 = np.std(y4, axis=1)  # Standard deviation of each list in y
    # Plot average and spread
    plt.plot(density, averages1, color='blue', label='Adaptive extension')
    plt.fill_between(density, averages1 - spreads1, averages1 + spreads1, color='lightblue', alpha=0.5)
    plt.plot(density, averages2, color='red', label='MRS-BiRRT: d = 0.1m')
    plt.fill_between(density, averages2 - spreads2, averages2 + spreads2, color='red', alpha=0.25)
    plt.plot(density, averages3, color='green', label='MRS-BiRRT: d = 0.2m')
    plt.fill_between(density, averages3 - spreads3, averages3 + spreads3, color='green', alpha=0.25)
    plt.plot(density, averages4, color='orange', label='MRS-BiRRT: d = 0.4m')
    plt.fill_between(density, averages4 - spreads4, averages4 + spreads4, color='orange', alpha=0.25)

    # Customize plot
    plt.xlabel('density of obstacles [%]')
    plt.ylabel('computation time [s]')
    #plt.title('Average and Spread')
    plt.legend()

    # Display the plot
    plt.show()

# BARPLOT
elif plot == 'barplot':
    # Calculate average and spread
    averages1 = np.mean(y1, axis=1)  # Average of each list in y
    spreads1 = np.std(y1, axis=1)  # Standard deviation of each list in y
    averages2 = np.mean(y2, axis=1)  # Average of each list in y
    spreads2 = np.std(y2, axis=1)  # Standard deviation of each list in y
    averages3 = np.mean(y3, axis=1)  # Average of each list in y
    spreads3 = np.std(y3, axis=1)  # Standard deviation of each list in y
    averages4 = np.mean(y4, axis=1)  # Average of each list in y
    spreads4 = np.std(y4, axis=1)  # Standard deviation of each list in y

    # Set the width of the bars
    bar_width = 0.2

    # Set the positions of the x-axis ticks
    step = 1.5
    bar_positions = np.arange(0, step*len(density), step)

    # Create the bar plot
    plt.bar(bar_positions, spreads1, width=bar_width, label='MRS-BiRRT with AE')
    plt.bar(bar_positions + bar_width, spreads2, width=bar_width, label='MRS-BiRRT with d = 0.1m')
    plt.bar(bar_positions + 2 * bar_width, spreads3, width=bar_width, label='MRS-BiRRT with d = 0.2m')
    plt.bar(bar_positions + 3 * bar_width, spreads4, width=bar_width, label='MRS-BiRRT with d = 0.4m')

    # Add horizontal grid lines
    plt.grid(axis='y', linestyle='-')

    # Customize the plot
    plt.xlabel('Density of obstacles [%]')
    plt.ylabel('Standard deviation of computation time [s]')
    #plt.title('Bar Plot')
    plt.xticks(bar_positions + 1.5 * bar_width, density)
    plt.legend()

    # Display the plot
    plt.show()

elif plot == 'ex2':
    # experiment 2
    com_time_de = [2.4139, 2.1569, 3.3003, 1.7095, 1.2555, 4.3905, 6.2371, 2.0046, 4.0303, 2.0358, 1.4931, 5.0234, 2.0844, 2.5389, 2.1954]
    com_time_01 = [6.3409, 5.7092, 4.2465, 8.1641, 5.7702, 4.6977, 7.0816, 2.6159, 7.4437, 2.9620, 3.2739, 3.9640, 7.1459, 4.9552, 6.9798]
    com_time_02 = [2.5921, 2.0786, 2.6234, 2.7908, 2.3005, 13.7479, 8.7866, 1.5734, 3.7526, 2.3228, 2.4941, 2.6737, 3.6375, 7.4126, 7.0638]
    com_time_04 = [30.3269, 1.4618, 6.4448, 2.6226, 19.0664, 1.9937, 3.4788, 1.1952, 6.4055, 5.4018, 6.4622, 16.6474, 1.5571, 5.0424, 2.6403]

    data = [com_time_de, com_time_01, com_time_02, com_time_04]  # Combine the data into a single list

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the boxplot
    ax.boxplot(data)

    # Set the labels for x-axis
    ax.set_xticklabels(['AE', 'd = 0.1m', 'd = 0.2m', 'd = 0.4m'])
    ax.grid(axis='y', linestyle='-')

    # Set the title and labels
    #ax.set_title('Comparison of Four Datasets')
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Computation time [s]')

    # Display the plot
    plt.show()

elif plot == 'limit':
    limit_com_time_1 = [1.4608, 1.5632, 1.6850, 2.4149, 1.0851, 1.3593, 1.3256, 2.2742, 1.1984, 1.9067]
    limit_com_time_2 = [1.6057, 1.9142, 1.7857, 0.9313, 1.6031, 1.4533, 1.0928, 1.7202, 1.2805, 2.8799]
    limit_com_time_3 = [1.0956, 1.0740, 1.6531, 2.0445, 1.5604, 1.6483, 1.8103, 1.9438, 1.6749, 1.1236]
    limit_com_time_4 = [2.1989, 1.9773, 1.5469, 1.7424, 1.8893, 1.5097, 1.6629, 1.5155, 1.6710, 0.8098]
    limit_com_time_5 = [1.3145, 1.7080, 1.8221, 1.6894, 1.5384, 2.6990, 2.6209, 1.2732, 2.4897, 2.1876]
    limit_com_time_10 = [2.2173, 1.8104, 1.8804, 1.5487, 1.6658, 1.4100, 1.4859, 1.9468, 2.0092, 1.5506]

    # Calculate average and spread
    averages1 = np.mean(limit_com_time_1, axis=0)  # Average of each list in y
    spreads1 = np.std(limit_com_time_1, axis=0)  # Standard deviation of each list in y
    averages2 = np.mean(limit_com_time_2, axis=0)  # Average of each list in y
    spreads2 = np.std(limit_com_time_2, axis=0)  # Standard deviation of each list in y
    averages3 = np.mean(limit_com_time_3, axis=0)  # Average of each list in y
    spreads3 = np.std(limit_com_time_3, axis=0)  # Standard deviation of each list in y
    averages4 = np.mean(limit_com_time_4, axis=0)  # Average of each list in y
    spreads4 = np.std(limit_com_time_4, axis=0)  # Standard deviation of each list in y
    averages5 = np.mean(limit_com_time_5, axis=0)  # Average of each list in y
    spreads5 = np.std(limit_com_time_5, axis=0)  # Standard deviation of each list in y
    averages10 = np.mean(limit_com_time_10, axis=0)  # Average of each list in y
    spreads10 = np.std(limit_com_time_10, axis=0)  # Standard deviation of each list in y

    x_values = [1, 2, 3, 4, 5, 10]
    averages = [averages1, averages2, averages3, averages4, averages5, averages10]
    std_dev = [spreads1, spreads2, spreads3, spreads4, spreads5 ,spreads10]

    # Create the figure and axes
    fig, ax = plt.subplots()

    ax.plot(x_values, averages, color='blue', marker='o', label='Averages 1')
    ax.errorbar(x_values, averages, yerr=std_dev, fmt='none', color='blue', capsize=5)

    # Customize plot
    plt.xlabel('Value of limit1 and limit2')
    plt.ylabel('Computation time [s]')
    # plt.title('Average and Spread')
    plt.legend()

    # Display the plot
    plt.show()




