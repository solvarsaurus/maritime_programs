from enum import Enum
from math import sin, cos, sqrt, atan2, radians, degrees


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    GEOGRAPHIC = 3


class Point:
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)
        elif system == CoordinateSystem.GEOGRAPHIC:
            # Interpret a as latitude and b as longitude in degrees
            self.x = a
            self.y = b

    # Factory methods for creating various types of coordinates
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    @staticmethod
    def new_geographic_point(lat, lon):
        return Point(lat, lon, CoordinateSystem.GEOGRAPHIC)

    # Methods to convert between coordinate systems
    def to_cartesian(self):
        if self.x and self.y:
            return (self.x, self.y)
        else:
            raise ValueError("Cannot convert to Cartesian")

    def to_polar(self):
        r = sqrt(self.x ** 2 + self.y ** 2)
        theta = atan2(self.y, self.x)
        return (r, theta)

    def to_geographic(self):
        lat = self.x
        lon = self.y
        return (lat, lon)

    # Calculate the distance between two points (Haversine formula for geographic coordinates)
    @staticmethod
    def haversine_distance(p1, p2):
        R = 6371  # Earth's radius in kilometers
        lat1, lon1 = radians(p1.x), radians(p2.y)
        lat2, lon2 = radians(p2.x), radians(p2.y)

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance


if __name__ == '__main__':
    # Example usage of different coordinate types
    p1 = Point.new_cartesian_point(3, 4)
    p2 = Point.new_polar_point(5, 0.785)  # 0.785 radians is approximately 45 degrees
    p3 = Point.new_geographic_point(37.7749, -122.4194)  # San Francisco (lat, lon)
    p4 = Point.new_geographic_point(34.0522, -118.2437)  # Los Angeles (lat, lon)

    print("Cartesian:", p1)
    print("Polar:", p2)
    print("Geographic (SF):", p3)
    print("Geographic (LA):", p4)

    # Calculate distance between geographic points (San Francisco to Los Angeles)
    distance = Point.haversine_distance(p3, p4)
    print("Distance between SF and LA:", distance, "km")