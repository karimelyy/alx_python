"""define an empty class BaseGeometry"""
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
    def __init_subclass__(cls):
        """
        Placeholder for subclasses to extebd or override
        Args:
            - cls: the subclass being created
        returns:
            - none
        """
        pass
    def area(self):
        """
        Calculate the area.

        Returns:
        - None (not implemented in the base class).
        """
        pass

    def perimeter(self):
        """
        Calculate the perimeter.

        Returns:
        - None (not implemented in the base class).
        """
        pass
