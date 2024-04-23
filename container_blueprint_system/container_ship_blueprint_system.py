import copy

# Class representing a container with common attributes
class Container:
    def __init__(self, container_number, container_type, description):
        self.container_number = container_number
        self.container_type = container_type
        self.description = description

    def __str__(self):
        return f"Container #{self.container_number} - {self.container_type}: {self.description}"

# Factory class to create containers using the Prototype pattern
class ContainerFactory:
    # Prototype for general container with basic attributes
    container_prototype = Container(0, "General", "General cargo container")

    @staticmethod
    def __new_container(proto, container_number, description):
        result = copy.deepcopy(proto)
        result.container_number = container_number
        result.description = description
        return result

    @staticmethod
    def new_refrigerated_container(container_number, description):
        container = ContainerFactory.__new_container(
            ContainerFactory.container_prototype,
            container_number,
            description
        )
        container.container_type = "Refrigerated"
        return container

    @staticmethod
    def new_dry_container(container_number, description):
        container = ContainerFactory.__new_container(
            ContainerFactory.container_prototype,
            container_number,
            description
        )
        container.container_type = "Dry"
        return container

# Creating specific container instances using the factory
refrigerated_container = ContainerFactory.new_refrigerated_container(
    1001, "Frozen food container"
)
dry_container = ContainerFactory.new_dry_container(
    1002, "Bulk dry goods container"
)

print(refrigerated_container)
print(dry_container)