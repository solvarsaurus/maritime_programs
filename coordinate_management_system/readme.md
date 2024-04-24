# Maritime Coordinate Management System (MCMS)

This project contains a unit test to evaluate singleton design partern in a maritime company context. 
It is designed to test whether factory functions return unique instances or singleton instances. 
This concept is useful in maritime applications to ensure specific objects, such as ships, 
GPS systems, or database connections, are not duplicated.

## Getting Started

To run the tests, you'll need Python and the `unittest` module, which is part of the standard library. No additional dependencies are required.

### Code Structure

- `identifier_1(factory)`: A function that checks whether the given factory function creates singleton instances.
- `Ship`: A simple class representing a ship in a maritime company.
- `primary_ship_factory()`: A factory function that returns the same instance each time (singleton).
- `secondary_ship_factory()`: A factory function that creates a new instance each time (not a singleton).
- `Evaluate`: A test class that checks singleton behavior for `primary_ship_factory` and `secondary_ship_factory`.

### Running the Tests

To run the tests, use the following command:

```bash
python -m unittest test_singleton
```

This will execute all the test cases in the Evaluate class to determine if the factory functions are creating singleton instances or not. 
In other words if it is generating the same instance each time or not.


## Test Cases
* test_primary_ship_is_singleton: Tests whether the primary_ship_factory returns the same instance each time.
* test_secondary_ship_is_not_singleton: Tests whether the secondary_ship_factory creates a new instance each time.

## Contributing
If you would like to contribute to this project, please submit a pull request with a detailed explanation of your changes. 
Ensure that all new features or fixes are accompanied by appropriate test cases.

## License

[MIT](https://choosealicense.com/licenses/mit/)