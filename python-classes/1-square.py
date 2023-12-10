class Square:
    """
    square class defines a square by:
        - private instance attribute: __size
        - instantiation with optional size
    """
    def __init__(self, size = 0):
        """
        initializes a new square instance
        Parameters:
            size (int, optional): the size of the square Default to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size