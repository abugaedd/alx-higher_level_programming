#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ The Square Class """
    def __init__(self, size):
        """ The size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
