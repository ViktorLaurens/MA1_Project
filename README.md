# MA1 Project: Adaptive Extension Bidirectional RRT for MRS

This project serves as an initial introduction and comprehensive exploration of task and motion planning, laying the groundwork for further investigation. Different variants of RRT are implemented in python including RRT itself, its bidirectional variant (BiRRT) and the extended version of this for multi_robot systems (MRS) without and without priority based planning. In this project adaptive extension is introduced to standard BiRRT extended for the use of MRSs. This means that the length of new edges to expand the tree with changes based upon a certain logic such as the density of obstacles in the neighborhood of new nodes. This algorithm is found in ```BiRRT_MRS_P_DE.py```. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Documentation](#documentation)
- [License](#license)
- [Contributing](#contributing)
- [Credits](#credits)
- [Contact](#contact)

## Installation 

To use this repository, you'll need to have Python and its dependencies installed on your machine. Follow these steps to get started:

1. Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/ViktorLaurens/MA1_Project.git
```

2. Navigate to the root directory of the cloned repository:
```bash
cd MA1_Project
```

## Usage

To launch the simulation for the motion planning algorithms in the "RRT_variants" folder, follow these steps:

1. Ensure you are in the root directory of the cloned repository.

2. Run the following command to execute the main script:
```bash
python main.py
```

This will start the simulation and execute the main function, which launches the motion planning algorithms.

**Note:** Make sure you have all the necessary dependencies installed. If any required libraries are missing, you may need to install them using pip or any package manager you prefer.

3. Explore the simulation and observe the motion planning algorithms in action. The program may generate output or display visualizations based on its implementation.

4. Feel free to modify the code in the .py files, including the "main.py" file and the files within the "RRT_variants" folder, to experiment with different algorithms or customize the behavior as needed.

5. After making changes, rerun the `python main.py` command to see the updated simulation results.

That's it! You can now use and explore the motion planning algorithms by running the main script in the repository. Remember to check the README or documentation within the repository for any additional instructions or details specific to the project.

## Features

This repository provides the following features:

### 1. Motion Planning Algorithms
- **RRT (Rapidly-Exploring Random Trees)**: Implements the RRT algorithm for motion planning in robotics.
- **BiRRT (Bidirectional Rapidly-Exploring Random Trees)**: Includes an enhanced version of the RRT algorithm with trees expanding from both the starting configuration and goal configuration.
- - **MRS-BiRRT (Rapidly-Exploring Random Trees for Multi-Robot Systems)**: Offers the extension of BiRRT for planning the path of multiple robots with and without priority planning (collision avoidance has yet to be implemented in all these versions). 
- **DE-MRS-BiRRT (better: AE-MRS-BiRRT)**: Implements adaptive extension to the MRS-BiRRT.

### 2. Simulation Environment
- **Visualization**: Provides a 2D simulation environment for visualizing the motion planning algorithms.
**Does not yet include: 
- **Obstacle Generation**: Tools for generating random obstacles within the simulation environment.
- **Path Evaluation**: Allows evaluation of the generated paths in terms of optimality, smoothness, and collision avoidance.

### 3. Configuration and Customization
- **Parameter Tuning**: Allows users to configure various parameters of the motion planning algorithms to adapt them to specific scenarios.
- **Algorithm Comparison**: Provides tools for comparing the performance and efficiency of different motion planning algorithms.
- **Algorithm Extension**: Offers a modular architecture that enables users to extend the repository with additional motion planning algorithms.

## Documentation

Comprehensive documentation explaining the theoretical foundations and implementation details of the motion planning algorithms can be found here: 
[Establishing_and_implementation_of_multi_agent_motion_planning_algorithms_for_simultaneous_operation_of_a_dual_arm_robotic_system (1).pdf](https://github.com/ViktorLaurens/MA1_Project/files/11470049/Establishing_and_implementation_of_multi_agent_motion_planning_algorithms_for_simultaneous_operation_of_a_dual_arm_robotic_system.1.pdf)

## License

## License

This project is licensed under the [MIT License](LICENSE).

The MIT License is a permissive open-source license that allows you to use, modify, and distribute this software for any purpose, both commercially and non-commercially. The license text can be found in the [LICENSE](LICENSE) file.

### Permissions
- Commercial use: ✔️
- Modification: ✔️
- Distribution: ✔️
- Private use: ✔️

### Limitations
- Liability: ❌
- Warranty: ❌

By using this software, you agree to the terms and conditions of the MIT License.

For more information about the MIT License, please visit [opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).
