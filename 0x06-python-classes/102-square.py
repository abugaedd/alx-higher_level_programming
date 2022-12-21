#!/usr/bin/python3
"""Create a Class square with size, method of area and getters & setters"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Constructor of a square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = size

    def __it__(self, other):
        """Compare operator <"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Compare operator <="""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Compare operator >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Compare operator >="""
        return (self.areaa() >= other.area())

    def __eq__(self, other):
        """Compare operator =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Compare operator !="""
        return (self.area() != other.area())

    def area(self):
        """Method toget the area of the Square"""
        return (self.__size ** 2)

    @property
