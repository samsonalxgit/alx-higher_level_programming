#!/usr/bin/python3
"""
create a class Square
"""


class Square:
    """
    Define the setter and getter for the size
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if (len(value) != 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square depending of the size received"""
        if (self.__size == 0):
            print()
        else:
            if (self.__position[1] > 0):
                for sn in range(self.__position[1]):
                    print()
            for n in range(self.__size):
                for s in range(self.__position[0]):
                    print(' ', end="")
                for y in range(self.__size):
                    print('#', end="")
                print()

    def __str__(self):
        string = ""
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            return string
        else:
            if self.__position[1] > 0:
                for pos in range(self.__position[1]):
                    string += "\n"
            for pos in range(self.__size):
                string += " " * self.__position[0] + "#" * self.__size + '\n'
        return string[:-1]
