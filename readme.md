# Maritime Software Suite

Welcome to the Maritime Software Suite, a collection of programs designed to facilitate and streamline various maritime operations. This repository contains several distinct programs, each serving a unique purpose in the maritime industry, from navigation and mapping to container ship management.

## Programs Overview

### Maritime Coordinate Management System (MCMS) 

This project contains a unit test to evaluate singleton design partern in a maritime company context. It is designed to test whether factory functions return unique instances or singleton instances. This concept is useful in maritime applications to ensure specific objects, such as ships, GPS systems, or database connections, are not duplicated.

### Maritime Container Ship Blueprint System (MCSP)

This project demonstrates the Prototype design pattern applied to a maritime context focusing on container ships. The pattern allows for creating new container instances by copying existing prototypes. This approach is useful when creating different types of containers with common attributes but varying specific details.

### Maritime Navigation and Mapping System (MNMS)

This project demonstrates a system for managing multiple types of coordinates, including Cartesian, Polar, and Geographic. In a factory design pattern. The code is designed with a maritime focus, allowing users to create and manipulate different types of coordinates and calculate distances between geographic points.

### Maritime Operations Management System (MOMS)

This program serves as a factory for creating and managing various maritime operations. It uses the factory design pattern to encapsulate object creation, allowing users to create different maritime operation scenarios and objects with flexibility and scalability. It's useful for handling maritime logistics, operations, and related activities.

## Getting Started

To run these programs, you'll need Python installed on your system. No external dependencies are required for basic usage, but advanced features might necessitate additional packages. Each program has its own entry point, typically using an `if __name__ == '__main__':` block.

1. **Clone this repository** to your local system:
```bash
   git clone https://github.com/your-username/maritime-software-suite.git
```

2. Navigate to the program directory you'd like to run, then execute the script using Python:

```bash 
cd maritime-software-suite
python maritime_coordinate_system.py 
```

## for the Maritime Coordinate System program
Follow the on-screen prompts (if applicable) to interact with the program.

## Usage Scenarios
### Here are some common usage scenarios for these programs:

* Navigation and Mapping: Use the Maritime Coordinate System to work with coordinates, convert between different systems, and calculate distances between geographic points.
* Container Ship Management: Utilize the Maritime Container Ship Prototype to create and manage different container ship configurations.
* Maritime Operations: Leverage the Maritime Operations Management System to create various maritime operations and manage them through a factory pattern.

## Contributing
We welcome contributions to this repository! If you have suggestions for new features, improvements, or bug fixes, please submit a pull request with a detailed explanation of your changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)