class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width


# Example usage:
rectangle = Rectangle(5, 4)
print("Length:", rectangle.get_length())
print("Width:", rectangle.get_width())
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())

rectangle.set_length(7)
rectangle.set_width(3)
print("\nAfter setting new dimensions:")
print("Length:", rectangle.get_length())
print("Width:", rectangle.get_width())
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
