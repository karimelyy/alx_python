#!/usr/bin/python3
"""
Module for defining the square class
"""
class Square:
      """
    Square class defines a square by:
        - Private instance attribute: __size
        - Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
          """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size