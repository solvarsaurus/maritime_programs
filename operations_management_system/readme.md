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

```python
mom = MaritimeOperationMachine()  # Initialize the machine
operation = mom.initiate_operation()  # Get user input to choose an operation
operation.execute()  # Execute the selected operation