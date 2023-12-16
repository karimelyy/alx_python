"""
This module contains the Base class, which serves as the base for other classes
in the project. it manages the 'id' attribute and avoids duplicating code
"""
class Base:
    """
    Base class for managing the 'id' attribute in the project.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of objects created.
        id (int): The public instance attribute representing the ID of the instance.
    """
    # Private class attribute to keep track of objects created
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
            id (int, optional): The ID for the instance. If provided, assigns
                the given ID; otherwise, increments __nb_objects and assigns
                the new value to the instance's ID attribute.
        """
        # Check if an ID is provided
        if id is not None:
            # If provided, assign the given ID
            self.id = id
        else:
            # If not provided, increment __nb_objects and assign the new value
            # to the instance's ID attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Example usage and testing
if __name__ == "__main__":
    # Create instances of Base and print their IDs
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)