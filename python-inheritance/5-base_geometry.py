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
    def area(self):
        """
        Public instance method that raises an Exception with the message"area() is not implemented"
        raises:
            - exception: always raised with the specified message
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Public instance method that validates an integer value.
        Parameters:
            - name (str): The name of the value.
            - value: The value to be validated.
        Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
