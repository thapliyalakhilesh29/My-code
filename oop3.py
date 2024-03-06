
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7)*self.radius**2
    
    def set_radius(self,radius):
        self.radius=radius

    def get_radius(self):
        return self.radius
    

circle = Circle(7)
print(circle.area())
print(circle.get_radius())
print(circle.set_radius(6))
print(circle.get_radius())
print(circle.area())
