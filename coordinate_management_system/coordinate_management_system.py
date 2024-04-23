from unittest import TestCase
from copy import deepcopy

# Function to check if a factory creates identifier instances
def identifier_1(factory):
    instance_1 = factory()
    instance_2 = factory()
    return instance_1 is instance_2

# A simple Ship class representing a ship in a maritime company
class Ship:
    def __init__(self, name):
        self.name = name

# Factory functions for creating ship instances
def primary_ship_factory():
    # This factory always returns the same instance (singleton)
    if not hasattr(primary_ship_factory, 'instance'):
        primary_ship_factory.instance = Ship("Main Ship")
    return primary_ship_factory.instance

def secondary_ship_factory():
    # This factory creates a new instance each time
    return Ship("Secondary Ship")

# Test case to evaluate singleton behavior
class Evaluate(TestCase):
    def test_primary_ship_is_singleton(self):
        # Test that the primary ship factory always returns the same instance
        self.assertTrue(identifier_1(primary_ship_factory))

    def test_secondary_ship_is_not_singleton(self):
        # Test that the secondary ship factory creates new instances
        self.assertFalse(identifier_1(secondary_ship_factory))