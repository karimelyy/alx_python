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
        super().__init__(size, size)  # Call the constructor of the parent class (Rectangle)
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