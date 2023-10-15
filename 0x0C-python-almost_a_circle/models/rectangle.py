#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle instance"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance
        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
            id (int): The identity of the new Rectangle
        Raises:
            TypeError: If either of width or height is not an int
            ValueError: If either of width or height <= 0
            TypeError: If either of x or y is not an int
            ValueError: If either of x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, nwidth):
        """Set the width of the Rectangle"""
        if type(nwidth) != int:
            raise TypeError("width must be an integer")
        if nwidth <= 0:
            raise ValueError("width must be > 0")
        self.__width = nwidth

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, nheight):
        """Set the height of the Rectangle"""
        if type(nheight) != int:
            raise TypeError("height must be an integer")
        if nheight <= 0:
            raise ValueError("height must be > 0")
        self.__height = nheight

    @property
    def x(self):
        """Get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, nx):
        """Set the x coordinate of the Rectangle"""
        if type(nx) != int:
            raise TypeError("x must be an integer")
        if nx < 0:
            raise ValueError("x must be >= 0")
        self.__x = nx

    @property
    def y(self):
        """Get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, ny):
        """Set the y coordinate of the Rectangle"""
        if type(ny) != int:
            raise TypeError("y must be an integer")
        if ny < 0:
            raise ValueError("y must be >= 0")
        self.__y = ny

    def area(self):
        """"Calculates the area of a Rectangle """
        return self.__width * self.__height

    def display(self):
        """Displays a Rectangle"""
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns a new representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
