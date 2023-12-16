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
        
        # Assign each argument to the right attribute
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
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        self.__y = value

# Example usage and testing
if __name__ == "__main__":
    # Create instances of Rectangle and print their IDs
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)