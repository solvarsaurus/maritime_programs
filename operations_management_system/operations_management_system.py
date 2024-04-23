from abc import ABC
from enum import Enum, auto

# Abstract base class for maritime operations
class MaritimeOperation(ABC):
    def execute(self):
        pass

# Specific operations for ship-related tasks
class Maintenance(MaritimeOperation):
    def execute(self):
        print("Performing ship maintenance")

class Navigation(MaritimeOperation):
    def execute(self):
        print("Navigating the ship through open waters")

# Abstract factory base class for creating maritime operations
class MaritimeOperationFactory(ABC):
    def create(self, detail):
        pass

# Concrete factories for specific operations
class MaintenanceFactory(MaritimeOperationFactory):
    def create(self, detail):
        print(f"Performing maintenance on {detail}")
        return Maintenance()

class NavigationFactory(MaritimeOperationFactory):
    def create(self, detail):
        print(f"Plotting course for {detail}")
        return Navigation()

# Main machine class to manage operations
class MaritimeOperationMachine:
    class AvailableOperation(Enum):
        MAINTENANCE = auto()
        NAVIGATION = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for operation in self.AvailableOperation:
                name = operation.name.capitalize()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def initiate_operation(self):
        print("Available operations:")
        for index, factory in enumerate(self.factories):
            print(f"{index}: {factory[0]}")

        choice = int(input(f"Choose an operation (0-{len(self.factories)-1}): "))
        detail = input("Specify detail (e.g., ship name or route): ")
        return self.factories[choice][1].create(detail)

# Example usage
if __name__ == "__main__":
    mom = MaritimeOperationMachine()
    operation = mom.initiate_operation()
    operation.execute()