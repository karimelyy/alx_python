"""
7-rectangle.py
Module containing the Rectangle class, which inherits from BaseGeometry.
Classes:
    - Rectangle: A class representing a rectangle.
"""
class rectangle(BaseGeometry):
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
