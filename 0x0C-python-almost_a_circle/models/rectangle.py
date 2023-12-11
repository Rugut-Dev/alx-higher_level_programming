#!/usr/bin/python3
 """Rectangle class inheriting from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle.
        y (int): y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a Rectangle instance.
    """


from models.base import Base


class Rectangle(Base):
    """Initializes a Rectangle instance"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method
        Ensures private instantiation

"""
        return self.__width

    @width.setter
    def width(self, val):
        """width setter method
        sets private instance
"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """height getter
        gets private instance
"""
        return self.__height

    @height.setter
    def height(self, val):
        """height setter
        sets private instance
"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """x getter method
        gets private instance
"""
        return self.__x

    @x.setter
    def x(self, val):
        """x setter method
        sets private instance
"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """y getter method that gts private instance"""
        return self.__y

    @y.setter
    def y(self, val):
        """y setter method that gets private instance"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        return self.height * self.width

    def display(self):
        for _ in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return (
            f"[Rectangle] ({self.id})"
            f" {self.x}/{self.y} - {self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args[:5]):
                setattr(self, attrs[i], arg)
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}
