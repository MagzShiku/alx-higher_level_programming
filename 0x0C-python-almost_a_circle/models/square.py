#!/usr/bin/python3

"""
this creates a square module
"""


from models.rectangle import Rectangle
"""
we import the property of rectangle from models.rectangle file
"""


class Square(Rectangle):
    """
    define the class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        we initialize the constructor method for the rectangle
        the square is a modification of the rectangle
        """
        super().__init__(size, size, x, y, id)
        """
        this super method calls the Rectangle
        """

    def __str__(self):
        """
        this str returns a string representation of the shape
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        this updates the vey/values of the rectangle
        """
        my_attribute = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
