# Maritime Container Ship Blueprint System

This project demonstrates the Prototype design pattern applied to a maritime context focusing on container ships. 
The pattern allows for creating new container instances by copying existing prototypes. 
This approach is useful when creating different types of containers with common attributes but varying specific details.

## Getting Started

To run this code, you'll need Python. The code has no external dependencies and can run with Python's standard library.

### Code Structure

- **Container**: A class representing a basic container with attributes like `container_number`, `container_type`, and `description`.
- **ContainerFactory**: A factory class that uses the Prototype design pattern to create new containers based on a common prototype. 
    It contains:
  - **Prototype**: The base prototype for general containers.
  - **Methods**:
    - `__new_container(proto, container_number, description)`: Creates a new container by copying the prototype and modifying specific attributes.
    - `new_refrigerated_container(container_number, description)`: Creates a refrigerated container with specific characteristics.
    - `new_dry_container(container_number, description)`: Creates a dry container with specific characteristics.

### Usage

To create container instances for ID, use the factory methods provided by the `ContainerFactory` class. 
Here's an example of creating a refrigerated container and a dry container:

```bash 
# Create a refrigerated container with specific attributes
refrigerated_container = ContainerFactory.new_refrigerated_container(
    1001, "Frozen food container"
)

# Create a dry container with specific attributes
dry_container = ContainerFactory.new_dry_container(
    1002, "Bulk dry goods container"
)
```

# Print container details
```bash 
print(refrigerated_container)  # Output: Container #1001 - Refrigerated: Frozen food container
print(dry_container)  # Output: Container #1002 - Dry: Bulk dry goods container
```
## Prototype Design Pattern

The Prototype design pattern allows you to create new objects by copying existing prototypes, which can be useful when you have similar objects with minor variations. 
In this project, prototypes represent general container types, and factory methods create new containers based on these prototypes with unique attributes.

## Contributing
If you'd like to contribute to this project, please submit a pull request with a detailed explanation of your changes. Ensure that all new features or fixes are accompanied by appropriate test cases.

## License

[MIT](https://choosealicense.com/licenses/mit/)