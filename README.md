# MA1 Project: Adaptive Extension Bidirectional RRT for MRS

This project serves as an initial introduction and comprehensive exploration of task and motion planning, laying the groundwork for further investigation. Different variants of RRT are implemented in python including RRT itself, its bidirectional variant (BiRRT) and the extended version of this for multi_robot systems (MRS) without and without priority based planning. In this project adaptive extension is introduced to standard BiRRT extended for the use of MRSs. This means that the length of new edges to expand the tree with changes based upon a certain logic such as the density of obstacles in the neighborhood of new nodes. This algorithm is found in ```python BiRRT_MRS_P_DE.py```. 

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

List the key features and functionalities of your project.

## Documentation

Provide links or instructions for accessing additional documentation, such as a separate documentation website, a wiki page, or relevant articles and tutorials.

## License

Specify the license under which your project is released. For example, you can use the following:

This project is licensed under the [MIT License](LICENSE).

## Contributing

If you welcome contributions, outline the guidelines for contributing to your project. Include information on submitting bug reports, feature requests, or pull requests. Specify any coding style requirements or development environment setup instructions.

## Credits

Acknowledge and give credit to any individuals, projects, or resources that have influenced or contributed to your project.

## Contact

Provide a way for users to contact you or the project maintainer. You can include your email address, social media handles, or a link to a contact form.

