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
class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Methods:
        - __init__(self, width, height): Constructor for initializing instances of Rectangle.
        Attributes:
            - __width (int): Private attribute for the width of the rectangle.
            - __height (int): Private attribute for the height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Constructor for the Rectangle class.
        Parameters:
            - width (int): The width of the rectangle.
            - height (int): The height of the rectangle.
        Returns:
            - None
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Public instance method to calculate the area of the rectangle.

        Returns:
            - int: The area of the rectangle.
        """
        return self.__width * self.__height
    
    def __dir__(self):
        """
        Override __dir__ to provide a consistent order of elements.
        Returns:
            - List of attributes and methods.
        """
        return ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
                '__subclasshook__', '__weakref__', 'area', 'integer_validator',
                '_Rectangle__width', '_Rectangle__height']
