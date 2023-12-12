"""define an empty class BaseGeometry"""
from collections.abc import Iterable


class BaseGeometry:
    """
    The class is a placeholder for geometry-related classes.
    Attributes:
        - No attributes are defined in this base class.
    Methods:
        - __init__(self): Constructor method for the BaseGeometry class.
    """
    def __init__(self):
        """
        Constructor for the BaseGeometry class.
        Parameters:
            - None
        Returns:
            - None
        """
        pass
    def area(self):
        """
        Public instance method that raises an Exception with the message"area() is not implemented"
        raises:
            - exception: always raised with the specified message
        """
        raise Exception("area() is not implemented")
    def __dir__(self):
        """
        Override __dir__ to exclude __init_subclass__ from the output.

        Returns:
        - List of attributes and methods.
        """
        return [attr for attr in dir(self) if attr != '__init_subclass__']

