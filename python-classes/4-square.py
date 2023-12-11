"""Define a square class"""
class Square:
    """Represent a square.
    Attributes:
        __size (int): the size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new square instance.
        Args:
            size (int): the size of the square Default to 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        """Getter method for size attribute
        Returns:
            int: the size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Setter method for the size attribute
        Args:
            value (int): the new size value
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Calculates the area of the square
        returns:
            int: the area of the square
        """
        return self.__size ** 2
    def my_print(self):
        """Print the square with the character #.
        if size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)