#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is a special rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the str method"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
            )

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter method"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = val
            self.height = val

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args[:5]):
                setattr(self, attrs[i], arg)
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        """returns dict object"""
        dict_obj = {}
        dict_obj["id"] = self.id
        dict_obj["size"] = self.size
        dict_obj["x"] = self.x
        dict_obj["y"] = self.y
        return dict_obj
