class Shape:
    def set_width(self, width):
        pass
    def set_height(self, height):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def set_width(self, width):
        self.size = width

    def set_height(self, height):
        self.size = height
