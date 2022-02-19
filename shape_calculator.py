class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width < 51 and self.height < 51:
            picture_width = ("*" * self.width) + "\n"
            full_picture = picture_width * self.height
            return full_picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, second):
        firstWidth = self.width
        firstHeight = self.height
        secondWidth = second.width
        secondHeight = second.height
        countHeight = 0
        countWidth = 0
        if firstHeight > secondHeight:
            countHeight = firstHeight // secondHeight
        if firstWidth > secondWidth:
            countWidth = firstWidth // secondWidth
        return countWidth * countHeight


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(width=side_length, height=side_length)
        self.side_length = side_length

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side_length):
        self.side_length = side_length
        self.width = side_length
        self.height = side_length

