#!/usr/bin/python3
"""
Class Square Module
"""


class Square():
    """
    Attr:
        width
        height
    Methods:
        __init__(self, *args, **kwargs)
        area(self)
        perimeter(self)
        __str__(self)
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialize square instance with width and height"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if (self.height != self.width):
                self.height = self.width
        else:
            self.height = self.width = 0

    def area(self):
        """ Return area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Return perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return string representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.width)
    print(s.height)
    print(s.area())
    print(s.perimeter())
    print(s.__str__())
