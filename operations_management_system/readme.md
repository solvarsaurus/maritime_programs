# Maritime Operations Management System (MOMS)

This project demonstrates a factory pattern for maritime operations, allowing a maritime company to manage various tasks related to ship operations, maintenance, and navigation. 
It creates operations dynamically based on user input, enabling flexibility and adaptability. The code would display the current state of the ship, allowing for maintenance or navigation tasks to be performed on the ship.

## Getting Started

To run this code, you'll need Python. The code doesn't require additional dependencies and can be executed with Python's standard library.

### Code Structure

- **MaritimeOperation**: An abstract base class representing a maritime operation with an `execute` method to perform the operation.
- **Maintenance and Navigation**: Concrete classes inheriting from `MaritimeOperation`, representing specific ship-related tasks.
- **MaritimeOperationFactory**: An abstract factory class for creating maritime operations. Specific factories derive from this base class.
- **MaintenanceFactory and NavigationFactory**: Concrete factories for creating instances of specific maritime operations.
- **MaritimeOperationMachine**: The main class that manages available operations and provides a method to create new instances based on user input.
  - Contains a list of factories for different operations.
  - The `AvailableOperation` enum represents the types of operations available.
  - The `initiate_operation` method lets users choose an operation and provide details, then creates the corresponding instance.

### Usage

To create and execute maritime operations, you can use the `MaritimeOperationMachine`. Here's an example:

```bash
mom = MaritimeOperationMachine()  # Initialize the machine
operation = mom.initiate_operation()  # Get user input to choose an operation
operation.execute()  # Execute the selected operation
```

## Applications
### This factory pattern can be applied to various maritime contexts, including:

* Container Ships: Operations for loading/unloading containers, ship maintenance, and navigation.
* Cruise Ships: Managing entertainment, passenger boarding, safety drills, and maintenance.
* Cargo Ships: Tasks related to cargo handling, equipment maintenance, and navigation.
* Offshore Platforms: Operations for drilling, safety checks, and logistics.
* Fishing Vessels: Managing fishing operations, net maintenance, and catch processing.
* Research Vessels: Data collection, equipment calibration, and navigation.
* Naval Ships: Operations for combat drills, navigation, and equipment maintenance.

## Contributing
If you'd like to contribute, please submit a pull request with detailed explanations of your changes. Ensure new features or bug fixes are accompanied by appropriate test cases.

## License

[MIT](https://choosealicense.com/licenses/mit/)