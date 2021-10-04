#Shadowfray
'''
For freecodeacademy.org

Creates objects that are squares and rectangles, allowing you
to change the width and height for each. It can also tell you
the area, diameter and length of the diagonal.

.get_picture() prints a picture of the rectangle

.get_amount_inside() tells you how many subrectangles can fit inside
the rectangle

the Square class inherents all traits from Rectangle, but is changed
so that the shape is a square where all sides are equal.
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height}'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            rectangleString = '' #blank string we'll return w the picture later
            middleZoneHorz = self.width - 2 #the width of the blank space

            rectangleString += ('*' * self.width) + '\n'
            for i in range(self.height - 2):
                rectangleString += '*' + (' ' * middleZoneHorz) + '*\n'
            rectangleString += ('*' * self.width) + '\n'

            return rectangleString

    def get_amount_inside(self, width2, height2):
        height_amount = self.height // height2
        width_amount = self.width // width2
        #we multiply these two together bc its an area
        total_inside = height_amount * width_amount
        return total_inside

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side
        
    def __str__(self):
        return f'Square(side={self.height})'

    def set_side(self, new):
        self.width = new
        self.height = new

    def set_width(self, new):
        self.width = new
        self.height = new

    def set_height(self, new):
        self.width = new
        self.height = new


