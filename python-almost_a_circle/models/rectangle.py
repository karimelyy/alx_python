"""
This module contains the Rectangle class, which inherits from the Base class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        id (int): The ID of the Rectangle instance.
        __width (int): The width of the Rectangle.
        __height (int): The height of the Rectangle.
        __x (int): The x-coordinate of the Rectangle.
        __y (int): The y-coordinate of the Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int, optional): The x-coordinate of the Rectangle.
            y (int, optional): The y-coordinate of the Rectangle.
            id (int, optional): The ID for the instance. If provided, assigns
                the given ID; otherwise, uses the default logic from the Base class.
        """
        # Call the super class with id
        super().__init__(id)
        
        # Assign each argument to the right attribute with validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, attribute_name, value):
        """Validate that the given value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def validate_non_negative_integer(self, attribute_name, value):
        """Validate that the given value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance using '#' characters and accounting for x and y."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Override the __str__ method to return a formatted string."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Assign arguments to attributes in the order:
            1st argument - id attribute
            2nd argument - width attribute
            3rd argument - height attribute
            4th argument - x attribute
            5th argument - y attribute

        Alternatively, use key-worded arguments (**kwargs) to assign values to attributes.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i == 0:
                    setattr(self, attributes[i], arg)
                else:
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)