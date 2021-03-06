#!/usr/bin/python3
"""Exports the Square class

   Important Note:
        When using the @property, @setter, and @getter functions
        avoid an infinite recursion by using a different name for their
        function definitions from the attributes they are mutating or
        retrieving.
"""


class Square:
    """Square class that does some things

    Arguments:
        size (int): Size of the square.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: Size of the square."""

        return self.__size

    @size.setter
    def size(self, size):
        """This gets called when class initializes because
        of the `self.size = size` statement in the __init__ method
        which triggers this setter method and sets the __size field.
        Thus self.size is now mapped to the getter and setter methods
        while self.__size gets returned to users.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Find the area of the square instance.

        Returns:
            (int) The area of the square.
        """

        return self.__size ** 2
