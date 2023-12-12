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
    @classmethod
    def __dir__(self):
        """
        Override __dir__ to exclude __init_subclass__ from the output.

        Returns:
        - List of attributes and methods.
        """
        return [attr for attr in dir(cls) if attr != '__init_subclass__']
