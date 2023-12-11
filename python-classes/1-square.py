"""Define a square class"""
class Square:
    """Represent a square.
    Attributes:
        __size (int): the size of the square.
    """
    def __init__(self, size):
        """Initializes a new square instance.
        Args:
            size (int): the size of the square Default to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size