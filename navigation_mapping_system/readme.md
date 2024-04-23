# Maritime Navigation and Mapping System (MNMS)

This project demonstrates a system for managing multiple types of coordinates, including Cartesian, Polar, and Geographic. In a factory design pattern.
The code is designed with a maritime focus, allowing users to create and manipulate different types of coordinates and calculate distances between geographic points.

## Getting Started

To run this code, you need Python installed. The code includes no external dependencies and can be executed with the Python standard library.

### Coordinate Systems

- **Cartesian**: Represents coordinates with x and y values.
- **Polar**: Represents coordinates with radius (rho) and angle (theta).
- **Geographic**: Represents coordinates with latitude and longitude, commonly used in maritime contexts.

### Classes

- **Point**: A class representing a coordinate. It can be initialized in Cartesian, Polar, or Geographic systems.
- **CoordinateSystem**: An enum representing the different types of coordinate systems.
- **PointFactory**: A factory class for creating different types of points.

### Features

- **Coordinate Creation**: Create instances of Cartesian, Polar, or Geographic points using factory methods.
- **Coordinate Conversion**: Convert between Cartesian, Polar, and Geographic coordinate systems.
- **Distance Calculation**: Calculate the distance between geographic points using the Haversine formula. This is useful for maritime navigation, where distances between points on a sphere are needed.

### Examples:

Here's an example of creating and working with different types of coordinates:

```python
# Creating different types of points
p1 = Point.new_cartesian_point(3, 4)  # Cartesian
p2 = Point.new_polar_point(5, 0.785)  # Polar (approx. 45 degrees)
p3 = Point.new_geographic_point(37.7749, -122.4194)  # Geographic (San Francisco)

# Converting between coordinate systems
polar = p1.to_polar()  # Convert Cartesian to Polar
geographic = p2.to_geographic()  # Convert Polar to Geographic

print("Cartesian:", p1)
print("Polar:", p2)
print("Geographic (SF):", p3)

# Calculating distance between geographic points
sf = Point.new_geographic_point(37.7749, -122.4194)  # San Francisco
la = Point.new_geographic_point(34.0522, -118.2437)  # Los Angeles
distance = Point.haversine_distance(sf, la)
print("Distance between SF and LA:", distance, "km")