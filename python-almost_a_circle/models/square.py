"""
This module contains the Square class, which inherits from the Rectangle class.
"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        id (int): The ID of the Square instance.
        __size (int): The size of the Square.
        __x (int): The x-coordinate of the Square.
        __y (int): The y-coordinate of the Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of Square
        Args:
            size (int): The size of the Square.
            x (int, optional): The x-coordinate of the Square.
            y (int, optional): The y-coordinate of the Square.
            id (int, optional): The ID for the instance. If provided, assigns
                the given ID; otherwise, uses the default logic from the Rectangle class.
        """
        # Call the super class with id, x, y, width, and height
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method to return a formatted string."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
