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
"""
7-rectangle.py
Module containing the Rectangle class, which inherits from BaseGeometry.
Classes:
    - Rectangle: A class representing a rectangle.
"""
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

    def __str__(self):
        """
        Override the __str__ method to provide a formatted string representation.
        Returns:
            - str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __dir__(self):
        """
        Override the __dir__ method to provide a consistent order of elements.

        Returns:
            - List of attributes and methods.
        """
        return ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
                '__subclasshook__', '__weakref__', 'area', 'integer_validator',
                '_Rectangle__width', '_Rectangle__height']
"""
8-square.py
Module containing the Square class, which inherits from Rectangle.
Classes:
    - Square: A class representing a square.
"""
class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Methods:
        - __init__(self, size): Constructor for initializing instances of Square.
    Attributes:
        - __size (int): Private attribute for the size of the square.
    Public Methods:
        - area(self): Calculates and returns the area of the square.
    Overrides:
        - __str__(self): Overrides the __str__ method to provide a formatted string representation.
    """
    def __init__(self, size):
        """
        Constructor for the Square class.
        Parameters:
            - size (int): The size of the square.
        Returns:
            - None
        """
        super().__init__(size, size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Public instance method to calculate the area of the square.
        Returns:
            - int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Override the __str__ method to provide a formatted string representation.
        Returns:
            - str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)